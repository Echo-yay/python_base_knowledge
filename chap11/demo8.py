# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/1/10 14:28

try:
    a = int(input('输入第一个整数：'))
    b = int(input('输入第二个整数：'))
    res = a / b
except BaseException as e: #所有可能出现的情况BaseException取名为e
    print('出错了',e)
else:
    print('结果为：', res)
finally:
    print('谢谢您的使用。')