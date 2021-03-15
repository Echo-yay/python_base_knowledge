# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/3/15 17:40

#sort()方法在原本的lst上进行排序，不创建新的对象
lst1 = [23,435,132,343,11,547]
lst1_new = lst1.sort()
print(lst1_new) #None
print(lst1) #[11, 23, 132, 343, 435, 547]

lst2 = [234,35,7,451,63]
lst2_new = sorted(lst2)
print(lst2_new) #[7, 35, 63, 234, 451]
print(lst2) #[234, 35, 7, 451, 63]

print('------------------------------')
#字典和字典之间不能使用比较运算
students = [
    {'name':'echo','age':18,'score':98},
    {'name':'john','age':14,'score':93},
    {'name':'henry','age':19,'score':90}
]
#字典之间不能使用比较运算
#students.sort()

def foo(ele):
    #print('ele = {}'.format(ele))
    return ele['age']   #通过返回值告诉sort方法，按照元素的哪个属性进行排序

#需要传递参数key指定比较规则
#key的参数类型是函数

#在sort内部实现时，调用了foo方法，并传入了一个参数，参数就是列表里的元素
students.sort(key=foo)
print(students)

print('-------------------------------')
students.sort(key=lambda ele:ele['score'])
print(students)