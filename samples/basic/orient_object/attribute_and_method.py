# 类的私有属性
# __private_attr: 双下划线开头，不能在类外部使用, 在类的方法内使用self.__private_attr
# 私有方法 __private_method, 只能在类内部方法中使用self.__private_method

class ClassName(object):
  """docstring for ClassName"""
  def __init__(self, arg):
    super(ClassName, self).__init__()
    self.arg = arg

class ClassName(object):
  __private_attr = 0
  public_attr = 1
  def function(self):
    self.__secretCount += 1
    self.publicCount += 1
    print (self.__secretCount)

# 私有方法
class Site():
  # 构造方法
  def __init__(self, name, url):
    self.name = name
    self.__url = url. #私有
  # 私有方法
  def __foo(self):
    print("this is private method, only access in method under class")

  def who(self):
    print("name is %s" % self.name)
    print("url is {}".format(self.__url))
  def foo(self):
    print("共用法法调用私有方法")
    self.__foo()
