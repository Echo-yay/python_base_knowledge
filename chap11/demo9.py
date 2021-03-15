# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/1/10 14:32

# 1.数学运算异常
#print(10/0) #ZeroDivisionError

lst = [11,22,33,44]
#print(lst[4]) #IndexError，索引从0开始

dict = {'name':'Echo','age':18}
#print(dict['gender']) #KeyError，映射中没有该键

#print(num) #NameError，未声明或初始化对象

#int a=20 #SyntaxError

a = int('hello') #ValueError，传入无效参数