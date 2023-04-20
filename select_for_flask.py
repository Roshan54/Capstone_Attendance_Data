import pyodbc
from datetime import datetime
import pandas as pd
cnxn = pyodbc.connect('DRIVER={SQL Server};'
                      'SERVER=tcp:facercgntn.database.windows.net;'
                      'DATABASE=Attendance_Database;UID=face_recognition;PWD=fnrcgntn123@#;')
subject_name = '' ## subject_name = db.Column(db.String(20), nullable=False) ## not class_id
cursor = cnxn.cursor()
query = "Select student_id , student_name ,subject_name, status, day , attendance_capture_time from [attendance] where day = DATENAME(weekday, GETDATE()) and cast(attendance_capture_time as date) = cast(GETDATE() as date) and subject_name = '" +subject_name+ "'"
cursor.execute(query)
columns = [column[0] for column in cursor.description]
rows = cursor.fetchall()
df1 = pd.DataFrame.from_records(rows, columns=columns)
print(df1)


#
# subject_name #as per the existing database
# 2000_Applied ML
# 2001_Knowledge and expert System
# 2002_Digital Portfolio
# 2003_Consulting
# 2004_AI in Enterprise System
# 2202_Ethical Leadership and Critical Decision Making
# 2203_Business Analysis and Assessments
# 2204_Statistical and Predictive Modelling for Analytics
# 2205_Visualizations, Leadership, and Business Communications
# 2206_Capstone