# -*- coding: utf-8 -*-

from generators import numbers

'''
file IO functions
'''
def slurp(filePath):
    # read contents of file to string
    with open(filePath) as x: data = x.read()
    return data

def slurpA(filePath):
    # same as slurp but return Array of lines instead of string
    with open(filePath) as x: data = x.read().splitlines()
    return data

def spit(filePath, data, overwrite=False):
    # write all contents to a file
    mode= 'w' if overwrite else 'a'
    with open(filePath, mode) as x: x.write(data)

def touch(filePath, times=None):
    # touch a file
    with open(filePath, 'a'):
        os.utime(filePath, times)

def rm(filePath):
    # delete a file if exists
    if os.path.isfile(filePath):
        os.remove(filePath)

def partition(l, n):
    """ 
    Yield successive n-sized partitions from l.
    >>> list(partition(range(1,10),2))
    [[1, 2], [3, 4], [5, 6], [7, 8], [9]]
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

class rollin(object):
    '''
    rolling file writer 
    this is a poor mans rolling file appender
    TODO maybe accept a generator function for incrementing file names
    must be infinite or a cycle
    '''
    def __init__(self, directory, filename, extension, limit_megabytes=10):
        self.directory = directory
        self.filename = filename
        self.limit_bytes = limit_megabytes*1024*1024
        self.gen = numbers()

    def open(self):
        sz = "%s/%s_%s.%s" % (self.directory, self.filename, self.gen.next(), self.extension)
        self.f = open(sz, 'a+b')

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def close(self):
        self.f.close()
        
    def write(self,data):
        if self.f.tell() > self.limit_bytes:
            self.close()
            self.open()
        self.f.write(data)
