# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/11/28 15:19

'''集合的创建方式'''

# 第一种
s1 = {'Python','String',90,90,'Python'}
print(s1,type(s1))

#第二种
s2 = set(range(6))
print(s2,type(s2))

# 第三种
s3 = set([1,2,3,4,5,6,7,4,2]) #去掉重复元素
print(s3,type(s3)) #{1, 2, 3, 4, 5, 6, 7} <class 'set'>

# 第四种
s4 = set((1,2,3,6,32,12,2,1,3)) #去掉重复元素，集合中的元素是无序的
print(s4,type(s4)) #{32, 1, 2, 3, 6, 12} <class 'set'>

# 第五种
s5 = set('python')
print(s5,type(s5)) #{'h', 'p', 'y', 't', 'n', 'o'} <class 'set'>

# 定义空集合
s6 = {} #类型为字典，不可
s7 = set() #可