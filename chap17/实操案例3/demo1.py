#encoding=utf-8
# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/1/28 14:59

#十进制，二进制，八进制，十六进制的转换
'''二进制bin()'''
def fun():
    num = int(input('请输入一个十进制的整数：'))
    print(num,'的二进制数为：',bin(num))   #使用了个数可变的位置参数
    print(str(num)+'的二进制数为：'+bin(num))  #'+'作为连接符，'+'的左右两侧必须为str
    print('%s的二进制数为：%s' % (num,bin(num)) )  #格式化字符串
    print('{0}的二进制数为：{1}'.format(num,bin(num))) #格式化字符串
    print(f'{num}的二进制数为：{bin(num)}')    #格式化字符串

    print('-------------------------------')
    '''八进制oct()'''
    print(f'{num}的八进制数为：{oct(num)}')
    print('{0}的八进制数为{1}'.format(num,oct(num)))
    print('%s的八进制数为：%s' % (num,oct(num)))

    print('-------------------------------')
    '''十六进制hex()'''
    print(f'{num}的十六进制数为：{hex(num)}')

if __name__ == '__main__':
    while True:
        try:
            fun()
            break
        except:
            print('请输入整数！请重新输入！')