#!/usr/bin/python
#coding=utf-8
import time,sys

def debug_print(s):
    print (s)
def deal_error(e):
    timenow  = time.localtime()
    datenow  = time.strftime('%Y-%m-%d', timenow)
    logstr = '%s 发生错误: %s' %(datenow, e)
    debug_print(logstr)
    file.write(logstr)
    sys.exit()

def printsep():
    debug_print("================")
