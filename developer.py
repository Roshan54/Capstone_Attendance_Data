from tkinter import *
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1500x800")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root,text = "DEVELOPER",font = ("Times new roman",35,"bold"),bg = "White",fg = "blue" )
        title_lbl.place(x=0,y=0,width=1500,height=45)

        img_top = Image.open(r"/Users/harshbhatt/Desktop/final year project/college_images/dev.jpg")
        img_top = img_top.resize((1500,720),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root ,image = self.photoimg_top)
        f_lbl.place(x=0,y=55,width = 1500,height = 720)

        main_frame = Frame(f_lbl,bd=2,bg= "White")
        main_frame.place(x=1000,y=0,width=500,height=600)

        img_top1 = Image.open(r"/Users/harshbhatt/Desktop/final year project/college_images/us.jpg")
        img_top1 = img_top1.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)
        
        f_lbl = Label(main_frame ,image = self.photoimg_top1)
        f_lbl.place(x=300,y=0,width = 200,height = 200)

        # dEVELOPER
        deV_label = Label(main_frame,text="Hello, We are students",font = ("Times new roman",20,"bold"),bg = "White",fg = "blue")
        deV_label.place(x=0,y=5)

        deV_label = Label(main_frame,text=" of Aditya Silver Oak.",font = ("Times new roman",20,"bold"),bg = "White",fg = "blue")
        deV_label.place(x=0,y=40)

        deV_label = Label(main_frame,text="Our guide for it is",font = ("Times new roman",20,"bold"),bg = "White",fg = "blue")
        deV_label.place(x=0,y=120)

        deV_label = Label(main_frame,text="Professor Hardika Ma'am.",font = ("Times new roman",18,"bold"),bg = "White",fg = "blue")
        deV_label.place(x=0,y=155)

        img2 = Image.open(r"/Users/harshbhatt/Desktop/final year project/college_images/laptop.jpeg")
        img2 = img2.resize((500,390),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        f_lbl = Label(main_frame,image = self.photoimg2)
        f_lbl.place(x=0,y=220,width = 500,height = 390)








if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()