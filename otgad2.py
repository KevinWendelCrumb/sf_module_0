import numpy as np
from random import randint
def random_finder(number=1):
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
            elif computer_number < number:
            low = computer_number    # Задаем загаданное число нижней границей интервала
            computer_number = computer_number + ((high-low)//2)
            tries += 1
        break
    return tries

    print("Компьютер потратил", tries, "попытки(ок) на отгадывание числа.")

def score_game(random_finder):
    '''Запускаем игру 1000 раз, чтоб узнать как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(random_finder(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)


# запускаем
score_game(random_finder)