'''
使用yield的函数是生成器
调用生成器的时候，每次遇到yield，会暂停保存当前所有信息，并返回yield的值， 再次执行next()的时候，从yield的位置继续
调用一个生成器函数， 返回的是迭代器对象 
'''

import sys

def fibonacci(n):
  a, b, counter = 0, 1, 0
  while True:
    if counter > n:
      return
    yield a
    a, b = b, a + b
    counter += 1
fib = fibonacci(10) #fib是一个迭代器对象

while True:
  try:
    print(next(fib))
  except StopIteration:
    sys.exit()
  