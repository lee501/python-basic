'''
列表可以修改，而字符串和元组不能
'''
list.append(x) #把元素添加到列表的结尾
list.extend(L) #把L列表的元素扩展到列表
list.insert(i, x) #在索引i的位置插入x元素
list.remove(x) #移除值为x的第一个元素
list.pop([i]) #移除索引i的值，[]两边的方括号表示这个参数是可选的
list.clear() #清空列表
list.index(x) #元素x出现的第一个位置的索引值
list.count(x) #x出现的次数
list.sort() #排序
list.reverse() #倒排元素
list.copy()

# 列表作为堆栈来使用
# 堆栈的特点是先进后出
list.append(x) #添加元素
list.pop() #取出最后的元素

# 列表作为堆栈来使用， 通过引入collections的deque
from collections import deque

queue = deque(['first', 'second'])
queue.append('third')
queue.popleft() #=>first

# 列表推导式：返回结果是一个根据表达从其后的 for 和 if 上下文环境中生成出来的列表
vec = [2, 4, 6]
[3*x for x in vec if x > 3]
>>>[12, 18]
