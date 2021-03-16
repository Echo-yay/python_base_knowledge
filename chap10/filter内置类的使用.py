# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/3/16 14:17

#filter 对可迭代对象进行过滤，得到的是filter对象,filter是可迭代对象
# python2是内置函数，3是内置类

#filter可以给定两个参数，第一个参数是函数，第二个是可迭代对象
ages = [12,23,30,17,16,22,19]
x = filter(lambda ele : ele > 18,ages)
#print(x)   #<filter object at 0x00000198845E48E0>
#for a in x:
#    print(a)

adult = list(x)
print(adult)    #[23, 30, 22, 19]