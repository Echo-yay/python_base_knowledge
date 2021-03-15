# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/11/17 19:10
n1 = 1.1
n2 = 2.2
print(n1 + n2)

# 解决运算不准确的方法
from decimal import Decimal
n = Decimal('1.1')+Decimal('2.2')
print(n,type(n))