import numpy as np
from random import randint

def random_finder(number, predict = 50, tries = 1):
    range = [1, 101]
    # Цикл отгадывания
    while predict != number:
        tries += 1
        if predict < number:
            range[0] = predict    # Задаем загаданное число нижней границей интервала
    # Продолжаем делить полученный интервал наполовину.
            predict = int((predict + range[1]) / 2)
        elif predict > number:
            range[1] = predict    # Задаем загаданное число верхней границей интервала
            predict = int((predict + range[0]) / 2)
    return tries
        
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

