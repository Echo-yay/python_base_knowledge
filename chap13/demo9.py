# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/1/13 15:12

#特殊方法
a = 20
b = 100
c = a+b #两个v整数类型的对象的相加操作
d = a.__add__(b)

print(c)
print(d)

class Student:
    def __init__(self,name):
        self.name = name

    def __add__(self, other):
        return self.name+other.name

    def __len__(self):
        return len(self.name)


stu1 = Student('Echo')
stu2 = Student('Henry')

s = stu1+stu2   #实现了两个对象的加法运算
print(s)

s1 = stu1.__add__(stu2)
print(s1)
print('------------------------------')

lst = [11,22,33,44]
print(len(lst)) #len是内置函数len
print(lst.__len__())

print(len(stu2))