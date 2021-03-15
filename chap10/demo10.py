# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/12/31 16:31

def fun(n):
    if n==1:
        return 1
    else:
        res = n*fun(n-1)
        return res

n = int(input('请输入数字：'))
res = fun(n)
print('{0}的阶乘为：{1}'.format(n,res))