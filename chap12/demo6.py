# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/1/12 15:04

#动态绑定属性和方法
class Student:
    def __init__(self,name,age):    #初始化方法
        self.name = name
        self.age = age

    def study(self):    #实力方法
        print(self.name+'在学习。 ')


#一个Student类可以创建多个实例对象，每个实例对象的属性值不同
stu1 = Student('Echo',18)   #Student类的实例对象，name指向"Echo"，age指向18.整个对象通过类指针指向Student类
stu2 = Student('Herny',19)  #Student类的实例对象

print(stu1)
print(id(stu1))
print(id(stu2))

print('-----------为stu1动态绑定“性别”属性----------')
stu1.gender = 'F'
print(stu1.name,stu1.age,stu1.gender)
print(stu2.name,stu2.age)

print('---------------------------')
stu1.study()
Student.study(stu1)
stu2.study()
Student.study(stu2)

def read():
    print('读书。')
stu1.read = read    #动态绑定方法
stu1.read()