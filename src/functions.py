# -*- coding: utf-8 -*-

'''
functions
'''
def identity(x): return x

def noop(): pass

def head(arr):
    return arr[0]

def empty(arr):
    return not arr

def tail(arr):
    return arr[1:]

def last(arr):
    l = arr[-1:]
    if l:
        return l[0]
    else:
        return None

def nth(arr, i, out_of_range=None):
    if len(arr) >= i:
        return arr[i]
    return out_of_range

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

def reorganizeList(lst, idxs, out_of_range=None):
    # functions for getting a specific index 
    n = lambda i: lambda l: nth(l, i, out_of_range)
    # function to apply all index functions to a list
    fn = juxt(*map(n, idxs))
    return fn(lst)

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

# from julia
def mapreduce(mapFn, reduceFn, items):
    return reduce(reduceFn, map(mapFn, items))

def juxt_all(predicates, obj):
    '''
    run a juxtaposition of predicates against an object return True 
    if all pass, exits immediately when first False is encountered
    '''
    def genfn():
        for p in predicates:
            yield p(obj)
    for x in genfn():
        if not x:
            return False
    return True

def juxt_any(predicates, obj):
    '''
    reverse of juxt_all - returns immediately on first True
    returns False if no predicates passn
    '''
    def genfn():
        for p in predicates:
            yield p(obj)
    for x in genfn():
        if x:
            return True
    return False

# return a snowman
def snowman(): return u'☃' 
