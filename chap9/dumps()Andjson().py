# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/12/28 18:01

#eval()函数可以执行字符串中的代码
x = 'input("请输入用户名：")'
eval(x)

#json的使用，把列表、元组、字典等转换成为Json字符串
person = {'name':'张三','age':18,'gender':'F'}

#如果想把字典传给前端页面或把他写入一个文件里
#'{"name":"张三","age":18,"gender":"F"}'
import json

m = json.dumps(person)  #dumps()将字典、元组等转换为字符串
print(m,type(m))    #<class 'str'>

n = '{"name": "zhangsan", "age": 18, "gender": "F"}'
p = eval(n)
print(p,type(p))

#将json字符串转换为python里的数据
s = json.loads(n)
print(s,type(s))    #{'name': 'zhangsan', 'age': 18, 'gender': 'F'} <class 'dict'>

#python                 json
#True                   true
#False                  false
#字符串                  字符串
#字典                    对象
#列表、元组               数组([])

print(json.dumps(['hello','good','yes']))   #["hello", "good", "yes"]
print(json.dumps(('hello','good','yes')))   #["hello", "good", "yes"]
#print(json.dumps({'hello','good','yes'}))