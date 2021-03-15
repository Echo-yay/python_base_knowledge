# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/1/13 15:22


#特殊方法__init__()与__new__()，非常重要
class Person(object):

    def __new__(cls, *args, **kwargs):
        print('__new__被调用执行了，cls的id值为{0}'.format(id(cls)))
        obj = super().__new__(cls)  #创建obj
        print('创建的对象的id为：{0}'.format(id(obj)))
        return obj  #将创建的对象赋值给self，转到line14

    def __init__(self,name,age):    #初始化方法执行结束，再将self赋值给p到line24
        print('__init__方法被调用了，self的id为：{0}'.format(id(self)))
        self.name = name
        self.age = age

print('object这个类对象的id为：{0}'.format(id(object)))
print('Person这个类对象的id为：{0}'.format(id(Person)))
print('----------------------------------------------')

#创建Person类的实例对象
p = Person('Echo',19)   #创建对象时，将Person传到cls，转到line8
print('p这个Person类的实例对象的id为：{0}'.format(id(p)))
