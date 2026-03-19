import random
mistakes = 0
correct = 0
while mistakes < 3:
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    if int(input(f"{a} + {b} = ")) == a + b:
        print("Правильно!")
        correct = correct + 1
    else:
        print("Ответ неверный")
        mistakes = mistakes + 1
print(f"Игра окончена. Правильных ответов: {correct}")