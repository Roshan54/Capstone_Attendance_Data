from tkinter import *
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime

class Face_Recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1500x800")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root,text = "FACE RECOGNITION",font = ("Times new roman",35,"bold"),bg = "White",fg = "darkgreen" )
        title_lbl.place(x=0,y=0,width=1500,height=45)

        img_top = Image.open(r"/Users/harshbhatt/Desktop/Face Recogition system/college_images/face_detector1.jpg")
        img_top = img_top.resize((650,700),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root ,image = self.photoimg_top)
        f_lbl.place(x=0,y=55,width = 650,height = 700)

        img_bottom = Image.open(r"/Users/harshbhatt/Desktop/Face Recogition system/college_images/face-recognition-attendance-system.png")
        img_bottom = img_bottom.resize((950,700),Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        
        f_lbl = Label(self.root ,image = self.photoimg_bottom)
        f_lbl.place(x=650,y=55,width = 950,height = 700)

        b1_1 = Button(f_lbl,text="Face Recognition",cursor="hand2",command = self.face_recog,font = ("Times new roman",18,"bold"),bg = "darkgreen",fg = "white" )
        b1_1.place(x=370,y=620,width=200,height=40)

    def mark_attendance(self,n,r,d):
        with open("attendance.csv","r+",newline="\n") as f:
            mydataList = f.readlines()
            name_list = []
            for line in mydataList:
                entry = line.split((","))
                name_list.append(entry[0])
            
            if((n not in name_list) and (r not in name_list) and (d not in name_list)):
                now =datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtstring = now.strftime("%H:%M:%S")
                f.writelines(f"\n{n},{r},{d},{dtstring},{d1},present")

                       


    #==============Face Recognition==================

    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbours,color,text,clf):
            gray_image =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)

            coord = []
            
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),((x+w),(y+h)),(0,255,0),3)
                id,predict =clf.predict(gray_image[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost",username="root",password="13055Don@",database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("select EmployeeName from employee where EmployeeId="+str(id))
                n=my_cursor.fetchone()
                n= "+".join(n)

                my_cursor.execute("select EmployeeId from employee where EmployeeId="+str(id))
                r=my_cursor.fetchone()
                r= "+".join(r)

                my_cursor.execute("select Dep from employee where EmployeeId="+str(id))
                d=my_cursor.fetchone()
                d= "+".join(d)

                if confidence>77:
                    cv2.putText(img,f"EmployeeName:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"EmployeeId:{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(n,r,d)

                else:
                    cv2.rectangle(img,(x,y),((x+w),(y+h)),(0,0,255),3)
                    cv2.putText(img,"Unknown face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

            return coord

        def recognize(img,clf,faceCascade):
            coord = draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")   
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret,img= video_cap.read()
            img = recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()           


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()