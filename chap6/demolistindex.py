# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/11/24 14:54

lst = list(['hello','echo',23,'hello'])
print(lst.index('hello')) #有重复元素时，只返回第一个元素的索引
#print(lst.index('python')) #不存在的元素的索引
print(lst.index('hello',1,4)) #在指定范围内查找元素的索引，查前不查后