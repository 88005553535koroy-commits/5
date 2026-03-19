result = ""
word_number = 1
while True:
    word = input(f"Ввести слово {word_number}: ")
    if word == "stop":
        break
    result = result + word + " "
    word_number += 1

print(result)