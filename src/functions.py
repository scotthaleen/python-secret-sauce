# -*- coding: utf-8 -*-

'''
functions
'''
def identity(x): return x

def noop(): pass

def head(arr):
    return arr[0]

def tail(arr):
    return arr[1:]

def juxt(*funs):
    ''' juxtaposition '''
    return lambda x: [fn(x) for fn in funs]

def dictGet(arraypath, j, default=None):
    '''
    Take array as the path to a dict item and return the item or default if path does not exist.
    '''
    if not j:
        return j 
    if not arraypath:
        return j
    else:
        return dictGet(arraypath[1:], j.get(arraypath[0]), default) \
            if j.get(arraypath[0]) else default

# TODO
#def curry(fn):
#    pass

# TODO
# def partial(fn, args):
#     pass

def inc(n):
    return n+1

def dec(n):
    return n-1

def utf8(sz):
    return sz.encode('utf-8')

# return a snowman
def snowman(): return '☃' 
