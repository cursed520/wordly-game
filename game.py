import random

class WordleGame:
    def __init__(self, words):
        self.words = words
        self.secret = random.choice(words)
        self.max_attempts = 6
        self.attempts = 0
        self.win = False

    def check_word(self, word):
        """
        Возвращает список цветов:
        green  - буква на месте
        yellow - буква есть, но место другое
        gray   - буквы нет
        """

        if len(word) != 5:
            return None

        result = ["gray"] * 5
        secret_letters = list(self.secret)

        # Сначала ищем зеленые буквы
        for i in range(5):
            if word[i] == self.secret[i]:
                result[i] = "green"
                secret_letters[i] = None

        # Потом ищем желтые
        for i in range(5):
            if result[i] == "green":
                continue

            if word[i] in secret_letters:
                result[i] = "yellow"
                index = secret_letters.index(word[i])
                secret_letters[index] = None

        self.attempts += 1

        if word == self.secret:
            self.win = True

        return result

    def new_game(self):
        self.secret = random.choice(self.words)
        self.attempts = 0
        self.win = False

        print('Новое слово', self.secret)