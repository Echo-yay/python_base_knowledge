#lambda()匿名函数

def add(a,b):
    return a+b
print('0x%X' % id(add))

x = add(4,5)    #函数名（实参）
print(x)

fn = add    #给add起别名
print(fn)
print(fn(1,2))
print('0x%X' % id(add))

#除了使用def关键字定义一个函数外，我们还能使用lambda表达式定义一个函数
#匿名函数，用来表达简单的函数，调用次数很少
#调用匿名函数的两种方式：
#1.定义一个名字(很少使用)
mul = lambda a,b:a+b
print(mul(1,2))
print('-------------------------------')
#2.把该函数当作参数传给另一个函数（回调）
def calc(a,b,fn):
    c = fn(a,b)
    return c

def add(m,n):
    return m+n

def minus(m,n):
    return m-n

x1 = print(calc(1,2,add))   #a = 1,b = 2,fn = add
x2 = print(calc(5,3,minus)) #a = 5,b = 3,fn = minus

x3 = calc(1,2,lambda x,y:x+y)
print(x3)