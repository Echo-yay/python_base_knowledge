#encoding=utf-8
# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/1/31 17:13

#模拟QQ登录

while True:
    qq = input('请输入QQ号：')
    ans = input('请输入密码：')
    if qq == '12345' and ans == 'asd':
        print('登录成功！')
        break
    else:
        print('登录失败！请重新登录！')