# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/11/25 19:11

lst = [20,30,78,54,67,22,11]
print('before sort',lst,id(lst))


# 调用sort方法
lst.sort()
print('after sort',lst,id(lst))

lst.sort(reverse=True) #降序排列
print(lst)

lst.sort(reverse=False) #升序排列
print(lst)

print('使用内置函数sorted()，产生一个新的列表对象')
lst = [1,98,5,46,4,78,5,4]
print('before',lst,id(lst))
# 排序
new_lst = sorted(lst)
print('after',new_lst,id(new_lst))
# 降序
new_lst = sorted(lst,reverse=True)
print('降序',new_lst)