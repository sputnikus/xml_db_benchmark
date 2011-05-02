#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@package xml_db_benchmark
@author Martin Putniorz <mputniorz@gmail.com>
@version 0.0

@section DESCRIPTION

Benchmark of eXist DB in Python
'''

import pyexist
import time
from xmldbbench import TestSession, xml_string_generator, bench

class ExistSession(TestSession):
    '''
    Test session for eXist (pyexist)
    '''
    def __init__(self):
        '''
        Constructor initializes default eXist session
        '''
        self._session = pyexist.ExistDB("admin:admin@localhost:8080/exist/rest/db")
    
    def write_test_small(self):
        '''
        Writes small XML string into /small document
        '''
        start = time.clock()     
        self._session.store("small", xml_string_generator(10, "small"))
        print "Write took ", ((time.clock() - start) * 1000), " ms"
        
    def write_test_large(self):
        '''
        Writes large XML string into /large document
        '''
        start = time.clock()     
        self._session.store("large", xml_string_generator(10000, "large"))
        print "Write took ", ((time.clock() - start) * 1000), " ms"
        
    def read_test_small(self):
        '''
        Reads all elements from /small document
        '''
        query_string = 'for $ele in //small return $ele'
        start = time.clock() 
        _ = self._session.query(query_string)[:]
        print "Query took ", ((time.clock() - start) * 1000), " ms"
        
    def read_test_large(self):
        '''
        Reads all elements from /large document
        '''
        query_string = 'for $ele in //large return $ele'
        start = time.clock() 
        _ = self._session.query(query_string)[:]
        print "Query took ", ((time.clock() - start) * 1000), " ms"     
    
if __name__ == '__main__':
    bench(ExistSession())
        