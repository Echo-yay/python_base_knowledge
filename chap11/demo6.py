# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/1/10 14:22
try:
    a = int(input('输入第一个整数：'))
    b = int(input('输入第二个整数：'))
    res = a / b
    print('结果为：', res)
except ZeroDivisionError:
    print('除数不可为0')

except ValueError:
    print('只能输入数字串！')

print('程序结束！')