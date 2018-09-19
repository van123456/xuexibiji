#!/usr/bin/env python
# -*-coding:utf-8-*-
import operator

# list是什么鬼东西？
# list-序列 --就是每个元素都分配一个索引--来确定它的位置
# 元素可以有哪些,可以是整数
list = [1, 2, 3, 4]
print(list)
print(list[0])
# 序列里面的元素可以是序列
list = ['12', [0, '2']]
print(list[1])
# append 可以是序列
list.append([12, '12'])
print(list)
list = [1, '2']
# 元素可以是字符串
print(type(list[1]))
# 序列可以直接实例化调用
tttt = []
list.append(5)
list.append('3')
# 序列的倒叙排列
list.reverse()
print(list)
# 序列的插入，插入的位置(索引)，元素
list.insert(3, '2')
print(list)
# 计算某个元素出现的频率
print(list.count('2'))
# 不可以索引超出list，序列范围的元素
print(list.count(list[0]))
print(list.count(99))
list1 = [1, '']
print(list1)
# 比较2个列表是不是一致
print(operator.eq(list, list1))
operator.add(list, list1)
print(list)
print("序列%s" % list)
# 遍历序列
for n in list:
    print(n)
