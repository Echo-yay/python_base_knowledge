# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/12/31 15:54

def fun(a,b=10): #a，b均为实参，且b被赋值，所以b成为默认值参数
    print('a=',a)
    print('b=',b)


def fun2(*args): #个数可变的位置参数
    print(args)

def fun3(**args): #个数可变的关键字参数
    print(args)

def fun4(a,b,c,d):
    print('a=',a)
    print('b=',b)
    print('c=',c)
    print('d=',d)

fun2(20,30,40)
fun3(a=11,b=22,c=33)
print()
fun4(10,20,304,50) # 位置实参传入
fun4(a=20,b=40,c=80,d=50) #关键字实参传递
print()
fun4(11,22,c=20,d=30) # a,b位置实参传递，后两个关键字实参传递
print()

'''若c,d只能使用关键字实参传递，则需要在cd前加*
在*之后的形参只能通过关键字传递
'''

def fun5(a,b,*,c,d):
    print('a=', a)
    print('b=', b)
    print('c=', c)
    print('d=', d)

fun5(10,20,c=30,d=40)


'''函数定义时的形参的顺序问题'''
def fun5(a,b,*,c,d,**args):
    pass

def fun6(*args1,**args2):
    pass

def fun7(a,b=10,*args1,**args2):
    pass