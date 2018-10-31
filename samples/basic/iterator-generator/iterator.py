# -*- coding: utf-8 -*-
# 迭代器是可以记录遍历位置的对象iter(). next()
'''
字符串、元组、列表都可以建立迭代器；
迭代器对象可以使用常规for语句进行遍历
'''
list = [1,2,3,4]
it = iter(list)
# 使用for循环遍历迭代器
for x in it:
  print(x)

# 使用next()来访问迭代器
import sys

list = [1,2,3,4]
it = iter(list)

while True:
  try:
    print(next(it))
  except StopIteration:
    sys.exit()
