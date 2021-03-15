# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/1/12 17:17

#多态
class Animal(object):
    def eat(self):
        print('动物会吃。')

class Dog(Animal):
    def eat(self):
        print('狗吃骨头...')

class Cat(Animal):
    def eat(self):
        print('猫吃鱼...')

class Person(object):
    def eat(self):
        print('人吃五谷杂粮...')

#定义一个函数
def fun(obj):
    obj.eat()

#开始调用函数
fun(Cat())  #Cat重写了Animal中eat方法，再调用
fun(Dog())
fun(Animal())
print('----------------------------------')
fun(Person())