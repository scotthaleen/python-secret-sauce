# -*- coding: utf-8 -*-

from functions import inc

'''
generators
'''
def numbers(start=0):
    n = start
    while True:
        yield n
        n = inc(n)

def AZ():
    for n in range(65,91):
        yield chr(n)

def az():
    for n in range(97,123):
        yield chr(n)

def alphanumeric():
    for n in range(0,10):
        yield str(n)
    for c in (x for x in AZ()):
        yield c
    for c in (x for x in az()):
        yield c
