#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    school = {}
    print("add - добавить класс")
    print("stop - достаточно классов")

    while True:
        a = input()
        if a == 'stop':
            break
        elif a == 'add':
            name = input("Введите название класса: ")
            kol = int(input("Введите количество учеников: "))
            school[name] = kol
        else:
            print("такой команды нет", file=sys.stderr)

    print("change - изменить количество учеников в классе")
    print("new - добавить класс")
    print("destroy - расформировать класс")
    print("stop - остановить изменения")

    while True:
        a = input()

        if a == 'change':
            klass = input("Класс, который изменяем: ")
            kol = int(input("Новое количество учеников: "))
            school[klass] = kol

        elif a == 'new':
            name = input("Введите название класса: ")
            kol = int(input("Введите количество учеников: "))
            school.setdefault(name, kol)

        elif a == 'destroy':
            name = input("Введите название класса: ")
            del school[name]
        elif a == 'stop':
            break
        else:
            print("Такой команды нет", file=sys.stderr)

    schet = 0
    for i in school:
        schet += school[i]
    print(school)
    print(f"В школе {schet} учеников")
