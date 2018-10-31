# py使用lambda来创建匿名函数
# 匿名函数只是一个表达式，不用写return，返回值就是该表达式的结果

# 将匿名函数赋值给变量
f = lambda x: x * x

# 将匿名函数返回值作为return
def biuld(x, y):
  return lambda: x + y
 