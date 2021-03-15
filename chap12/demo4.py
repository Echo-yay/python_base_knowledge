# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/1/11 17:20

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
stu1.study()    #对象名.方法名
print(stu1.name)
print(stu1.age)
print(stu1.native_place)

print('--------------')

Student.study(stu1)     #33行 == 26行，都是调用Student中的study方法
                        #类名.方法名(对象名)-->实际上是方法定义处的self