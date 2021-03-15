# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/1/19 16:30
import os

filename = 'stuInfor'
def main():
    while True:
        menu()
        choice = int(input('请选择'))
        if choice in [0,1,2,3,4,5,6,7]:
            if choice==0:
                answer = input('确定退出吗？y/n\n')
                if answer=='Y' or answer=='y':
                    print('谢谢您的使用！')
                    break
                else:
                    continue
            elif choice==1:
                insert()    #录入学生信息
            elif choice==2:
                search()    #查找学生信息
            elif choice==3:
                delete()    #删除学生信息
            elif choice==4:
                modify()    #修改学生信息
            elif choice==5:
                sort()      #排序
            elif choice==6:
                total()     #统计学生总人数
            elif choice==7:
                show()      #显示所有函数

def menu():
    print('==================学生信息管理系统==================')
    print('----------------------功能菜单--------------------')
    print('\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t5.排序')
    print('\t\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t\t0.退出')

#录入学生信息
def insert():
    student_list = []   #用于存储学生信息
    while True:
        stuID = input('请输入学生ID：')
        if not stuID:
            break
        stuname = input('请输入姓名：')
        if not stuname:
            break

        try:
            engrade = int(input('请输入英语成绩：'))
            pygrade = int(input('请输入Python成绩：'))
            javagrade = int(input('请输入Java成绩：'))
        except:
            print('输入无效，不是整数类型，请重新输入')
            continue

        #将录入的学生信息保存到字典中
        student = {'ID':stuID,'Name':stuname,'EnGrade':engrade,'PyGrade':pygrade,'JavaGrade':javagrade}
        student_list.append(student)

        #选择是否继续添加
        answer = input('是否继续输入？y/n\n')
        if answer=='y' or answer=='Y':
            continue
        elif answer=='n' or answer=='N':
            print()
            break

    #调用save()函数
    save(student_list)
    print('学生信息录入完毕！')

#将信息保存至文件
def save(lst):
    try:
        stu_txt = open(filename,'a',encoding='utf-8')   #存在stuInfor.txt以追加方式打开
    except:
        stu_txt = open(filename,'w',encoding='utf-8')   #否则以写方式打开
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()

#查找学生信息
def search():
    student_query = []
    while True:
        id = ''
        name = ''
        if os.path.exists(filename):
            mode = input('按ID查找请输入1；按姓名查找请输入2：')
            if mode == '1':
                id = input('请输入学生ID：')
            elif mode == '2':
                name = input('请输入学生姓名：')
            else:
                print('输入有误！请重新输入。')
                search()

            with open(filename,'r',encoding='utf-8') as rfile:
                student = rfile.readlines()
                for item in student:
                    d = eval(item)
                    if id != '':
                        if d['ID'] == id:
                            student_query.append(d)
                    elif name != '':
                        if d['Name'] == name:
                            student_query.append(d)
            #显示查询结果
            show_student(student_query)
            #清空列表
            student_query.clear()
            answer = input('是否继续查询？y/n')
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break
        else:
            print('学生信息不存在！')
            return
def show_student(lst):
    if len(lst) == 0:
        print('没有查询到学生信息，无数据显示！')
        return
    #定义标题显示格式
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('ID','姓名','英语成绩','Python成绩','Java成绩','总成绩'))
    #定义内容的显示格式
    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    for item in lst:
        print(format_data.format(item.get('ID'),
                                 item.get('Name'),
                                 item.get('EnGrade'),
                                 item.get('PyGrade'),
                                 item.get('JavaGrade'),
                                 int(item.get('EnGrade'))+int(item.get('PyGrade'))+int(item.get('JavaGrade'))
                                 ))

