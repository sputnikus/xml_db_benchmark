#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@package xml_db_benchmark
@author Martin Putniorz <mputniorz@gmail.com>
@version 0.0

@section DESCRIPTION

Benchmark of BaseX DB in Python
'''

import BaseXClient
import time
from xmldbbench import xml_string_generator, bench, TestSession

class BasexSession(TestSession):
    '''
    Test session for BaseX API
    '''
    def __init__(self):
        '''
        Constructor initializes default BaseX session a creates testdb
        '''
        self._session = BaseXClient.Session('localhost', 1984, 'admin', 'admin')
        self._session.execute("create db testdb")
        
    def __del__(self):
        '''
        Destructor drops testdb and closes session
        '''
        self._session.execute("drop db testdb")
        self._session.close()    
        
    def write_test_small(self):
        '''
        Writes small XML string into /small document
        '''
        elements = xml_string_generator(10, "small")     
        self._session.add("small.xml", "/small", elements)
        print self._session.info()
        
    def write_test_large(self):
        '''
        Writes large XML string into /large document
        '''
        elements = xml_string_generator(10000, "large")     
        self._session.add("large.xml", "/large", elements)
        print self._session.info()
        
    def read_test_small(self):
        '''
        Reads all elements from /small document
        '''
        query_string = 'for $ele in //small return $ele'
        query = self._session.query(query_string)
        start = time.clock()
        query.init()
        while query.more():
            query.next()
        print "Query took ", ((time.clock() - start) * 1000), " ms"    
        query.close()
        
    def read_test_large(self):
        '''
        Reads all elements from /large document
        '''
        query_string = 'for $ele in //large return $ele'
        query = self._session.query(query_string)
        start = time.clock()
        query.init()
        while query.more():
            query.next()
        print "Query took ", ((time.clock() - start) * 1000), " ms"
        query.close()
        
if __name__ == '__main__':
    bench(BasexSession())