# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/11/28 16:12

'''列表生成式'''
lst = [i*i for i in range(6)]
print(lst)

'''字典生成式'''
fruits = ['apple','peach','orange']
prices = [20,10,30]
dict1 = {fruit.upper():price for fruit,price in zip(fruits,prices)}
print(dict1)

'''集合生成式'''
s1  = {i*i for i in range(6)}
print(s1)

'''没有元组生成式，因为元组是不可变序列'''