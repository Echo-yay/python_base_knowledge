#encoding=utf-8
# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/1/28 15:45

#计算消耗的能量
def fun():
    num = int(input('请输入当天行走的步数：'))
    cal = num*28
    print(f'今天消耗了{cal}卡卡路里，即{cal/1000}千卡。')
if __name__ == '__main__':
    while True:
        try:
            fun()
            break
        except:
            print('输入错误，请重新输入数字！')