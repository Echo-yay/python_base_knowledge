# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/11/18 16:30
# range()的三种创建方式

'''1、只有一个参数'''
r = range(10) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]，默认步长为1
print(r) # range(0,10)
print(list(r)) # 查看range对象中的整数序列

'''2、有两个参数，start和stop，指定起始'''
r = range(1,10) # [1, 2, 3, 4, 5, 6, 7, 8, 9]，默认步长为1
print(list(r))

'''2、有三个参数，start、stop和step，指定起始和步长'''
r = range(1,10,2) # [1, 3, 5, 7, 9]
print(list(r))

# 判断元素是否在r中
print(10 in r) # False
print(9 in r) # True