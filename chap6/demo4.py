# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/11/24 15:19

print('p'in 'python') # True
print('K'in 'python') #False

lst = [10,20,'Python','echo']
print(10 in lst)
print(100 in lst)
print(10 not in lst)
print(100 not in lst)

#列表元素的遍历
for i in lst:
    print(i,end='\t')