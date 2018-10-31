# 可迭代对象Iterable  __iter__()
# 迭代器 __next__()
def fibon(n):
  a = b = 1
  for i in range(n):
    yield a
    a, b = b, a + b

for x in fibon(1000):
  print(x)
