# -*- coding: utf-8 -*-


""" 
   simple implementation of either monad
"""
class Maybe(object):
    def __init__(self): raise NotImplementedError( "abstract")
    def hasValue(self): return False
    def value(self): raise ValueError("No value present")
    def valueOr(self, value): return value
    def isSome(self): return False
    def isNone(self): return False

class some(Maybe):
    def __init__(self, value):
        self._value = value
    #overrides
    def isSome(self): return True
    def hasValue(self): return True
    def value(self): return self._value
    def valueOr(self, value): return self._value
    
class none(Maybe):
    def __init__(self): pass
    #overrides
    def isNone(self): return True
    
