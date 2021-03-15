# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/11/18 16:09

'''从键盘中录入两个数并比较大小'''
a = float(input('请输入第一个数字：'))
b = float(input('请输入第二个数字：'))

'''if a>=b:
    print(a,'>=',b)
else:
    print(a,'<',b)'''

print('使用条件表达式比较')
print(a,'>=',b)  if a>=b else print(str(a)+'<'+str(b))