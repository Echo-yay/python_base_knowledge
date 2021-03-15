# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/1/13 16:33
def fun1():
    pass
def fun2():
    pass

class Student:
    native_place = 'Beijing'    #类属性
    def study(self,name,age):    #实例方法
        self.name = name
        self.age = age
    @staticmethod
    def sm():   #静态方法
        pass
    @classmethod
    def cm(cls):    #类方法
        pass
a = 1
b = 2
c = a+b