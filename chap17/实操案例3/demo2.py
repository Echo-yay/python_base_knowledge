#encoding=utf-8
# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/1/28 15:30

#为手机充值
def fun():
    money_old = 8
    print('原有话费金额：\033[0;34m8元\033[m')
    money = float(input('请输入充值金额：'))
    money_new = money_old+money
    print('当前可用金额为：%s' % (money_new))

if __name__ == '__main__':
    while True:
        try:
            fun()
            break
        except:
            print('请输入数字！')

