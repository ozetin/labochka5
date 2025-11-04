#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    str1 = set(input("Введите строку: "))
    str2 = set(input("Введите строку: "))
    obsh = set(str1.intersection(str2))
    print(obsh)