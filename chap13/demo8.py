# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/1/13 14:57

#特殊方法
#print(dir(object))
class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name = name
        self.age = age
class D(A):
    pass

#创建C类的对象
x = C('Jack',20)    #x是C类型的实例对象
print(x.__dict__)   #实例对象的属性字典
print(C.__dict__)   #类对象的方法字典
print('---------------------------')
print(x.__class__)  #输出对象所属于的类
print(C.__bases__)  #输出C类的父类元组
print(C.__base__)   #输出C类的第一个父类（基类）
print(C.__mro__)    #输出类的层次结构元组
print(A.__subclasses__())   #输出A的子类列表