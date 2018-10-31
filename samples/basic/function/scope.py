'''
python的作用域：只有module class def lambada会引入新的作用域
作用域的查找根js的查找方式一样
访问： 局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问
修改：内部作用域修改外部作用域变量，用到global和nonlocal关键字
'''
# 修改全局变量
num = 1
def change():
  global num
  print(num)
  num = 2
  print(num)

# 修改嵌套作用域的变量使用nonlocal
def outer():
  num = 'outer'
  def inner():
    nonlocal num
    num = 'inner'
    print(num)
  inner()
  print(num)

def outer():
  num = 'outer'
  def inner():
    print(num)
  inner()


# 访问外部作用域
a = 10
def test():
    m = a + 1
    print(m)
test()