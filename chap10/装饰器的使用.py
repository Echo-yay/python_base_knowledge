# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/3/16 17:35

import time

def calc_time(fn):
    print('我是外部函数，被调用')
    print('fn=',fn)
    def inner():
        start = time.time()
        fn()
        end = time.time()
        print('代码耗时:',end-start)

    return inner

@calc_time
# 1.调用calc_time
# 2.把被装饰的函数传给fn
def demo():
    x = 1
    for i in range(1,1000000):
        x += i
    print(x)
# 3.当再次调用demo函数时，此时的demo已经不是原来的demo
print('此时的demo为',demo)
demo()