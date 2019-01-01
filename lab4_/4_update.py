from lab4_ import db

student = db['student']
teacher = db['teacher']
course = db['course']

s_rowkey = '201600301111'
s_data = {'info:CLASS': '2017'}
print('更新学号为{}的学生数据:{}'.format(s_rowkey, s_data))
student.put(s_rowkey, s_data)
print('更新学生表数据成功!\n')


c_rowkey = '666666'
c_data = {'info:NAME': '中学生物'}
print('更新编号为{}的课程数据:{}'.format(c_rowkey, c_data))
course.put(c_rowkey, c_data)
print('更新课程表数据成功!\n')


t_rowkeys = ['666666', '777777']
s_data = {'info:AGE': '66'}
for rowkey in t_rowkeys:
    print('更新编号为{}的教师数据:{}'.format(rowkey, s_data))
    teacher.put(rowkey, s_data)
print('更新教师表数据成功!\n')
