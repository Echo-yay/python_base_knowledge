# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/12/31 17:05

for i in range(3):
    uname = input("请输入用户名：")
    pwd = input(('请输入密码：'))
    if uname == 'admin' and pwd == 'admin':
        print('登陆成功！')
        break
    elif i != 2:
        print('还有{0}次机会，请重新输入！'.format(2 - i))
    else:
        print('账号已锁定！')
