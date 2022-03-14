import sys

no_of_tries = 5
word = "pythonn"
used_letters = []

user_word = []

def find_indexes(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes

for _ in word: # "_" wykorzystujemy gdy nie używamy potem zmiennej z pętli for
    user_word.append("_")

while True:
    letter = input("Podaj litere: ")
    used_letters.append(letter)

    found_indexes = find_indexes(word, letter)
    if len(found_indexes) == 0:
        print("Nie ma takiej litery.")
        no_of_tries -= 1

    if no_of_tries == 0:
        print("Koniec gry:(")
        sys.exit(0)

    print("Użyte litery:", used_letters)