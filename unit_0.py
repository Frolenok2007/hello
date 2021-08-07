
import numpy as np


def game_core_v(number):
    '''Сначала устанавливаем любое random число, а потом загаданны отрезок уменьшаем или увеличиваем методом половинного деления
     в зависимости от того, больше оно или меньше нужного.
    Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    minimal = 1
    maximus = 101
    predict = 50
    while number != predict:
        count += 1
        predict = (maximus + minimal) // 2
        # print(number, predict)  # вывод получаемых значений
        if number > predict:
            minimal = predict
        elif number < predict:
            maximus = predict
    return(count) # выход из цикла, если угадали


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)


score_game(game_core_v)
