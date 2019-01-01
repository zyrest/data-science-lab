from lab4_ import db

student = db['student']
teacher = db['teacher']

print('求所有学生的姓名,年龄:')
task4_result = student.scan()
print('{:<10s}\t{:<10s}'.format('姓名', '年龄'))
for key, value in task4_result:
    r_dict = dict(value)
    name = r_dict[b'info:NAME'].decode('utf8')
    age = r_dict[b'info:AGE'].decode('utf8')
    print('{:<10s}\t{:<10s}'.format(name, age))

print('找出所有男老师:')
task9_result = teacher.scan()
for key, value in task9_result:
    r_dict = dict(value)
    sex = r_dict[b'info:SEX'].decode('utf8')
    if sex == '男':
        pri_str = ', '.join((k.decode('utf8')+'='+v.decode('utf8')) for k, v in r_dict.items())
        print(pri_str)
