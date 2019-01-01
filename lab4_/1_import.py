from lab4_ import db
import csv

student = db['student']
teacher = db['teacher']
course = db['course']
student_course = db['student_course']
teacher_course = db['teacher_course']


def get_data_dict(filename):
    keys = []
    dict_ans = []
    with open(filename) as scsv:
        reader = csv.reader(scsv)
        for line in reader:
            index = reader.line_num
            if index == 1:
                keys = list(line)
                for i in range(len(keys)):
                    keys[i] = 'info:' + str(keys[i])
                continue

            one_ans = dict()
            one_list = list(line)
            for i in range(len(one_list)):
                one_ans[keys[i]] = one_list[i]
            dict_ans.append(one_ans)
    return dict_ans


if __name__ == '__main__':
    s_dict = get_data_dict('csvs/student.csv')
    for one in s_dict:
        student.put(one['info:SID'], one)
    print('student表数据导入成功!')

    t_dict = get_data_dict('csvs/teacher.csv')
    for one in t_dict:
        teacher.put(one['info:TID'], one)
    print('teacher表数据导入成功!')

    c_dict = get_data_dict('csvs/course.csv')
    for one in c_dict:
        course.put(one['info:CID'], one)
    print('course表数据导入成功!')

    sc_dict = get_data_dict('csvs/student_course.csv')
    for one in sc_dict:
        student_course.put(one['info:SID']+':'+one['info:CID']+':'+one['info:TID'], one)
    print('student-course表数据导入成功!')

    tc_dict = get_data_dict('csvs/teacher_course.csv')
    for one in tc_dict:
        teacher_course.put(one['info:TID']+':'+one['info:CID'], one)
    print('teacher-course表数据导入成功!')
