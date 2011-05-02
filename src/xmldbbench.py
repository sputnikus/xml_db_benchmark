# -*- coding: utf-8 -*-

'''
@package xml_db_benchmark
@author Martin Putniorz <mputniorz@gmail.com>
@version 0.0

@section DESCRIPTION

Generic benchmark fo XML DB in Python using cProfile
'''

import random
import string
import cProfile

LENGTH = 6

class TestSession(object):
    '''
    "Virtual" test class
    '''
    def __init__(self):
        pass
    def __del__(self):
        pass
    def write_test_small(self):
        pass
    def write_test_large(self):
        pass
    def read_test_small(self):
        pass
    def read_test_large(self):
        pass

def xml_string_generator(maximum, name):
    '''
    Generates well-formed XML string, elements are filled with
    random string
    
    @param maximum Number of elements
    @param name Root name
    @return XML string 
    '''
    elements = '<'+name+'>\n'
    for _ in xrange(maximum):
        content = ''.join(random.choice(string.ascii_uppercase)
                          for _ in range(LENGTH))
        elements += '\t<ele>' + content + '</ele>\n'
    elements += '</'+name+'>'
    return elements

def bench(session):
    '''
    Function profiles functions from passed session
    
    @param session TestSession instance
    '''
    print "Benchmark: Write small file into db"
    cProfile.runctx('session.write_test_small()', globals(), locals())
    print "Benchmark: Write large file into db"       
    cProfile.runctx('session.write_test_large()', globals(), locals())
    print "Benchmark: Read small file using xquery"       
    cProfile.runctx('session.read_test_small()', globals(), locals())
    print "Benchmark: Read large file using xquery"  
    cProfile.runctx('session.read_test_large()', globals(), locals())
    del(session) 