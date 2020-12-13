# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

# 12. Ввести список А из 10 элементов, найти сумму элементов,
# больших 2 и меньших 20 и кратных 8, их количество и вывести результаты на экран.


if __name__ == '__main__':
    A = list(map(int, input("Enter 10 items separated by a space> ").split(" ")))
    if len(A) != 10:
        print("Error! Wrong list size", file=sys.stderr)
        exit(1)

    sum = 0
    qua = 0
    for i in A:
        if 2 < i < 20 and (i % 8) == 0:
            sum += i
            qua += 1

    print(f"Sum elements = {sum} \nQuatity of elements = {qua}")
