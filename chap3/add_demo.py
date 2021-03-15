# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/11/17 19:14
# 从键盘输入两个整数，在计算两个数的和
a = input('请输入数字a：')
b = input('请输入数字b：')

from decimal import Decimal
sum = Decimal(a)+Decimal(b)
print('结果是：'+str(sum))

c = input('乘数1：')
d = input('乘数2：')
res = int(c) * int(d)
print(res)