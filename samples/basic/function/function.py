# -*- coding: utf-8 -*-
'''
函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()。
函数内容以冒号起始，并且缩进。
return [表达式] 结束函数，选择性地返回一个值给调用方。
不带表达式的return相当于返回 None。
'''
import re

def add(a, b):
  if re.match(r'-?[1-9]\d*$', a) and re.match(r'-?[1-9]\d*$', b):
    return int(a) + int(b)
  else:
    return a + b
m = add("1", "2")
print(m)

s = add("a", "b")
print(s)
