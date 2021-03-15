# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/1/12 16:28

class Car:
    def __init__(self,brand):
        self.brand = brand  #属性

    def start(self):
        print('汽车启功...')

car = Car('保时捷')
car.start()
print(car.brand)