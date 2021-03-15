# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/11/18 15:16

money = 1000 #余额
s = float(input("请输入取款金额：")) #取款金额
# 判断余额是否充足
if money >= s:
    money = money-s
    print("取款成功！当前余额为",money)
else:
    print("余额不足！")