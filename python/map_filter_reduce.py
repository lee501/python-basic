# map 将一个函数映射到一个输入列表的所有元素上
# map(function, list)

items = [1,2,3,4]
squared = []
for i in items:
  squared,append(i**2)

# 使用map来处理
items = [1,2,3,4,5]
squared = list(map(lambda x: x**2, items))

# 列表的函数
def multiply(x):
  return(x*x)
def add(x):
  return(x+x)

funcs = [multiply, add]

for i in range(5):
  value = map(lambda x: x(i), funcs)
  print(list(value))


'''
filter 过滤列表的元素
'''
numbers = range(-5, 5)
less_than_zero = filter(lambda x: x < 0, numbers)
print(list(less_than_zero))


'''
reduce 对列表进行计算返回结果
'''
from functools import reduce
product = reduce(lambda x, y: x * y, [1, 2, 3])