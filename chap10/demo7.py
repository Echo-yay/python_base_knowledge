# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/12/31 15:47

def fun(a,b,c):
    print('a=',a)
    print('b=',b)
    print('c=',c)

#函数的调用
fun(1,2,3)

print()

lst = [11 ,22 ,33]
fun(*lst) #在函数调用时，将列表中的每个元素都转换为位置实参传入

print()

tup = (111,222,333)
fun(*tup)

print()

fun(a=10 ,c=20 ,b=30) #函数调用，关键字实参

dic = {'a':100,'c':200,'b':300}
#fun(dic)
fun(*dic)
'''a= a
b= c
c= b'''
print()
fun(**dic) #在函数调用时，将字典中的所有键值对都转换为关键字实参传入