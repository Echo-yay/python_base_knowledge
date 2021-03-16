# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/3/16 17:47

#注意与上一个代码的区别（return和参数）
import time

def calc_time(fn):
    print('我是外部函数，被调用')
    print('fn=',fn)

    def inner(n):
        start = time.time()
        s = fn(n)
        end = time.time()
        return s,end-start

    return inner

@calc_time
# 1.调用calc_time
# 2.把被装饰的函数传给fn

def demo(n):
    x = 1
    for i in range(1,n):
        x += i
    return x
# 3.当再次调用demo函数时，此时的demo已经不是原来的demo
print('此时的demo为',demo)
m = demo(1000000)
print('m的值是:',m)