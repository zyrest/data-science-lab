from lab4_ import db

student = db['student']
teacher = db['teacher']
course = db['course']

print('向学生表中插入一条数据：')
s_d = {
    'info:SID': '201600301111',
    'info:NAME': '张三',
    'info:SEX': '男',
    'info:CLASS': '2016'
}
student.put(s_d['info:SID'], s_d)
print('学生表数据插入成功')

print('向课程表中插入一条数据：')
c_d = {
    'info:CID': '666666',
    'info:NAME': '中学物理'
}
course.put(c_d['info:CID'], c_d)
print('课程表数据插入成功')

print('向教师表中插入多条数据：')
t_d = [
    {
        'info:TID': '666666',
        'info:NAME': '张三',
        'info:DNAME': '软件学院'
    },
    {
        'info:TID': '777777',
        'info:AGE': '54',
        'info:NAME': '李四'
    }
]
for one in t_d:
    teacher.put(one['info:TID'], one)
print('教师表数据插入成功')
