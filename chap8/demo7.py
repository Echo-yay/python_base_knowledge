# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/11/28 15:48

'''集合之间的关系'''
#是否相等：元素相同即相等
s1 = {1,2,4,5}
s2 = {2,1,5,4}
print(s1 == s2)
print(s1 != s2)
print(s1.issubset(s2))
print(s2.issubset(s1))
print('-------------------------------')
# 是否为子集
s1 = {10,20,30,40,90,80}
s2 = {10,20,30,40}
s3 = {10,60}
s4 = {1,2,4,5}
s5 = {2,1,5,4}
print(s4.issubset(s5))
print(s5.issubset(s4))
print(s2.issubset(s1))
print(s3.issubset(s1))

print('--------------')
#是否为超集
s1 = {1,2,4,5}
s2 = {2,1,5,4}
s3 = {10,20,30,40,90,80}
s4 = {10,20,30,40}
s5 = {10,60}
print(s1.issuperset(s2))
print(s2.issuperset(s1))
print(s3.issuperset(s4))
print(s3.issuperset(s5))

print('-------------------------')
#是否有交集
s3 = {10,20,30,40,90,80}
s4 = {10,20,30,40}
print(s3.isdisjoint(s4)) #False，有交集为False