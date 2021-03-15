# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/12/31 17:14

lst1=[11,22,33,44]
#print(lst1[4]) #list index out of range

lst2 = []
#lst2 = append[a,b,c]
lst2.append(('a','b','c')) #append是list的方法，所以要注意用法
lst2.append('d')
lst2.extend('e')
lst2.append([1,2,3,4])
lst2.append({'Echo':98})
print(lst2)