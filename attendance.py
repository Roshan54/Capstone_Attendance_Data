from tkinter import *
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata = []
class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1500x800")
        self.root.title("Face Recognition System")

        #====================variables==============
        self.var_attend_id=StringVar()
        self.var_attend_name = StringVar()
        self.var_attend_dep = StringVar()
        self.var_attend_time = StringVar()
        self.var_attend_date = StringVar()
        self.var_attend_atst = StringVar()



        #image1
        img = Image.open(r"/Users/harshbhatt/Desktop/final year project/college_images/smart-attendance.jpg")
        img = img.resize((750,200),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image = self.photoimg)
        f_lbl.place(x=0,y=0,width = 750,height = 200)

        #image2
        img1 = Image.open(r"/Users/harshbhatt/Desktop/final year project/college_images/clg.jpg")
        img1 = img1.resize((750,200),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image = self.photoimg1)
        f_lbl.place(x=750 ,y=0,width = 750,height = 200)

        #Background image
        img3 = Image.open(r"/Users/harshbhatt/Desktop/final year project/college_images/laptop.jpeg")
        img3 = img3.resize((1500,800),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root,image = self.photoimg3)
        bg_img.place(x=0,y=200,width = 1500,height = 800)

        title_lbl = Label(bg_img,text = "ATTENDANCE MANAGEMENT SYSTEM",font = ("Times new roman",35,"bold"),bg = "White",fg = "darkgreen" )
        title_lbl.place(x=0,y=0,width=1500,height=45)

        main_frame = Frame(bg_img,bd=2,bg= "White")
        main_frame.place(x=15,y=55,width=1450,height=700)

        #left label frame
        Left_frame = LabelFrame(main_frame,bd=2,bg="White",relief=RIDGE,text="Employee Attendance Details",font = ("Times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=700,height=585)

        img_left = Image.open(r"/Users/harshbhatt/Desktop/final year project/college_images/girl.jpeg")
        img_left = img_left.resize((685,130),Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame ,image = self.photoimg_left)
        f_lbl.place(x=5,y=0,width = 685,height = 130)

        left_inside_frame = Frame(Left_frame,bd=2,relief =RIDGE,bg= "White")
        left_inside_frame.place(x=0,y=135,width=695,height=380)

        # Labels and entry
        #attendanceid id
        attendanceid_label = Label(left_inside_frame,text="Employee ID:",font = ("Times new roman",12,"bold"),bg="White")
        attendanceid_label.grid(row=0,column=0,padx=10,pady=5,sticky =W)

        attendanceid_entry = ttk.Entry(left_inside_frame,width=20,textvariable = self.var_attend_id,font = ("Times new roman",12,"bold"))
        attendanceid_entry.grid(row=0,column=1,padx=10,pady=5,sticky =W)

        #employee name
        employeeName_label = Label(left_inside_frame,text="Employee Name:",font = ("Times new roman",12,"bold"),bg="White")
        employeeName_label.grid(row=0,column=2,padx=10,pady=5,sticky =W)

        employeeName_entry = ttk.Entry(left_inside_frame, width=20,textvariable = self.var_attend_name,font = ("Times new roman",12,"bold"))
        employeeName_entry.grid(row=0,column=3,padx=10,pady=5,sticky =W)

        
        #Department
        Dep_label = Label(left_inside_frame,text="Department:",font = ("Times new roman",12,"bold"),bg="White")
        Dep_label.grid(row=1,column=0,padx=10,pady=5,sticky =W)

        Dep_entry = ttk.Entry(left_inside_frame, width=20,textvariable = self.var_attend_dep,font = ("Times new roman",12,"bold"))
        Dep_entry.grid(row=1,column=1,padx=10,pady=5,sticky =W)

        #Time
        time_label = Label(left_inside_frame,text="Time:",font = ("Times new roman",12,"bold"),bg="White")
        time_label.grid(row=1,column=2,padx=10,pady=5,sticky =W)

        time_entry = ttk.Entry(left_inside_frame, width=20,textvariable = self.var_attend_time,font = ("Times new roman",12,"bold"))
        time_entry.grid(row=1,column=3,padx=10,pady=5,sticky =W)

        #date
        date_label = Label(left_inside_frame,text="Date:",font = ("Times new roman",12,"bold"),bg="White")
        date_label.grid(row=2,column=0,padx=10,pady=5,sticky =W)

        date_entry = ttk.Entry(left_inside_frame, width=20,textvariable = self.var_attend_date,font = ("Times new roman",12,"bold"))
        date_entry.grid(row=2,column=1,padx=10,pady=5,sticky =W)

        #attendance
        attendancelabel = Label(left_inside_frame,text="Attendance status:",font = ("Times new roman",12,"bold"),bg="White")
        attendancelabel.grid(row=3,column=0,padx=10,pady=5,sticky =W)

        self.attendance_status = ttk.Combobox(left_inside_frame, width=20,textvariable = self.var_attend_atst,font = ("Times new roman",12,"bold"),state="readonly")
        self.attendance_status["values"] = ("status","Present","Absent")
        self.attendance_status.current(0)
        self.attendance_status.grid(row=3,column=1,padx=2,pady=10)

        # button frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="White")
        btn_frame.place(x=0,y=300,width=680,height=35)

        save_btn = Button(btn_frame,text="Import csv",command =self.importcsv,width=24,font = ("Times new roman",12,"bold"),bg="blue",fg="White")
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame,text="Export csv",command = self.exportcsv,width=24,font = ("Times new roman",12,"bold"),bg="blue",fg="White")
        update_btn.grid(row=0,column=1)

        reset_btn = Button(btn_frame,text="Reset",command = self.reset_data,width=24,font = ("Times new roman",12,"bold"),bg="blue",fg="White")
        reset_btn.grid(row=0,column=2)

        

        #Right label frame
        Right_frame = LabelFrame(main_frame,bd=2,bg="White",relief=RIDGE,text="Attendance Details",font = ("Times new roman",12,"bold"))
        Right_frame.place(x=725,y=10,width=700,height=585)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="White")
        table_frame.place(x=5,y=5,width=690,height=455)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame,column =("name","id","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance ")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width = 100)
        self.AttendanceReportTable.column("name",width = 100)
        self.AttendanceReportTable.column("department",width = 100)
        self.AttendanceReportTable.column("time",width = 100)
        self.AttendanceReportTable.column("date",width = 100)
        self.AttendanceReportTable.column("attendance",width = 100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    #==================Fetch Data====================
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    

    #Import csv
    def importcsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes = (("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread =csv.reader(myfile,delimiter =",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
    
    #Export csv
    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No data found to export",parent =self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes = (("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write = csv.writer(myfile,delimiter =",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"successfully!!")

        except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_attend_id.set(rows[0])
        self.var_attend_name.set(rows[1])
        self.var_attend_dep.set(rows[2])
        self.var_attend_time.set(rows[3])
        self.var_attend_date.set(rows[4])
        self.var_attend_atst.set(rows[5])

    def reset_data(self):
        self.var_attend_id.set("")
        self.var_attend_name.set("")
        self.var_attend_dep.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_atst.set("")


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()