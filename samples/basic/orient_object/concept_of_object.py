'''
类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。

数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。

实例变量：定义在方法中的变量，只作用于当前实例的类。
继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
实例化：创建一个类的实例，类的具体对象。
方法：类中定义的函数。
对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法
'''
# 类对象
# 支持的两种操作：属性引用和实例化 Test.i, x = Test()  【x.i 类的实例化对象可以访问类变量， 但是方法无法访问类变量】
class Test():
  # 类变量(属性)
  i = 1
  # 方法
  def func(self):
    return 'hello python'

# 实例化
x = Test()
x.i #属性的引用，与js一样
x.func() #方法的引用
Test.i #类对象对属性的操作


'''
方法：使用def来创建，参数必须包括self， self代表类的实例
'''
# 定义类
class People:
  # 基本属性
  name = ''
  age = 0
  # 私有属性, 只能在类的内部访问
  __weight = 0
  # 构造方法
  def __init__(self, name, age, weight):
    self.name = name
    self.age = age
    self.__weight = weight
  #方法
  def speak(self):
    print("{} 的年纪是{}, 体重是{}".format(self.name, self.age, self.__weight)) 

# 继承
class man(People):
  grade = ''
  def __init__(self, na, age, w, grade):
    People.__init__(self, na, age, w)
    self.grade = grade
  #重写 
  def speak(self):
    





