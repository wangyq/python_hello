#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is a  demo 
"""
__author__ = 'yinqingwang@163.com'
__version__ = '0.10'
__license__ = 'MIT'

import datetime,time
 
sz = 5000000
 
def pong():
    v = yield
    while v >= 0:
        v2 = v + 1
        v = yield v2
    return
 
def ping(peer):
    cur_val = 0
    while cur_val <= sz:
        new_val = peer.send(cur_val)
        cur_val = new_val + 1
 
    print(cur_val)
 
 
n2 = pong()
t1 = datetime.datetime.now() 
n2.send(None)   # start it so it pauses on the first yield
 
#t1 = datetime.datetime.now()
ping(n2)
t2 = datetime.datetime.now() 
 
d = (t2-t1).microseconds /1000 
print("%d ms" %d)
