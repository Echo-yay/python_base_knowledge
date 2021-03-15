# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/1/11 17:29

#类属性，静态方法，静态方法的使用
class Student:
    native_place = '北京' #直接写在类里的变量称为类属性

    #初始化方法
    def __init__(self,name,age):
        self.name = name    #self.name称为实体属性，进行一个赋值操作，将局部变量name的值赋给实体属性
        self.age = age

    #实例方法
    def study(self):
        print('学习。')

    #静态方法
    @staticmethod
    def method():   #()中没有self
        print('使用staticmethod进行修饰，所以是静态方法。')

    #类方法
    @classmethod
    def cm(cls):
        print('使用classmethod进行修饰，所以是类方法。')

#在类之外定义的称为函数，在类之内定义的称为方法

#函数
def drink():
    print('喝水。')

#类属性的使用方式
print(Student.native_place)
stu1 = Student('Echo',20)
stu2 = Student('Henry',19)
print(stu1.native_place)
print(stu2.native_place)
print()
Student.native_place = '上海'
print(stu1.native_place)
print(stu2.native_place)
print()
stu2.native_place = '天津'
print(stu2.native_place)
print('--------------类方法的使用方式---------------')
Student.cm()
print('--------------静态方法的使用方式---------------')
Student.method()