# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/11/18 15:48
'''
会员      大于等于200     8折
         大于等于100     9折
         小于100        不打折

非会员    大于等于200     9.5折
         小于200        不打折
'''

answer = input('您是会员吗？')
money = float((input('请输入消费金额：')))
if answer == 'y': #会员
    print('会员')
    if money >= 200:
        cost = 0.8*money
        print("打8折，此次消费", cost, '元。')
    elif 100<= money <200:
        cost = 0.9*money
        print("打9折，此次消费", cost, '元。')
    elif 0<= money <100:
        print("不打折，此次消费", money, '元。')
    else:
        print("输入金额有错！")

else: # 非会员
    print('非会员')
    if money >= 200:
        cost = 0.95*money
        print("打95折，此次消费", cost, '元。')
    elif 0<= money <200:
        print("不打折，此次消费", money, '元。')
    else:
        print("输入金额有错！")

#print("此次消费",cost,'元。')