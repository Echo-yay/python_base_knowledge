# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/11/17 19:17
a,b = 20,30
print('a>b吗？',a>b)
print('a<b吗？',a<b)
print('a<=b吗？',a<=b)
print('a>=b吗？',a>=b)
print('a==b吗？',a==b)
print('a!=b吗？',a!=b)

'''=为赋值运算符，==为比较运算符
    一个变量由标识，类型和值构成
    ==比较的是value
    is是比较对象'''

a = 10
b = 10
print(a==b)     #True
print(a is b)   #True
'''说明a与b的id和value都相同'''
print(a is not b)

print("---------------list-------------------")
list1 = [11,22,33,44]
list2 = [11,22,33,44]
print(list1 == list2)
print(list1 is list2)
print(id(list1),id(list2))
print(list1 is not  list2)