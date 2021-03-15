# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/1/12 16:32

class Student:
    def __init__(self,name,age):
        self.name = name
        self.__age = age    #若不希望年龄在类的外部被使用，所以使用__修饰

    def show(self):
        print(self.name,self.__age)

stu = Student('Echo',20)
stu.show()  #Echo 20
#在类的外部使用name和age
print(stu.name)     #Echo

#print(stu.__age)    #AttributeError: 'Student' object has no attribute '__age'

#print(dir(stu))
print(stu._Student__age)#在类的外部可以通过_Student__age进行访问