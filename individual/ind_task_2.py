# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import math

# 12. В списке, состоящем из вещественных элементов, вычислить:
# 1) количество элементов списка, лежащих в диапазоне от А до В;
# 2) сумму элементов списка, расположенных после максимального элемента.
# Упорядочить элементы списка по убыванию модулей элементов.


if __name__ == '__main__':

    # Инициализация списка
    Lis = list(map(float, input("Enter items separated by a space> ").split(" ")))
    a = int(input("Enter A of range> "))
    b = int(input("Enter B of range> "))
    if not Lis:
        print("List is empty", file=sys.stderr)
        exit(1)

    # 1 задание
    qua = 0
    for i in Lis:
        if a < i < b:
            qua += 1

    # Поиск максимального элемента и его индекса
    i_max, lis_max = 0, Lis[0]
    for i, item in enumerate(Lis):
        if item > lis_max:
            i_max = i
            lis_max = item

    # 2 задание
    sum = 0
    i_sum = i_max + 1
    while i_sum <= len(Lis):
        if i_sum >= len(Lis):
            break
        sum += Lis[i_sum]
        i_sum += 1

    # Сортировка по модулю пузырьком
    temp = 0
    for i in range(len(Lis)-1):
        for j in range(len(Lis)-i-1):
            if math.fabs(Lis[j+1]) < math.fabs(Lis[j]):
                temp = Lis[j]
                Lis[j] = Lis[j+1]
                Lis[j+1] = temp

    print(f"Task 1: number from a to b = {qua} \nTask 2: sum of elements from max = {sum} \nSort list = {Lis}")
