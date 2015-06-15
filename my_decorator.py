#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is a crawl demo
"""
__author__ = 'yinqingwang@163.com'
__version__ = '0.10'
__license__ = 'MIT'

import functools


def mylog(msg=None,*arg):
    #def inner(fn):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args,**kw):
            print "begin call : %s" % fn.__name__
            res = fn(*args,**kw)
            print "end call : %s " % fn.__name__
            return res
        return wrapper
    #return inner
    return decorator

@mylog()
def myadd(x,y):
    return x*x + y*y

print myadd(3,4)
