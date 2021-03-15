# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/1/12 16:57

#方法重写
class Person(object):   #Person类继承object类
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print('名字：{0}，年龄：{1}。'.format(self.name,self.age))

class Student(Person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)
        self.stu_no = stu_no

    def info(self):
        super().info()
        print('学号：{0}'.format(self.stu_no))

class Teacher(Person):
    def __init__(self,name,age,teach_year):
        super().__init__(name,age)
        self.teach_year = teach_year

    def info(self):
        super().info()
        print("教龄：{0}".format(self.teach_year))

stu = Student('Echo',18,'1001')
teacher = Teacher('Herny',45,10)
stu.info()
print('-----------------')
teacher.info()