# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/3/16 14:27

from functools import reduce

#reduce以前是一个内置函数
#内置函数和内置类都在builtin.py文件里
scores = [100,89,76,87]
print(reduce(lambda ele1,ele2 : ele1 + ele2,scores))    #352

#求总成绩
students = [
    {'name':'echo','age':18,'score':98},
    {'name':'henry','age':19,'score':97},
    {'name':'john','age':20,'score':96},
]

#def bar(x,y):
#    return x+y['score']
#初始化的值为0：   x = 0
#               y = {'name':'echo','age':18,'score':98}
#若不指定初始化的值： x={'name':'echo','age':18,'score':98}
#                 y={'name':'henry','age':19,'score':97}
#print(reduce(bar,students,0))

#或者写成
print(reduce(lambda x,y:x+y['score'],students,0))