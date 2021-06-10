"""
关于字典dict的一些操作

Version: 0.1
Author: yomi
Date: 2021-04-08
"""

# 创建字典的字面量语法
scores = {'yomi': 95, 'john': 78, 'susan': 83}
print(scores)
# 创建字典的构造器语法
items1 = dict(one=1, two=2, three=3, four=4)
# 通过zip函数将两个序列压成字典
items2 = dict(zip(['a', 'b', 'c'], '123'))
# 创建字典的推导式语法
items3 = {num: num ** 2 for num in range(1, 10)}
print(items1, items2, items3)
# 通过键可以获取字典中的值
print(scores['yomi'])
print(scores['john'])
# 对字典中所有键值对进行遍历
for key in scores:
    print(f'{key}: {scores[key]}')
# 更新字典中的元素
scores['john'] = 65
scores['joe'] = 34
scores.update(jobs=45, cook=54)
print(scores)
if 'candy' in scores:
    print(scores['candy'])
print(scores.get('candy')) # get方法也是通过键获取对应的值，但可以设置默认值
print(scores.get('candy', 60))
# 删除字典中的元素
print(scores.popitem())
print(scores.popitem())
print(scores.pop('yomi', 100)) # pop方法也能设置默认值，如要删除的键不在字典里，则返回默认值
# 清空字典
scores.clear()
print(scores)
