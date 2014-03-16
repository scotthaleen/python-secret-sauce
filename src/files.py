# -*- coding: utf-8 -*-
import os

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

class rollin(object):
    '''
    rolling file writer 
    this is a poor mans rolling file appender
    TODO maybe accept a generator function for incrementing file names
    must be infinite or a cycle
    TODO add optional event function to be triggered on file change 
    (useful if you would like to automatically move the files when 
    done being written too)
    '''
    def __init__(self, directory, filename, extension, limit_megabytes=10):
        self.directory = directory
        self.filename = filename
        self.limit_bytes = limit_megabytes*1024*1024
        self.gen = numbers()
        self.rotate = False

    def open(self):
        sz = "%s/%s_%s.%s" % (self.directory, self.filename, self.gen.next(), self.extension)
        self.f = open(sz, 'a+b')

    def rotate():
        self.rotate = True

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def close(self):
        self.f.close()
        
    def write(self,data):
        if self.rotate or (self.f.tell() > self.limit_bytes):
            self.rotate = False
            self.close()
            self.open()
        self.f.write(data)
