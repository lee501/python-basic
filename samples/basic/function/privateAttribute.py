# -*- coding: utf-8 -*-
# python _、__和__xx__的区别
# _foo代表不能被直接访问的类属性
# __foo 双下划线表示类的私有属性
'''
# 1 print cls.__dict__
# 2 print ins1.__dict__

# ###########输出##########
# {'clsvar': 1, '__module__': '__main__', '__doc__': None, '__init__': <function __init__ at 0x101bbc398>} 类属性
# {'insvar': 2} 实例属性
# 一个实例对象的属性查找顺序是先查找自己的__dict__, 然后是它的类, 接着是父类
'''
class student(object):
  __name = 0
  _sex = 'male'
  def p(self):
    return self.__name
 
