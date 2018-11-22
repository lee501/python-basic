#推导式从一个数据序列构建到另一个新的数据序列的结构体

# list推导式
'''
语法： variable = [表达式 for 表达式 in input_list if 表达式条件]
'''
multiples = [i for i in range(30) if i % 3 is 0]

squared = []
for x in range(10):
  squared.append(x**2)
# 使用列表推导式来处理
squared = [x**2 for x in range(10)]


# dict推导式
'''
语法：[表达式 for 表达式 in input_dict if 表达式条件]
'''
mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}

mcase_frequency = { k.lower(): mcase.get(k.lower, 0) + mcase.get(k.upper(), 0) for k in mcase.keys()}

# 快速对换字典的键和值
{v: k for k, v in my_dict.items()}


# 集合推导式
'''
与list推导式类似， 区别使用的是{ }
'''
squ = {x**2 for x in [1,2,3]}
