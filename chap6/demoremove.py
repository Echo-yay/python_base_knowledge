# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/11/25 18:53

lst=[10,20,30,40,50,60,30]
lst.remove(30) #从列表中移除一个元素，重复元素存在则只移除第一个
print(lst)

# 根据索引移除元素，若索引不存在则抛出异常
lst.pop(1)
print(lst)
lst.pop() #不写索引移除最后一个元素
print(lst)

#切片操作，删除至少一个元素,将产生一个新的列表对象
new_lst=lst[1:3]
print('原列表',lst,id(lst))
print('新列表',new_lst,id(new_lst))
'''不产生新的列表对象，而删除原列表中的内容'''
print(lst)
lst[1:3]=[] #将原列表中的片段替代
print(lst)

'''清除列表中的所有元素'''
lst.clear()
print(lst)

'''del语句将列表对象删除'''
del lst
#print(lst) #NameError: name 'lst' is not defined