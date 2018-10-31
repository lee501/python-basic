# 检查列表中重复的数据
# 算法1
slist = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = []
for value in slist:
  if slist.count(value) > 1:
    if value not in duplicates:
      duplicates.append(value)

# 算法2
duplicates = set([x for x in slist if slist.count(x) > 1])

# 集合的交集和差集
set1 = set(['yellow', 'red', 'blue', 'green', 'black'])
set2 = set(['red', 'brown'])

set1.intersection(set2)

set1.difference(set2)


# python的三元运算符(条件表达式)
# condition_is_true if condition else condition_is_false
is_fat = True
state = "fat" if is_fat else "not fat"

# 使用元组的三元表达式, 原因是在Python中，True等于1，而False等于0，这就相当于在元组中使用0和1来选取数据。
# (if_test_is_false, if_test_is_true)[test]
fat = True
fitness = ("skin", "fat")[fat]
