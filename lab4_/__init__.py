import happybase

conn = happybase.Connection('localhost',
                            table_prefix='user201600301252', table_prefix_separator=':',
                            port=9090, transport='buffered', protocol='binary')
# conn = happybase.Connection('localhost')

db = {
    'student': conn.table('student'),
    'teacher': conn.table('teacher'),
    'course': conn.table('course'),
    'student_course': conn.table('student_course'),
    'teacher_course': conn.table('teacher_course')
}
