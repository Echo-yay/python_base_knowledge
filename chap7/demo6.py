# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/11/25 20:29

# 字典的特点
dict1 = {'Echo':100,'Echo':98} #key不允许重复
print(dict1)

dict2 = {'first':'Echo','second':'Echo'}
print(dict2)

# key是不可变对象，列表是可变对象
lst = [1,2,3,4]
lst.insert(1,20)
print(lst)
#dict3 = {lst:200} #TypeError: unhashable type: 'list'

str = 'Hello' #说明字符串是不可变对象
dict4 = {str:2}
print(dict4)