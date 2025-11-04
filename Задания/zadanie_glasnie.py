#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    schet = 0
    glasnie = set('уеыаоэяиюё')
    a = input("Введите строку: ").lower()
    for i in a:
        if i in glasnie:
            schet += 1
    print(schet)