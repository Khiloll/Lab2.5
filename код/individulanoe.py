#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def check_ordered_tuple(t):
    # Проверка на упорядоченность по возрастанию
    if all(t[i] <= t[i + 1] for i in range(len(t) - 1)):
        print("Кортеж упорядочен по возрастанию")
    else:
        # Находим номер первого элемента, нарушающего упорядоченность
        index_of_first_unordered = next((i for i in range(len(t) - 1) if t[i] > t[i + 1]), None)
        print("Кортеж не упорядочен по возрастанию. Нарушение упорядоченности на элементе с индексом:", index_of_first_unordered)


# Пример кортежей для проверки
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (1, 3, 2, 4, 5)

# Проверяем упорядоченность кортежей
check_ordered_tuple(tuple1)
check_ordered_tuple(tuple2)
