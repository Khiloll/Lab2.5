#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys


if __name__ == '__main__':
    # Ввести кортеж одной строкой.
    A = tuple(map(int, input().split()))
    # Проверить количество элементов кортежа.
    if len(A) != 10:
        print("Неверный размер кортежа", file=sys.stderr)
        exit(1)
    # Найти искомую сумму 1.
    s = 0
    for item in A:
        if abs(item) < 5:
            s += item
    print(s)

    # Найти искомую сумму 2.
    s = sum(a for a in A if abs(a) < 5)
    print(s)
