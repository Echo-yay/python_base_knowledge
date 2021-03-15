# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/12/31 16:40

#斐波那契数列，输出第n位

def fun(n):
    if n==1 or n==2:
        return 1
    else:
        res = fun(n-1) + fun(n-2)
        return res

n = int(input("请输入所求项数："))
res = fun(n)
print('斐波那契数第{0}项为{1}'.format(n,res))

print('----------------------------------')

# 输出前n位
lst = []
for i in range(1,n+1):
    s = fun(i)
    lst.append(s) #lst=lst.append(s)报错，因为append会修改lst本身，并且返回None。不能把返回值再赋值给lst

print('斐波那契数前{0}项为{1}'.format(n,lst))