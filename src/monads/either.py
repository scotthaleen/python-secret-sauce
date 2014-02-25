# -*- coding: utf-8 -*-



""" 
   simple implementation of either monad
"""
class Either(object):
    def __init__(self):
        raise NotImplementedError( "Should not have instantiated this" )
    def isLeft(self): return False
    def left(self):
        raise NotImplementedError( "No value present" )
    def isRight(self): return False
    def right(self):
        raise NotImplementedError( "No value present" )

#LeftProjection
class Left(Either):
    def __init__(self, value):
        self.value = value
    #overrides
    def isLeft(self): return True
    def left(self): return self.value

#RightProjection        
class Right(Either):
    def __init__(self, value):
        self.value = value
    #overrides
    def isRight(self): return True
    def right(self): return self.value
