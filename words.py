# words.py

def load_words(filename="n5.txt"):
    words = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                word = line.strip().lower()

                # Берём только слова из 5 букв
                if len(word) == 5 and word.isalpha():
                    words.append(word)

    except FileNotFoundError:
        print("Файл со словами не найден!")

    return words