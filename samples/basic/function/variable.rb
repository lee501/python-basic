# 全局变量和局部变量／
# 定义在函数内部的变量拥有局部作用域、只能在函数内部使用
# 定义在函数外部的变量全局作用域、在整个作用域中使用

total = 0

def sum(a, b):
  total = a + b
  print("函数体内部是局部值：", total)
  return total

sum(1, 2)
print(total)

'''
python的类变量和实例变量
参考js的对象、python中的__dict__属性、key: value
类和实例都有自己的__dict__属性
一个实例对象的属性查找顺序是先查找自己的__dict__, 然后是它的类, 接着是父类
_foo代表不能被直接访问的类属性
__foo 双下划线表示类的私有属性
'''
# 面向对象思想
class Test(object):
  # l类变量
  klass_variable = 1

  def __init__(self):
    # 实例变量
    self.instance_variable = 3

  def get(self):
    return self.klass_variable

test = Test()
print(Test.__dict__)
print("===========================")
print(test.__dict__)
print("实例变量: ", test.instance_variable)
print("类变量: ", Test.klass_variable)
print("实例访问类变量: ", test.klass_variable)
print("通过实例访问方法: ", test.get())

