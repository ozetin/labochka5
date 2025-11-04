#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    slov = {}
    print("add - добавить пару")
    print("stop - достаточно пар")

    while True:
        a = input()

        if a == "add":
            kluch = int(input("Введите число-ключ: "))
            znach = input("Введите значение-строку: ")
            slov[kluch] = znach
        elif a == "stop":
            break
        else:
            print("Неизвестная команда", file=sys.stderr)
    new_slov = {v: k for k, v in slov.items()}
    print(slov)
    print(new_slov)