# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/11/23 20:51

for item in 'Python':
    print(item)

#range可产生一个整数序列，也是可迭代对象
for i in range(10):
    print(i)

# 如果在循环体中不需要使用到自定义变量，可将自定义变量写为“_”
for _ in range(5):
    print('岁月漫长，值得等待~')



print('——————使用for循环计算从1到100的偶数和——————')

sum = 0 #用于存储偶数和
for i in range(2,101,2):
    sum = sum+i
print(sum)