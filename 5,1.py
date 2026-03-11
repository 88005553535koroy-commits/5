N = int(input("кол-во слов: "))
result = ""
for number in range(N):
    w = input(f"ввести слово {number +1}: ")
    result = result + w + " "
print(result)