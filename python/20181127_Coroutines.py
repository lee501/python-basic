'''
协程和生成器区别：
  生成器是数据的生产者
  协程师数据的消费者

  生成器减少内存的压力，值是动态生成的，而不是存在一个列表中
'''

# 创建一个生成器
def fib(n):
  a, b = 0, 1
  while b < n:
    yield a
    a, b = b, a + b

for i in fib(n):
  print(i)

# 协程

def grep(pattern):
  print("Searching for {0}".format(pattern))
  while True:
    line = yield
    if pattern in line:
      print(line)

# 启动协程，使用next()方法
pattern = grep('test')
next(pattern)

# 外部传值给协程,通过yield来接收
pattern.send('hello')
pattern.send('this is test') #=> this is test

# 通过close()来关闭协程
pattern.close()
