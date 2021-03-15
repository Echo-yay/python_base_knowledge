# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/12/29 15:27

# 字符串的劈分，劈分结果放在列表中
print('----------split()------------')
s = 'hello Python'
lst = s.split() #默认空格为分隔符
print(lst)
s1 = 'hello|python|Echo'
lst1 = s1.split(sep='|')
print(lst1)
lst2 = s1.split(sep='|',maxsplit=1)
print(lst2)

print('----------rsplit()-----------')
s = 'hello Python'
lst = s.rsplit() #默认空格为分隔符
print(lst) #['hello', 'Python']
s1 = 'hello|python|Echo'
lst1 = s1.rsplit(sep='|')
print(lst1)
lst2 = s1.rsplit(sep='|',maxsplit=1)
print(lst2) #['hello|python', 'Echo']

'''由此例子可知，左右劈分两种方法只有当指定最大劈分次数时结果才不同'''