'''
参数类型：
  必须参数
  默认参数：默认参数必须是不可变对象，（city='beijing'）
    enroll(name, gender, age=6, city='Beijing')
  可变参数: （*params） 可变参数在函数调用时自动组装为一个tuple
                      如果传入的是1，2，3，4这样，* 使params接收到的是一个tuple
                      如果传入的是(1,2,3,4)或[1,2,3,4], *会展开tuple或list的元素， 将它变成可辨参数传入
  关键字参数: （**params）关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
  
  命名关键字参数：1 如果前边没有可变参数，使用*来限定关键字参数的名字 限制关键字参数的名字(name, sex, *, city, job)
               2  如果关键字参数前边有可变参数(name, sex, *num, city, job)
'''
# 默认参数/错误的例子
def add_end(L=[]):
    L.append('END')
    return L
'''
Python函数在定义的时候，默认参数L的值就被计算出来了，
即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，
如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了
'''
# 可变参数例子
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
calc(1,2,3,4)

# numbers = [1,2,3,4] 本身是一个数组
calc(nums[0], nums[1], nums[2]) #并不需要这么传递
*numbers 直接将list变成可变参数，即展开成nums[0]...


# 关键字参数

def person(name, sex, **kw):
  print('name: ', name, '性别: ', sex, 'other: ', kw)
# 传值方式 第一种以city=‘beijing’这种方式

person('lee', 'F', city='BeiJing') => name: Bob age: 35 other: {'city': 'Beijing'}
person('lee', 'F', city='BeiJing', job='programmer')
# 第二种以dict传值
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('anne', 'M', **extra)

---------------------
# 命名关键字参数
def person(name, age, *, city, job)
# 必须传入参数名
person(name, age, city='Beijing', job='hard')
# 命名关键字参数可以有默认值 def person(name, age, *, city'Beijing', job)
person(name, age, job='hard')

