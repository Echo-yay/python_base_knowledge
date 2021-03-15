# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/11/27 15:51

'''不可变序列，可变序列'''
'''可变序列，列表、字典'''
lst = [1,2,3,4]
print('lst:',id(lst))
lst.append(5)
print('lst-after:',id(lst))

'''不可变序列，元组、字符串'''
str = 'asd'
print('str:',id(str))
str = 'sdf'
print('after-str:',id(str))