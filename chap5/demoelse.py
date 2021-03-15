# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/11/24 13:47

# for与else连用
for i in range(3):
    pwd = input("请输入密码：")
    if pwd == "ASD":
        print("密码正确！")
        break
    else:
        print("请重新输入！")
else:
    print("次数已达上限！该卡已锁定！")