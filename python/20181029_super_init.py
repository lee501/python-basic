# Python中子类调用父类的方法有两种方法能够实现：调用父类构造方法，或者使用super函数
class A(object):
  def __init__(self, name, gender):
    self.nameA = "A"
    self.name = name
    self.gender = gender
  def a_func(self):
    print("function a: {0}".format(self.nameA))


class B(A):
  def __init__(self, name, gender, age)
    super(B, self).__init__(name, gender)
    self.nameB = "B"
    self.name = name.upper()
    self.age = age + 1

  def b_func(self):
    pass

b = B("lee", "boy", 22)
b.nameA
b.nameB
b.name
b.gender
b.age
