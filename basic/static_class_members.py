#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'ivan'

class Clazz:
    static_member = "I'm static member"

    def __init__(self):
        print 'Born!'

    @staticmethod
    def static_method1():
        print "Static method 1 called"
        print Clazz.static_member

    def static_method2():
        print "Static method 2 called"
        print Clazz.static_member

    static_method2 = staticmethod(static_method2)

def main():
    clazz = Clazz()
    print clazz.static_member + "     and...     " + Clazz.static_member

    Clazz.static_method1()
    Clazz.static_method2()

if __name__ == '__main__':
	main()