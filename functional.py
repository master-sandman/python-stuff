# -*- coding: utf-8 -*-

def sum(*args):
    result = 0
    for arg in args:
        result += arg
    return result

def mul(*args):
    result = 1
    for arg in args:
        result *= arg
    return result

def coalesce(*args):
    for arg in args:
        if arg is not None:
            return arg
    return None

def noneif(a, b):
    if a == b:
        return None
    else:
        return a
