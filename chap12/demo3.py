# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/1/11 17:09

# 对象的创建（类的实例化）
class Student:
    native_place = '北京'

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def study(self):
        print('学习。')

    @staticmethod
    def method():
        print('静态方法。')

    @classmethod
    def cm(cls):
        print('类方法。')

def drink():
    print('喝水。')

#创建Student类的对象
stu1 = Student('Echo',20)
print(id(stu1))
print(type(stu1))
print(stu1)
print('-------------------')
print(id(Student))
print(type(Student))
print(Student)
