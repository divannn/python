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

    @classmethod
    def class_method1(cls):
        print "Class method 1 called"
        print Clazz.static_member


def main():
    clazz = Clazz()
    print clazz.static_member + "     and...     " + Clazz.static_member
    print "Static methods" + "-" * 50
    Clazz.static_method1()#via class
    clazz.static_method2()#via instance

    print "Class methods" + "-" * 50
    Clazz.class_method1()#via class
    clazz.class_method1()#via instance


if __name__ == '__main__':
    main()