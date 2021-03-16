# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/3/16 16:23

#1.一个函数作为另一个函数的返回值（lambda）
#2.一个函数作为另一个函数的参数
#3.函数内部再定义一个函数

def foo():
    print('foo被调用')

    return 'foo'

def bar():
    print('bar被调用了')
    return foo()

x = bar()
print('x的值是{}'.format(x))

print('-------------------------------')

def foo_2():
    print('foo被调用')

    return 'foo'

def bar_2():
    print('bar被调用了')
    return foo_2

y = bar_2() #y是foo_2()的别名
print('y的值是{}'.format(y))
y()
print('-------------------------')
z = bar_2()()
print(z)

print('----------------------------------------')
def outer():
    m = 100

    def inner():
        n = 90
        print('我是inner函数')

    print('我是outer函数')

outer() #我是outer函数

print('-----------------------------------------------')
def outer_2():
    m = 100

    def inner_2():
        n = 90
        print('我是inner函数')

    print('我是outer函数')
    return inner_2

outer_2()()