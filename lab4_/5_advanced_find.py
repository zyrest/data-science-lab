from lab4_ import db

student = db['student']
teacher = db['teacher']
course = db['course']
student_course = db['student_course']
teacher_course = db['teacher_course']

all_sc = student_course.scan()


def myAlign(string, length=0):
    if length == 0:
        return string
    slen = len(string)
    re = string
    placeholder = ' '
    for s in string:
        if ord(s) > 127:
            placeholder = u'　'
            break
    while slen < length:
        re += placeholder
        slen += 1
    return re


print('找出选课数目排名前10的学生:')
task3_result = {}
for k, sc in all_sc:
    key = k.decode('utf8')
    sid = key.split(':')[0]
    task3_result[sid] = 1 if sid not in task3_result.keys() else task3_result[sid]+1

sorted_task3 = sorted(task3_result.items(), key=lambda item: item[1])
sorted_task3.reverse()
print('{:<20s}\t{:<20s}\t{:<20s}'.format('学号', '姓名', '选课数'))
for i in range(10):
    coll = sorted_task3[i]
    sid = coll[0]
    count = coll[1]
    sname = student.row(sid.encode('utf8'))[b'info:NAME'].decode('utf8')
    print('{:<20s}\t{:<20s}\t{:<20d}'.format(sid, sname, count))


print('求每门课程的选修人数和平均成绩:')
task6_result = []
cid_count = {}
cid_score = {}
for k, sc in all_sc:
    key = k.decode('utf8')
    cid = key.split(':')[1]
    score = int(sc[b'info:SCORE'].decode('utf8')) if b'info:SCORE' in sc.keys() else 0
    cid_count[cid] = 1 if cid not in cid_count.keys() else cid_count[cid] + 1
    cid_score[cid] = score if cid not in cid_score.keys() else cid_score[cid] + score

for k, count in cid_count.items():
    cname = course.row(k.encode('utf8'))[b'info:NAME'].decode('utf8')
    one = {
        'cid': k,
        'count': count,
        'name': cname,
        'per_score': round(cid_score[k] / count, 2)
    }
    task6_result.append(one)

task6_result = sorted(task6_result, key=lambda item: item['per_score'])
task6_result.reverse()
print('{:<20}{:<20}{:<20}{:<20}'.format('课程号', '课程名', '选课数', '平均成绩'))
for res in task6_result:
    print('{}{}{}{}'.format(
        myAlign(res['cid'], 20), myAlign(res['name'], 20),
        myAlign(str(res['count']), 20), myAlign(str(res['per_score']), 20)))
