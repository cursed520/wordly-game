import random
from colorama import Fore, Style
import colorama
import os

colorama.init(autoreset=True)

file = open('n5.txt', 'r', encoding='utf-8')
lines = file.readlines()
file.close()

all_words = []
for line in lines:
    word = line.strip()
    if len(word) == 5:
        all_words.append(word)

while True:
    secret = random.choice(all_words)
    attempts = 0
    while True:
        leval = int(input('Уровень сложности:'))
        if leval == 1:
            max_attempts = 8
            break
        elif leval == 2:
            max_attempts = 6
            break
        elif leval == 3:
            max_attempts = 4
            break
        elif leval == 4:
            max_attempts = 3
            break
        else:
            print("Неверный ввод, попробуйте снова")

    print("\n🎯 Угадай слово из 5 букв!")

    while attempts < max_attempts:
        guess = input(f"\nПопытка {attempts + 1}/{max_attempts}: ").strip().lower()

        if len(guess) != 5:
            print("❌ Нужно ввести слово из 5 букв!")
            continue

        if guess not in all_words:
            print("❌ Такого слова нет в словаре!")
            continue

        if guess == secret:
            print("\n🎉 ПОБЕДА! Ты угадал слово!")
            break

        print("  ", end="")
        for i, letter in enumerate(guess):
            if letter == secret[i]:
                print(Fore.GREEN + letter.upper(), end=" ")
            elif letter in secret:
                print(Fore.YELLOW + letter.upper(), end=" ")
            else:
                print(Fore.LIGHTWHITE_EX + letter.upper(), end=" ")
        print()

        attempts += 1

    else:
        print(f"\n😔 ПРОИГРЫШ! Было загадано: {secret.upper()}")

    while True:
        again = input("\n🔄 Сыграем ещё раз? (д/н): ").strip().lower()
        if again == "д" or again == "н":
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        print("⚠️ Введите 'д' или 'н'")

    if again == "н":
        print("👋 Спасибо за игру! До встречи!")
        break
