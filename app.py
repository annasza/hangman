no_of_tries = 5
word = "python"
used_letters = []

user_word = []


###

for _ in word:
    user_word.append("_")

while True:
    letter = input("Podaj litere: ")
    used_letters.append(letter)
    print(used_letters)