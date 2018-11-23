# lambda表达式在python中为匿名函数
'''
语法 lambda 参数: 操作(参数)
'''
add = lambda x, y: x + y

add(3,5)


# 列表排序
a = [(1, 2), (4, 1), (9, 10), (13, -3)]
a.sort(key=lambda x: x[1])
