#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sys

if __name__ == '__main__':

    marshruti = []
    while True:

        print("Список команд:\n")
        print("add - добавить маршрут")
        print("list - вывести список маршрутов")
        print("isk - поиск маршрута по номеру")
        print("end - завершить работу программы")

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

            if marshruti:
                marshruti.sort(key=lambda x: x.get("number",""))

        elif a == "list":
            for i in marshruti:
                print("Начальный маршрут: ", i["start"])
                print("Конечный маршрут: ", i["end"])
                print("Номер маршрута: ", i["number"], "\n")

        elif a == "isk":
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

        elif a == "end":
            break

        else:
            print("Неизвестная команда")


