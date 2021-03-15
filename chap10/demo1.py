# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/12/29 17:48

#函数的创建和调用

def calc(a,b): # a,b形参，在函数的定义处
    c = a+b
    return c

result1 = calc(1,2) #1，2实参，在函数调用处
print(result1)

result2 = calc(b=10,a=20) #关键字参数
print(result2)