# 集合是一个无序没有重复的集合
# 创建一个空集合要使用set()
# 基本功能包括关系测试和消除重复元素。
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)                      # 删除重复的
{'orange', 'banana', 'pear', 'apple'}
>>> 'orange' in basket                 # 检测成员
True
>>> 'crabgrass' in basket
False
