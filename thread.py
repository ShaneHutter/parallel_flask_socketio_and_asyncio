#!/usr/bin/env python3
"""Run two blocking commands asyncronously"""

from concurrent.futures import thread
from threading import Thread
from time import sleep

def foo():
    print( "foo" )
    sleep( 10 )
    print( "FOO" )

def bar():
    print( "bar" )
    sleep( 5 )
    print( "BAR" )

if __name__ == '__main__':
    thread_foo = Thread( target = foo )
    thread_bar = Thread( target = bar )
    thread_foo.start()
    thread_bar.start()