#删除学生信息
def delete():
    while True:
        student_id = input('请输入要删除的学生ID：')
        if student_id != '':
            if os.path.exists(filename):    #判断要stuInfor.txt文件是否存在
                with open(filename,'r',encoding='utf-8') as file:   #以只读方式打开文件
                    student_old = file.readlines()  #将文本文件中的每一行都作为独立的字符串对象，并将这些对象放入列表中返回
            else:
                student_old=[]
            flag = False    #标记是否删除
            if student_old:
                with open(filename,'w',encoding='utf-8') as wfile:
                    d={}
                    for item in student_old:    #每个item是字符串
                        d = dict(eval(item))    #将字符串转化为字典，eval函数就是实现list、dict、tuple与str之间的转化。eval参数是一个字符串, 可以把这个字符串当成表达式来求值
                        if d['ID'] != student_id:
                            wfile.write(str(d)+'\n')
                        else:
                            flag = True
                    if flag:
                        print('ID为{0}的学生信息已删除。'.format(student_id))
                    else:
                        print(f'ID为{student_id}的学生不存在。')
            else:
                print('无学生信息！')
                break
            show()  #删除操作后显示所有学生信息
            answer = input('是否继续删除？y/n\n')
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break

#修改学生信息（代码不完善，当ID不存在时会导致文件中所有信息丢失，还需修改）
def modify():
    show()
    if os.path.exists(filename):    #判断stuInfor.txt文件是否存在
        with open(filename,'r',encoding='utf-8') as rfile:
            student_old = rfile.readlines() #将每条学生信息以字符串的形式存入列表中
    else:
        return
    student_id = input('请输入要修改的学生ID：')
    if student_id != '':
        with open(filename,'w',encoding='utf-8') as wfile:
            count=0
            for item in student_old:
                d = eval(item)
                if d['ID'] == student_id:   #需要修改信息的学生ID找到
                    count = count+1
                    print('找到该生信息！请修改。')
                    while True:
                        try:
                            d['Name'] = input('请重新输入姓名：')
                            d['EnGrade'] = input('请输入英语成绩：')
                            d['PyGrade'] = input('请输入Python成绩：')
                            d['JavaGrade'] = input('请输入Java成绩：')
                        except:
                            print('输入有误，请重新输入！')
                        else:
                            break
                    wfile.write(str(d)+'\n')
                    print('修改成功！')
                else:
                    wfile.write(str(d)+'\n')
            if count == 0:
                print('该学生不存在！')
            answer = input('是否继续修改学生信息？y/n：')
            if answer == 'y' or answer == 'Y':
                modify()
            else:
                show()
    else:
        print('学生ID不能为空！')
        modify()

#根据学生成绩排序
def sort():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            students_list = rfile.readlines()
        students_new = []
        for item in students_list:
            d = eval(item)
            students_new.append(d)
    else:
        print('文件不存在，无法排序！')
        return

    asc_or_desc = input('请选择（0.升序，1.降序）：')
    if asc_or_desc == '0':
        asc_or_desc_bool = False
    elif asc_or_desc == '1':
        asc_or_desc_bool = True
    else:
        print('输入有误，请重新输入！')
        sort()
    mode = input('请选择排序方式（1.按英语成绩排序 2.按Python成绩排序 3.按Java成绩排序 0.按总成绩排序）：')
    if mode == '1':
        students_new.sort(key=lambda students_new:int(students_new['EnGrade']),reverse=asc_or_desc_bool)
    elif mode == '2':
        students_new.sort(key=lambda students_new: int(students_new['PyGrade']),reverse=asc_or_desc_bool)
    elif mode == '3':
        students_new.sort(key=lambda students_new: int(students_new['JavaGrade']),reverse=asc_or_desc_bool)
    elif mode == '0':
        students_new.sort(key=lambda students_new: int(students_new['EnGrade'])+int(students_new['PyGrade'])+int(students_new['JavaGrade']),reverse=asc_or_desc_bool)
    else:
        print('输入有误，请重新输入！')
        sort()
    show_student(students_new)

#统计全部学生人数
def total():
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            students = rfile.readlines()
            if students:
                print('共有{0}名学生'.format(len(students)))
            else:
                print('学生人数为0，请录入学生信息！')
    else:
        print('文件不存在，无法统计！')

#显示全体学生信息
def show():
    student_list = []
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            students = rfile.readlines()
        for item in students:
            student_list.append(eval(item))
        if student_list:
            show_student(student_list)
        else:
            print('学生人数为0。')
    else:
        print('学生信息文件不存在！')

if __name__ == '__main__':
    main()