import pyodbc
import pandas as pd
cnxn = pyodbc.connect('DRIVER={SQL Server};'
                      'SERVER=tcp:facercgntn.database.windows.net;'
                      'DATABASE=Attendance_Database;UID=face_recognition;PWD=fnrcgntn123@#;')

cursor = cnxn.cursor()
query = "Select * from [attendance]"
# student_id = '1001'
# query = "Select student.student_id, student_name ,professor_name,subject_name,course_name,class_id ,day from student  \
#         left join timetable on student.student_id = timetable.student_id  \
#         left join course_subject on timetable.subject_id = course_subject.subject_id  \
#         left join professor on timetable.professor_id = professor.professor_id " \
#         "where student.student_id = '" + str(student_id) + \
#         "' and day = DATENAME(weekday, GETDATE()) and ABS(DATEDIFF(MINUTE, '2023-04-12 10:00:42.103',(CAST(CAST('2023-04-12 10:00:42.103' AS DATE) AS DATETIME) + CAST(start_time AS DATETIME)))) <= 30"

cursor.execute(query)
columns = [column[0] for column in cursor.description]
rows = cursor.fetchall()
df1 = pd.DataFrame.from_records(rows, columns=columns)
print(df1)


# cursor = cnxn.cursor()
# query = "Truncate table attendance;"\
#         "DBCC CHECKIDENT ('attendance', RESEED, 1);"
# cursor.execute(query)
# cursor.close()
# cnxn.commit()
# cnxn.close()
#

# cursor = cnxn.cursor()
# query = "INSERT INTO [dbo].[attendance]([student_id],[day],[time],[status],[class_id],[student_name],[subject_name])" \
#         "VALUES (1010,'Wednesday','10:10:00.0000000','Absent','210E','Vivek','2002_Digital Portfolio')," \
#         "(1011,'Wednesday','10:10:00.0000000','Absent','210E','Nidhi','2002_Digital Portfolio')"
# cursor.execute(query)
# cursor.close()
# cnxn.commit()
# cnxn.close()