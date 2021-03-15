# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/11/28 15:31

'''集合的相关操作'''
# 判断元素是否存在
s = {1,2,3,4,5,6,}
print(1 in s)
print(10 in s)
print(1 not in s)
print(10 not in s)

# 新增元素
print(s)
s.add(8)    #只能加一个元素
print(s)
s.update([30,40]) #[]里放列表
print(s)    #将列表中的元素分开放入集合中
s.update((1,2,4,322,567)) #
print(s)
s.update({43,668,231}) #
print(s)
s.update({'www':12,'piu':343})  #只把键放入集合中
print(s)
print('-----------删除-------------')
s.remove(322)
print(s)
#s.remove(999) # 元素不存在 ，KeyError: 999
#print(s)
s.discard(1)
print(s)
s.discard(999) #元素不存在，不抛异常
print(s)
s.pop() #随机删
print(s)
s.pop() #随机删
print(s)
#s.pop(322) #TypeError: pop() takes no arguments
#print(s)
s.clear() #清空
print(s)