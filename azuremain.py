import os
import pickle
import numpy as np
import cv2
import face_recognition
import cvzone
import numpy as np
from datetime import datetime , date
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import pyodbc
import pandas as pd
import time
from tkinter import *

top = Tk()
top.geometry("450x300")

#Connection string to fetch images from Azure blob storage
connection_string = "DefaultEndpointsProtocol=https;AccountName=facerecognitioncapstone;AccountKey=DayqekRI//ZUtjMKwsq+LhIWPzlaJ53LcBepkVLTNl028QXziXp/1appbdR7fB4Zhizba2YpANb++AStnTNKZA==;EndpointSuffix=core.windows.net"

#Connection string for Azure server database
cnxn = pyodbc.connect('DRIVER={SQL Server};'
                      'SERVER=tcp:facercgntn.database.windows.net;'
                      'DATABASE=Attendance_Database;UID=face_recognition;PWD=fnrcgntn123@#;')
cursor = cnxn.cursor()

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

imgBackground = cv2.imread('Resources/background.png')

# Importing the mode images into a list
folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))

# Load the encoding file
print("Loading Encode File ...")
file = open('Encode.p', 'rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds
print("Encode File Loaded")

modeType = 0
counter = 0
id = -1
imgStudent = []
img_id =0

def display_username():
    class_id_var = class_id_input_area.get()
    class_id_label.config(text=class_id_var)
    global class_id
    class_id = class_id_var
    top.destroy()

def azuredatabase(student_id):
    query = "Select student.student_id, student_name ,professor_name,subject_name,course_name,class_id ,day from student  \
            left join timetable on student.student_id = timetable.student_id  \
            left join course_subject on timetable.subject_id = course_subject.subject_id  \
            left join professor on timetable.professor_id = professor.professor_id  \
            where student.student_id = '" + str(student_id) + \
             "' and day = DATENAME(weekday, GETDATE()) and ABS(DATEDIFF(MINUTE, '2023-04-12 10:00:42.103',(CAST(CAST('2023-04-12 10:00:42.103' AS DATE) AS DATETIME) + CAST(start_time AS DATETIME)))) <= 30 "

    cursor.execute(query)
    # Create a list of column names
    columns = [column[0] for column in cursor.description]
    # Create a list of rows
    rows = cursor.fetchall()
    # Create a dataframe from the rows and columns
    df = pd.DataFrame.from_records(rows, columns=columns)
    df_dict = df.to_dict(orient='records')
    return df_dict

def attendance_update(student_id):
    cursor = cnxn.cursor()
    query = "INSERT INTO [dbo].[attendance]([student_id],[professor_id],[day],[time],[status],[class_id],[student_name],[professor_name],[attendance_capture_time], subject_name) \
            (select student_id, [professor_id], [day], start_time, 'Present' as [status], [class_id], [student_name], [professor_name], getdate() as [attendance_capture_time], subject_name from  \
            (Select student.student_id, student_name ,start_time, day, professor.professor_id, professor_name, subject_name, course_name, class_id from student  \
            left join timetable on student.student_id = timetable.student_id  \
            left join course_subject on timetable.subject_id = course_subject.subject_id  \
            left join professor on timetable.professor_id = professor.professor_id  \
            where student.student_id = '" + str(student_id) +  \
            "' and day = DATENAME(weekday, GETDATE()) and ABS(DATEDIFF(MINUTE, '2023-04-12 10:00:42.103',(CAST(CAST('2023-04-12 10:00:42.103' AS DATE) AS DATETIME) + CAST(start_time AS DATETIME)))) <= 30)a)"
    cursor.execute(query)
    cnxn.commit()

while True:
    success, img = cap.read()

    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    imgBackground[162:162 + 480, 55:55 + 640] = img
    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]
    cv2.waitKey(1)

    if faceCurFrame:
        for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            print("matches", matches)
            print("faceDis", faceDis)
            matchIndex = np.argmin(faceDis)
            print(matches[matchIndex])

            if not matches[matchIndex]:
                img_id += 1
                imgBGR = cv2.cvtColor(imgS, cv2.COLOR_RGB2BGR)
                file_name_path = "Resources/unknown"+str(img_id) + ".jpg"
                cv2.imwrite(file_name_path, imgBGR)
                cv2.putText(imgBGR, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                cv2.imshow("cropped Face", imgBGR)
                time.sleep(5)
                cv2.waitKey(1)

            if matches[matchIndex]:
                print("Known Face Detected")
                print(studentIds[matchIndex])
                print(type(studentIds[matchIndex]))
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
                imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)
                student_id = studentIds[matchIndex]
                ##call the azure database function
                df_dict = azuredatabase(student_id)
                print(df_dict)
                #Enter in which class you are in
                class_id = Label(top, text="Enter in which class you are in :").place(x=40, y=60)
                submit_button = Button(top, text="Submit", command=display_username).place(x=40, y=130)
                class_id_input_area = Entry(top, width=30)
                class_id_input_area.place(x=110, y=60)
                class_id_label = Label(top, text="")
                top.mainloop()
                ## call class_id compare and update information .
                print(id)
                if counter == 0:
                    cvzone.putTextRect(imgBackground, "Loading", (275, 400))
                    cv2.imshow("Face Attendance", imgBackground)
                    cv2.waitKey(1)
                    counter = 1
                    modeType = 1

        if counter != 0:

            if counter == 1:
                blob_service_client = BlobServiceClient.from_connection_string(connection_string)
                container_name = "facercgntn"
                container_client = blob_service_client.get_container_client(container_name)
                blob_name = "{}.png".format(student_id)
                blob_client = container_client.get_blob_client(blob_name)
                image_data = blob_client.download_blob().content_as_bytes()
                nparr = np.frombuffer(image_data, np.uint8)
                imgStudent = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                if df_dict[0]['class_id'] == class_id :
                    cursor.execute("Select * from attendance")
                    columns = [column[0] for column in cursor.description]
                    rows = cursor.fetchall()
                    df1 = pd.DataFrame.from_records(rows, columns=columns)
                    print(pd.to_datetime(df1['attendance_capture_time']).dt.date)
                    subset = df1.loc[(df1['student_id'] == student_id) & (df1['subject_name'] == df_dict[0]['subject_name']) & (pd.to_datetime(df1['attendance_capture_time']).dt.date == date.today())]
                    print(subset)
                    if subset.empty :
                        atnd = attendance_update(student_id)
                        print('attendance marked')
                    else:
                        modeType = 3
                        counter = 0
                        imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]
                else:
                    print('you are in wrong class')

            if modeType != 3:

                if 10 < counter < 20:
                    modeType = 2

                imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

                if counter <= 10:
                    if df_dict[0]['class_id'] == class_id:
                        cv2.putText(imgBackground, str(df_dict[0]['class_id']), (861, 125),
                                cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                    else :
                        cv2.putText(imgBackground, 'You are in wrong class', (861, 125),
                                    cv2.FONT_HERSHEY_COMPLEX, 0.1, (255, 255, 255), 1)
                    cv2.putText(imgBackground, str(df_dict[0]['subject_name']), (1006, 550),
                                cv2.FONT_HERSHEY_COMPLEX, 0.25, (255, 255, 255), 1)
                    cv2.putText(imgBackground, str(student_id), (1006, 493),
                                cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                    (w, h), _ = cv2.getTextSize(df_dict[0]['student_name'], cv2.FONT_HERSHEY_COMPLEX, 0.5, 1)
                    offset = (414 - w) // 2
                    cv2.putText(imgBackground, str(df_dict[0]['student_name']), (808 + offset, 445),
                                cv2.FONT_HERSHEY_COMPLEX, 0.5, (50, 50, 50), 1)

                    imgStudent_resized = cv2.resize(imgStudent, (216, 216))

                    imgBackground[175:175 + 216, 909:909 + 216] = imgStudent_resized

                counter += 1

                if counter >= 20:
                    counter = 0
                    modeType = 0
                    studentInfo = []
                    imgStudent = []
                    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]
    else:
        modeType = 0
        counter = 0
    #cv2.imshow("Webcam", img)
    cv2.imshow("Face Attendance", imgBackground)
    cv2.waitKey(1)
cursor.close()
cnxn.close()