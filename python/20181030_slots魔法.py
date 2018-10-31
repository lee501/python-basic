'''
Python不能在对象创建时直接分配一个固定量的内存来保存所有的属性
默认情况下Python用一个字典来保存一个对象的实例属性。这非常有用，因为它允许我们在运行时去设置任意的新属性

可以使用__slots__魔法指定固定集合的属性分配空间
'''
class MyClass(object):
  __slot__ = ['name', 'identifier']
  def __init__(self, name, identifier):
    self.name = name
    self.identifier = identifier
    self.set_up()

  def set_up():
    pass
