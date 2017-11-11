# -*- coding: utf-8 -*-

from itertools import dropwhile, takewhile


def split_with(pred, coll):
    '''
    split a collection by the first matching predicate
    split_with(lambda x: x < 3, range(10)
    ([0, 1, 2], [3, 4, 5, 6, 7, 8, 9])
    '''
    return (list(takewhile(pred, coll)), list(dropwhile(pred, coll)))
