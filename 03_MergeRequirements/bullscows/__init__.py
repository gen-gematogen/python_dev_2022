import textdistance
import random

def bullscows(guess: str, secret: str) -> (int, int):
    return (textdistance.hamming.similarity(guess, secret), textdistance.bag.similarity(guess, secret))

def ask(prompt: str, valid: list[str] = None) -> str:
    word = input(prompt)

    if valid:
        while not word in valid:
            word = input("Ваше слово не из словоря, введите новое: ")
    return word

def inform(format_string: str, bulls: int, cows: int) -> None:
    print(format_string.format(bulls, cows))

def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    word = random.choice(words)
    print(f"В загаданном слове {len(word)} букв")
    count = 0
    user_word = ''

    while word != user_word:
        user_word = ask("Введите слово: ", words)
        b, c = bullscows(word, user_word)
        inform("Быки: {}, Коровы: {}", b, c)
        count += 1

    return count



if __name__ == "__main__":
    print(12345)
    with open("dict.txt") as d:
        words = d.read().split()
        print(gameplay(ask, inform, words))
