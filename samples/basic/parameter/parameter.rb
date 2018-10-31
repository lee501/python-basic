# -*- coding: utf-8 -*-
# 不可变参数（值传递）整数、字符串、元组
def changeInt(a):
  a = 10
  return a
b = 5
changeInt(b)
print(b)

# 可变参数（引用传递） list、字典
def changelist(mylist):
  mylist.append([1,2,3,4])
  print("函数内的值：", mylist)

test = [5,6,7]
changelist(test)
print(test)


# python的参数分为四种：位置参数、缺省参数（参数设置默认值）、
#                   可选参数（前面加*）：在函数调用的时候自动封装成tuple或list
#                   关键字参数（**）：封装成字典dict

# lambda 来创建匿名函数
sum = lambda a, b: a + b
