# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/1/13 15:53

class CPU:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu = cpu
        self.disk = disk

#变量的赋值
cpu1 = CPU()
cpu2 = cpu1
print(cpu1)
print(cpu2)

print('------------------------------')
#类的浅拷贝
disk = Disk()
computer1 = Computer(cpu1,disk)
#浅拷贝
import copy
computer2 = copy.copy(computer1)
print(computer1,computer1.cpu,computer1.disk)
print(computer2,computer2.cpu,computer2.disk)

print('----------------------------------')
#深拷贝
computer3 = copy.deepcopy(computer1)
print(computer1,computer1.cpu,computer1.disk)
print(computer3,computer3.cpu,computer3.disk)