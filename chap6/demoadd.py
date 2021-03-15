# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/11/24 15:25

#向列表的末尾添加一个元素
lst = [1,2,3]
print('添加之前',lst)
print(id(lst))
lst.append(4)
print('添加之后',lst)
print(id(lst))

lst2 = ['hello','world']
lst.append(lst2) #将lst2作为一个元素加入
print(lst)
lst.extend(lst2) #添加多个
print(lst)

# 在任意位置添加一个元素
lst.insert(1,80)
print(lst)

# 在列表中的任意位置添加至少一个元素
lst3 = [True,False,'hello']
lst[1:]=lst3
print(lst)