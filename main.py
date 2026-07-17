import customtkinter as ctk
import tkinter as tk

from game import WordleGame
from words import load_words

# =========================
# Настройки
# =========================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

BG_COLOR = "#121213"

EMPTY_COLOR = "#1A1A1B"
BORDER_COLOR = "#565758"

GREEN_COLOR = "#6AAA64"
YELLOW_COLOR = "#C9B458"
GRAY_COLOR = "#787C7E"

# =========================
# Главное приложение
# =========================

class WordlyApp(ctk.CTk):

    ROWS = 6
    COLS = 5

    def __init__(self):

        super().__init__()

        self.title("Wordly")
        self.geometry("500x750")
        self.resizable(False, False)

        self.configure(
            fg_color=BG_COLOR
        )

        # загрузка слов

        self.words = load_words()

        if not self.words:
            raise Exception(
                "Нет слов в n5.txt"
            )

        # игра

        self.game = WordleGame(
            self.words
        )

        self.current_row = 0
        self.current_col = 0

        # клетки

        self.cells = []

        self.create_title()

        self.create_board()

        # клавиатура

        self.bind(
            "<Key>",
            self.keyboard_input
        )

        self.create_info()

    # =====================
    # Заголовок
    # =====================

    def create_title(self):

        title = ctk.CTkLabel(
            self,
            text="WORDLY",
            font=(
                "Arial",
                32,
                "bold"
            )
        )

        title.pack(
            pady=20
        )

    # =====================
    # Игровое поле
    # =====================

    def create_board(self):

        board = ctk.CTkFrame(
            self,
            fg_color=BG_COLOR
        )

        board.pack()

        for row in range(
            self.ROWS
        ):

            row_cells = []

            for col in range(
                self.COLS
            ):

                cell = ctk.CTkLabel(
                    board,
                    text="",
                    width=55,
                    height=55,
                    font=(
                        "Arial",
                        26,
                        "bold"
                    ),
                    fg_color=EMPTY_COLOR,
                    corner_radius=0,
                    text_color='white',
                )


                cell.grid(
                    row=row,
                    column=col,
                    padx=3,
                    pady=3
                )

                row_cells.append(
                    cell
                )

            self.cells.append(
                row_cells
            )
# =====================
    # Информация снизу
    # =====================

    def create_info(self):

        self.info_label = ctk.CTkLabel(
            self,
            text="Введите слово",
            font=(
                "Arial",
                16
            )
        )

        self.info_label.pack(
            pady=20
        )

        self.new_game_button = ctk.CTkButton(
            self,
            text="Новая игра",
            command=self.new_game
        )

        self.new_game_button.pack()

    # =====================
    # Ввод клавиатуры
    # =====================

    def keyboard_input(self, event):

        key = event.keysym

        # удалить букву

        if key == "BackSpace":

            if self.current_col > 0:

                self.current_col -= 1

                self.cells[
                    self.current_row
                ][
                    self.current_col
                ].configure(
                    text=""
                )

            return

        # проверить слово

        if key == "Return":

            self.check_word()

            return

        # ввод букв

        if len(event.char) == 1:

            if event.char.isalpha():

                if self.current_col < self.COLS:

                    self.cells[
                        self.current_row
                    ][
                        self.current_col
                    ].configure(
                        text=event.char.upper()
                    )

                    self.current_col += 1

    # =====================
    # Проверка слова
    # =====================

    def check_word(self):

        if self.current_col != 5:
            self.info_label.configure(
                text="Нужно 5 букв!"
            )
            return

        word = ""

        for cell in self.cells[self.current_row]:

            word += cell.cget(
                "text"
            ).lower()

        if word not in self.words:

            self.info_label.configure(
                text="Такого слова нет!"
            )

            return

        result = self.game.check_word(
            word
        )

        self.paint_result(
            result
        )

        if self.game.win:

            self.info_label.configure(
                text="🎉 Победа!"
            )

            return

        self.current_row += 1
        self.current_col = 0

        if self.current_row >= 6:

            self.info_label.configure(
                text=f"😔 Было слово: {self.game.secret.upper()}"
            )

    # =====================
    # Покраска клеток
    # =====================

    def paint_result(self, result):

        colors = {

            "green":
                GREEN_COLOR,

            "yellow":
                YELLOW_COLOR,

            "gray":
                GRAY_COLOR

        }

        for i in range(5):

            self.cells[
                self.current_row
            ][i].configure(

                fg_color=
                colors[result[i]],

                text_color=
                "white"

            )

    # =====================
    # Новая игра
    # =====================

    def new_game(self):

        print("Новая игра нажата")

        self.game.new_game()

        self.current_row = 0
        self.current_col = 0

        for row in self.cells:
            for cell in row:
                cell.configure(
                    text="",
                    fg_color=EMPTY_COLOR,
                    text_color="white"
                )

        self.info_label.configure(
            text="Введите слово"
        )

        self.update()

# =========================
# Запуск
# =========================

if __name__ == "__main__":

    app = WordlyApp()

    app.mainloop()