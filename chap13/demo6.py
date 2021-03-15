# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/1/12 17:03

#object类
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return '我的名字是{0}，今年{1}岁。'.format(self.name,self.age)

stu = Student('Echo',20)
print(dir(stu)) #查看stu的属性和方法
print(stu)  #默认调用__str__()方法
print(type(stu))