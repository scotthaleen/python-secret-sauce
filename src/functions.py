# -*- coding: utf-8 -*-

'''
functions
'''
def identity(x): return x

def noop(*args, **kwargs): pass

def head(arr):
    return arr[0]

def empty(arr):
    return not arr

def rest(arr):
    return arr[1:]

def last(arr):
    l = arr[-1:]
    if l:
        return l[0]
    else:
        return None

def nth(arr, i, out_of_range=None):
    if len(arr) > i:
        return arr[i]
    return out_of_range

def juxt(*funs):
    ''' juxtaposition '''
    return lambda *args: [fn(*args) for fn in funs]

#
# TODO
# take array as the path in a nested dict and update that item with
# the new value
# def updateIn(d, arraypath, value):
#

def getIn(d, arraypath, default=None):
    '''
    Take array as the path to a dict item and return the item or default if path does not exist.
    '''
    if not d:
        return d 
    if not arraypath:
        return d
    else:
        return getIn(d.get(arraypath[0]), arraypath[1:], default) \
            if d.get(arraypath[0]) else default

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

def partition(l, n):
    """ 
    Yield successive n-sized partitions from l.
    >>> partition(range(1,10),2)
    [[1, 2], [3, 4], [5, 6], [7, 8], [9]]
    """
    def _part():
        for i in xrange(0, len(l), n):
            yield l[i:i+n]
    #I prefer it to be a list instead of generator
    return [i for i in _part()]


# from julia
def mapreduce(mapFn, reduceFn, items):
    return reduce(reduceFn, map(mapFn, items))

# alpha
def wrapwith(object):
    '''
    dynamically create a with statement object for closed-over resource
    '''
    def __init__(self, openfn, closefn):
        self.openfn = openfn
        self.closefn = closefn
    
    def __enter__(self):
        return self.openfn()

    def __exit__(self, type, value, traceback):
        self.closefn()


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
    returns False if no predicates pass
    '''
    def genfn():
        for p in predicates:
            yield p(obj)
    for x in genfn():
        if x:
            return True
    return False

def select_keys(o, keys=[]):
    '''
    given a map build a new map with only selected keys
    select_keys({'a': 1, 'b': 2, 'c': 3}, keys=['a','b'])
    ;; {'a': 1, 'b': 2}
    '''
    rtn = {}
    for k in keys:
        if k in o:
            rtn[k] = o[k]
    return rtn

def update_in(o, k, fn):
    '''
    given a map update the specific key with the applied function to the key
    update_in({'a': 1}, 'a', lambda x: x+1)
    ;; {'a': 2 } 
    '''
    if k in o:
        o[k]= fn(o[k])
    return o

def reductions(f, seed, coll):
    '''
    like reduce but returns itermediate values of f applied to coll starting with seed
    reductions(lambda a,b: a+b, 0, [1,2,3,4])
    ;; [0, 1, 3, 6, 10]
    '''
    if not coll:
        return [seed]
    accum = [seed]
    last = seed
    for item in coll:
        next_ = f(last, item)
        accum.append(next_)
        last = next_
    return accum


def split_on_condition(pred, coll):
    '''
    apply a predicate to each item in a collection returning a tuple-2 of the items that (pass,fail) condition
    split_on_condition(lambda x: x % 2 == 0, range(10))
    ;; ([0, 2, 4, 6, 8], [1, 3, 5, 7, 9])
    '''
    truthy, falsy = [], []
    for item in coll:
        (truthy if pred(item) else falsy).append(item)
    return (truthy,falsy)

# return a snowman
def snowman(): return u'☃' 
