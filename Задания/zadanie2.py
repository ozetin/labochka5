#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sys

if __name__ == '__main__':

    marshruti = []
    print("add - добавить маршрут")
    print("end - закончить ввод маршрутов")
    while True:
        a = input().lower()

        if a == "add":
            start = input("Введите название начального пункта: ")
            end = input("Введите название конечного пункта: ")
            number = int(input("Введите номер маршрута: "))

            marshrut = {
                "start": start,
                "end": end,
                "number": number
            }
            marshruti.append(marshrut)

            if len(marshruti) > 1:
                marshruti.sort(key=lambda x: x.get("number",""))
        elif a == "end":
            break
        else:
            print("неизвестная команда")

    isk_numb = int(input("Введите номер искомого маршрута: "))
    schet = 0

    for i in marshruti:
        if i["number"] == isk_numb:
            schet += 1
            print(f"Начальный пункт: {i['start']}")
            print(f"Конечный пункт: {i['end']}")
            print(f"Номер маршрута: {i['number']}")
    if schet == 0:
        print("Таких маршрутов нет", file=sys.stderr)