from tkinter import *
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1500x800")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root,text = "HELP DESK",font = ("Times new roman",35,"bold"),bg = "White",fg = "blue" )
        title_lbl.place(x=0,y=0,width=1500,height=45)

        img_top = Image.open(r"C:\Users\Admin\Desktop\Untitled Folder\college_images\laptop.jpeg")
        img_top = img_top.resize((1500,720),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root ,image = self.photoimg_top)
        f_lbl.place(x=0,y=55,width = 1500,height = 720)

        deV_label = Label(f_lbl,text="Email ID: harshabhatt99@gmail.com",font = ("Times new roman",20,"bold"),bg = "White",fg = "blue")
        deV_label.place(x=525,y=200)




if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()