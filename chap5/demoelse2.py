# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/11/24 13:51

a = 0
while a<3:
    pwd = input("请输入密码:")
    if pwd == "ASD":
        print("输入正确！")
        break

    print("密码错误！请重新输入！")
    a = a+1
else:
    print("次数已达上限！该卡已锁定！")