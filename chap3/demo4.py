# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/11/17 19:16
# 赋值运算符：从右往左
i = 1+3
print(i)

a=b=c=20    #链式赋值
print(a,id(a))
print(b,id(b))
print(c,id(c))  #a,b,c的id相同

#支持参数赋值
a = 20
a+=30
print(a)
a-=10
print(a)
a*=2
print(a)
a/=3
print(a)
a//=2
print(a)
a%=3
print(a)

# 支持解包赋值
a,b,c = 20,30,40
print(a,b,c)

# 交换两个变量的值
print(a,b)
a,b = b,a
print(a,b)