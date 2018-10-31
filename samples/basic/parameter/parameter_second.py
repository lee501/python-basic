'''
strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。

python的参数传递：不可变对象是传值;  可变对象是传递引用，修改会改变原对象
'''

# 不可变对象
def changeInt(i):
  i = i + 1
  return i

b = 2
changeInt(b)

# 参数传可变对象
def changename(mylist):
  mylist.append([1,2,3,4])
  print('更改后的list：', mylist)
  return
mylist = [10,20,30]
changeme( mylist )
print ("函数外取值: ", mylist)
