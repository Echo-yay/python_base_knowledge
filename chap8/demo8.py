 # 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/11/28 16:02

'''集合的数学操作'''

# 交集
s1 = {1,2,3,4}
s2 = {1,2,5,6,8}
print(s1.intersection(s2))
print(s1 & s2)
print(s1)
print(s2)
print(
    '--------------'
)
# 并集
print(s1.union(s2))
print(s1 | s2)
print(s1)
print(s2)
print('-------------')

# 差集操作
print(s1.difference(s2))
print(s1-s2)
print(s2.difference(s1))
print(s2-s1)
print(s1)
print(s2)
print('------------------')

#对称差集
print(s1.symmetric_difference(s2))
print(s1^s2)
print(s1)
print(s2)
print('-----------------------')