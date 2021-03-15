# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/12/30 18:41

# 函数的返回值
def fun(num):
    odd = [] #奇数
    even = [] #偶数
    for i in num:
        if i%2 == 1:
            odd.append(i)
        else:
            even.append(i)
    return odd,even

lst = []
num = -1

while num != 0:
    num = int(input('请输入数字，输入0为止：'))
    if num != 0:
        lst.append(num)

print(fun(lst))

'''
函数的返回值
    1.如果没有返回值，即函数执行完毕后，不需要给调用处提供数据。return可以省略不写
    2.函数的返回值
        2.1如果是1个，直接返回类型
        2.2如果是多个，返回结果为元组
'''

#1
def fun1():
    print('hello')
    # return

#2.1
def fun2():
    return 'hello'

res = fun2()
print(res)

#2.2
def fun3():
    return 'hello','world'

res1 = fun3()
print(res1)