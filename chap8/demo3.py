# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/11/27 16:36

t = (10,[20,30],40)
print(t)
print(type(t))
print(t[0],type(t[0]),id(t[0]))
print(t[1],type(t[1]),id(t[1]))
print(t[2],type(t[1]),id(t[2]))

'''尝试将t1修改为100'''
#t[1] = 100 #元组不允许修改元素
print(t)
'''由于[20,30]是列表，所以可以向列表中添加元素，而列表的内存地址不变'''
t[1].append(100)
print(t,id(t[1]))