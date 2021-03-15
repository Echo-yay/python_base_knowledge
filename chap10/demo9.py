# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/12/31 16:11

def fun(a,b):
    c=a+b # c：局部变量，因为c是在函数体内进行定义的变量，作用域为函数体内。a,b为函数的形参，作用范围也是函数内部，相当于局部变量
    print(c)

'''由于a,c超出了起作用的范围，所以以下两个句子报错'''
#print(c)
#print(a)

name = 'Echo' #作用范围为全体，全局变量
print(name)
def fun2():
    print(name)
fun2()



def fun3():
    global age #局部变量使用global声明，就变成了全局变量
    age = 20
    print(age)
fun3()
print(age)