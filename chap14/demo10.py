# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/1/14 15:03

import sys
print(sys.getsizeof(24))    #占内存空间大小
print(sys.getsizeof(45))
print(sys.getsizeof(True))
print(sys.getsizeof(False))

import time
print(time.time())
print(time.localtime(time.time()))

import urllib.request   #urllib是一个包，有个模块是request
print(urllib.request.urlopen('http://www.baidu.com').read())    #读取百度返回的东西