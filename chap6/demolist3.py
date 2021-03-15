# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/11/24 15:08

lst=[1,2,3,4,5,6,7,8,9]
#start为1，stop为6，step为1
print(lst[1:6:1])
print('原列表',id(lst))
lst2 = lst[1:6:1]
print('切片',id(lst2))
#lst = [1,1,1,1,1,1]
#print(lst2) # 切出的片段为新的列表对象

# start为1，stop为6，step为2
lst3 = lst[1:6:2]
print(lst3)

# 省略start
print(lst[:6:2])

# 省略stop
print(lst[2::1])

print('----------步长为负数----------')
print(lst[::-1])

#start=7,stop省略，step=-1
print(lst[7::-1])
print(lst[7:8:-1])