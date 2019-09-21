# -*- coding: utf-8 -*-
# 多线程编程
'''
 使用全局解释器锁GIL确保只有一个线程在解释器中运行
'''
from time import sleep, ctime

def loop0():
  print("start loop 0 at {}".format(ctime()))
  sleep(4)
  print("stop loop 0 at {}".format(ctime()))

def loop1():
  print("start loop 1 at {}".format(ctime()))
  sleep(2)
  print("stop loop 1 at {}".format(ctime()))

def main():
  print("startn at {}".format(ctime()))
  loop0()
  loop1()
  print("all done at {}".format(ctime()))

if __name__ == '__main__':
  main()
