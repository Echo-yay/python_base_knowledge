# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/3/16 17:05

import time #time模块可以获取当前的时间
#运行前获取时间
start = time.time() #可以获取当前时间的时间戳
'''
时间戳：
从1970-01-01 00:00:00 UTC到现在的秒数
'''
print('start = ',start)
x = 0
for i in range(1,100000000):
    x += i  #19的阶乘
print(x)
end = time.time()
print('end = ',end)
print('运行时间：{}秒'.format(end-start))
#运行后再获取时间

start = time.time()
print('hello')
time.sleep(3)   #睡眠3s
print('world')
end = time.time()
print(end-start)

print('================通用与所有语言的最优化写法==================')

def calc_time(fn):
    start = time.time()
    fn()
    end = time.time()
    return end-start

def demo():
    x = 0
    for i in range(1, 100000000):
        x += i  # 19的阶乘
    print(x)

time = calc_time(demo)
print(time)

print('==============python装饰器的使用还可以更优化==============')