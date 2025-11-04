#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    u = set("qwertyuiopasdfghjklzxcvbnm")

    A = {"a", "e", "f", "i"}
    B = {"a","b", "k", "n"}
    C = {"e","f","n","o","w","x"}
    D = {"a","d","e","o","p","t","u"}

    An = u.difference(A)
    Bn = u.difference(B)

    X = (A.union(B)).intersection(D)
    Y = (An.intersection(Bn)).difference(C.union(D))

    print(f"Y = {Y}")
    print(f"X = {X}")