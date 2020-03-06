import random
from random import randint
n = 1
i = random.randint(1,100)
def random_finder(num_itterations=1000):
    n = 1
    count = 0
    i = random.randint(1,100)
    print("Компьютер загадал число. Отгадайте его. У вас 10 попыток")
    for i in range(10):
        if i < 50:
            if i > 25:
                n = 26
                while i != n:
                    n += 1
            else:
                n = 1
                while i != n:
                    n += 1
        if n > 50:
            if n < 75:
                n = 51
                while i != n:
                    n += 1
    if n == i:
              print('Вы угадали!' % i)
          
random_finder(num_itterations=1000)