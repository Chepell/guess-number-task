"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def divide_and_conquer_predict(number: int = 1) -> int:
    """Угадываем число используя алгоритм разделяй и влавствуй

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    # Задаю начальные значения диапазона чисел
    min_num = 1
    max_num = 100

    # Счетчик количества попыток
    count = 0

    while True:
        count += 1
        # Всегда выбираем число в середине диапазона
        predict_number = (max_num + min_num) // 2
        if predict_number == number:
            break  # выход из цикла если угадали
        elif predict_number > number:  # Если предложенное число оказалось больше загаданного
            # Корректирую верхний диапазон, максимальное число теперь меньше предложенного
            max_num = predict_number - 1
        elif predict_number < number:  # Если предложенное число оказалось меньше загаданного
            # Корректирую нижний диапазон, минимальное число теперь больше предложенного
            min_num = predict_number + 1  # Корректирую нижний диапазон
    return count


def score_game(divide_and_conquer_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        divide_and_conquer_predict ([type]): функция угадывания разделяй и влавствуй

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=1000)  # загадали список чисел

    for number in random_array:
        count_ls.append(divide_and_conquer_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток!")
    return score


if __name__ == "__main__":
    # RUN
    score_game(divide_and_conquer_predict)
