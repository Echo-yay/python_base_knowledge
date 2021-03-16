# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/3/16 16:54

#闭包 = 函数块+引用环境
def outer():
    x = 10  #在外部函数中定义了局部变量
    def innner():
        return x+1 #内部函数对局部变量操作

    return innner

print('-----------------------')

def outer_2():
    x = 10  #在外部函数中定义了局部变量
    def innner_2():
        #在内部函数如何修改外部函数的局部变量
        nonlocal x  #此时这里的x不再是新增变量，而是外部的局部变量x
        y= x+1 #内部函数对局部变量操作
        print('inner中的y={}'.format(y))
        x = 20  #不是修改外部的x变量，而是在inner函数内部声明一个x变量

    return innner_2

outer_2()()   #inner中的y=11