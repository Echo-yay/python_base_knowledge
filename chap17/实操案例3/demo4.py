#encoding=utf-8
# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/1/28 15:52

# 预测子女身高
def fun():
    father_height = float(input('请输入父亲的身高：'))
    mother_height = float(input('请输入母亲的身高：'))
    son_height = (father_height+mother_height)*0.54
    print('预测子女的身高为：{:0.2f}cm。'.format(son_height))
if __name__ == '__main__':
    while True:
        try:
            fun()
            break
        except:
            print('请输入正确的数字！')