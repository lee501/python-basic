# -*- coding: UTF-8 -*-
# for 循环可以遍历列表、字符串
for letter in "Python":
  print("当前字母：", letter)

# 使用索引
fruits = ['runoob', 786 , 2.23, 'john', 70.2 ]
for index in range(len(fruits)):
  print(fruits[index])

# for .. else else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行，while … else 也是一样。
for num in range(10, 20):
  for i in range(2, num):
    if num % i == 0:
      j = num / i
      print("%d 等于 %d * %d ", % (num, i, j))
      break
  else:
   print(num, "zhishu")    
