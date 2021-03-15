# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/11/27 15:51
'''元组的创建'''

'''第一种，直接创建'''
t1 = ('Echo','str',88)
print(t1,type(t1))

t3 = 'Echo',88 # 多个元素省略小括号
print(t3,type(t3))
t4 = (21,) # 只有一个元素时，使用逗号！！和小括号！！
print(t4,type(t4))

'''第二种，内置函数tuple()'''
t2 = tuple(('Echo','world',90))
print(t2,type(t2))

'''空元组的创建方式'''
#空列表
lst = []
lst = list()
#空字典
d = {}
d = dict()
#空元组
t = ()
t = tuple()
