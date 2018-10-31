# -*- coding: utf-8 -*-
'''
break 跳出for和while循环，终止循环对应的else也不执行
'''
for letter in "python":
  if letter == 'o':
    break
  print('当前字母： ', letter)

for n in range(2, 10):
  for x in range(2, n):
    if n % x == 0:
      print(n, '等于', x, '*', n//x)
      break
  else
    print(n, '质数')
