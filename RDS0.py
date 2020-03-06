import random
from random import randint
number = random.randint(1,100)
computer_number = 50
tries = 1
low = 1
high = 100
# Цикл отгадывания
while computer_number != number:
    if computer_number > number:
        high = computer_number    # Задаем загаданное число верхней границей интервала
# Продолжаем делить полученный интервал наполовину.
        computer_number = computer_number - ((high-low)//2)
        print(computer_number)
    elif computer_number < number:
        low = computer_number    # Задаем загаданное число нижней границей интервала
        computer_number = computer_number + ((high-low)//2)
        print(computer_number)
        tries += 1
     
print("Компьютер потратил", tries, "попытки(ок) на отгадывание числа.")


