from tkinter import *
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1500x800")
        self.root.title("Face Recognition System")

        #==================variable=================
        self.var_dep = StringVar()
        self.var_work = StringVar()
        self.var_year = StringVar()
        self.var_exp = StringVar()
        self.var_employeeID = StringVar()
        self.var_employeeName = StringVar()
        self.var_employeeEmailID = StringVar()
        self.var_employeeContact = StringVar()
        self.var_employeeGen = StringVar()
        self.var_employeeNum = StringVar()
        self.var_employeeSal = StringVar()
        self.var_employeeAdd = StringVar()
        self.var_employeeDOB = StringVar()
        self.var_employeeB = StringVar()


        #image1
        img = Image.open(r"/Users/harshbhatt/Desktop/Face Recogition system/college_images/clg.jpg")
        img = img.resize((500,130),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image = self.photoimg)
        f_lbl.place(x=0,y=0,width = 500,height = 130)
        #image2
        img1 = Image.open(r"/Users/harshbhatt/Desktop/Face Recogition system/college_images/girl.jpeg")
        img1 = img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f_lbl = Label(self.root,image = self.photoimg1)
        f_lbl.place(x=500 ,y=0,width = 500,height = 130)
        #image3
        img2 = Image.open(r"/Users/harshbhatt/Desktop/Face Recogition system/college_images/smart-attendance.jpg")
        img2 = img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        f_lbl = Label(self.root,image = self.photoimg2)
        f_lbl.place(x=1000,y=0,width = 500,height = 130)

        #background image
        img3 = Image.open(r"/Users/harshbhatt/Desktop/Face Recogition system/college_images/laptop.jpeg")
        img3 = img3.resize((1500,800),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root,image = self.photoimg3)
        bg_img.place(x=0,y=130,width = 1500,height = 800)

        title_lbl = Label(bg_img,text = "EMPLOYEE MANAGEMENT SYSTEM",font = ("Times new roman",35,"bold"),bg = "White",fg = "Darkgreen" )
        title_lbl.place(x=0,y=0,width=1500,height=45)

        main_frame = Frame(bg_img,bd=2,bg= "White")
        main_frame.place(x=15,y=55,width=1400,height=700)

        #left label frame
        Left_frame = LabelFrame(main_frame,bd=2,bg="White",relief=RIDGE,text="Employee Details",font = ("Times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=650,height=565)

        img_left = Image.open(r"/Users/harshbhatt/Desktop/Face Recogition system/college_images/smart-attendance.jpg")
        img_left = img_left.resize((635,130),Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        
        f_lbl = Label(Left_frame ,image = self.photoimg_left)
        f_lbl.place(x=5,y=0,width = 635,height = 130)

        # current course
        current_course_frame = LabelFrame(Left_frame,bd=2,bg="White",relief=RIDGE,text="Current Employee Information",font = ("Times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=635,height=125)

        # Department
        dep_label = Label(current_course_frame,text="Department",font = ("Times new roman",12,"bold"),bg="White")
        dep_label.grid(row=0,column=0,padx=35)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep,font = ("Times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"] = ("Select Department","Analysis","Admin","Support","Computer expert")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        # Course (Type of work)
        work_label = Label(current_course_frame,text="Work Type",font = ("Times new roman",12,"bold"),bg="White")
        work_label.grid(row=0,column=2,padx=35,sticky =W)

        work_combo = ttk.Combobox(current_course_frame,textvariable=self.var_work ,font = ("Times new roman",12,"bold"),width=17,state="readonly")
        work_combo["values"] = ("Select Work","Field work","Computer work","Management","Hardware support")
        work_combo.current(0)
        work_combo.grid(row=0,column=3,padx=0,pady=10,sticky =W)

        # Year
        year_label = Label(current_course_frame,text="Year",font = ("Times new roman",12,"bold"),bg="White")
        year_label.grid(row=1,column=0,padx=35,sticky =W)

        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year ,font = ("Times new roman",12,"bold"),width=17,state="readonly")
        year_combo["values"] = ("Select Year","2020-2021","2021-2022","2022-2023","2023-2024")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky =W)

        # Experience
        exp_label = Label(current_course_frame,text="Experience",font = ("Times new roman",12,"bold"),bg="White")
        exp_label.grid(row=1,column=2,padx=35,sticky =W)

        exp_combo = ttk.Combobox(current_course_frame,textvariable=self.var_exp ,font = ("Times new roman",12,"bold"),width=17,state="readonly")
        exp_combo["values"] = ("Select Experience","1-Year","2-Year","3-Year","4-Year")
        exp_combo.current(0)
        exp_combo.grid(row=1,column=3,padx=2,pady=10,sticky =W)

        # Class Employee information
        employee_frame = LabelFrame(Left_frame,bd=2,bg="White",relief=RIDGE,text="Employee Information",font = ("Times new roman",12,"bold"))
        employee_frame.place(x=5,y=265,width=635,height=290)

        #employee id
        employeeID_label = Label(employee_frame,text="Employee ID:",font = ("Times new roman",12,"bold"),bg="White")
        employeeID_label.grid(row=0,column=0,padx=10,pady=5,sticky =W)

        employeeId_entry = ttk.Entry(employee_frame,textvariable=self.var_employeeID,width=20,font = ("Times new roman",12,"bold"))
        employeeId_entry.grid(row=0,column=1,padx=10,pady=5,sticky =W)

        #employee name
        employeeName_label = Label(employee_frame,text="Employee Name:",font = ("Times new roman",12,"bold"),bg="White")
        employeeName_label.grid(row=0,column=2,padx=10,pady=5,sticky =W)

        employeeName_entry = ttk.Entry(employee_frame, textvariable=self.var_employeeName,width=20,font = ("Times new roman",12,"bold"))
        employeeName_entry.grid(row=0,column=3,padx=10,pady=5,sticky =W)

        #Employee Email Id
        employeeEmailID_label = Label(employee_frame,text="Employee EmailID:",font = ("Times new roman",12,"bold"),bg="White")
        employeeEmailID_label.grid(row=1,column=0,padx=10,pady=5,sticky =W)

        employeeEmailId_entry = ttk.Entry(employee_frame,textvariable=self.var_employeeEmailID, width=20,font = ("Times new roman",12,"bold"))
        employeeEmailId_entry.grid(row=1,column=1,padx=10,pady=5,sticky =W)

        #employee contact number
        employeeContact_label = Label(employee_frame,text="Phone no.:",font = ("Times new roman",12,"bold"),bg="White")
        employeeContact_label.grid(row=1,column=2,padx=10,pady=5,sticky =W)

        employeeContact_entry = ttk.Entry(employee_frame,textvariable=self.var_employeeContact,width=20,font = ("Times new roman",12,"bold"))
        employeeContact_entry.grid(row=1,column=3,padx=10,pady=5,sticky =W)

        #Gender
        employeeGen_label = Label(employee_frame,text="Gender:",font = ("Times new roman",12,"bold"),bg="White")
        employeeGen_label.grid(row=2,column=2,padx=10,pady=5,sticky =W)

        #employeeGen_entry = ttk.Entry(employee_frame,textvariable=self.var_employeeGen, width=20,font = ("Times new roman",12,"bold"))
        #employeeGen_entry.grid(row=2,column=3,padx=10,pady=5,sticky =W)
        employeeGen_combo = ttk.Combobox(employee_frame,textvariable=self.var_employeeGen ,font = ("Times new roman",12,"bold"),width=17,state="readonly")
        employeeGen_combo["values"] = ("Male","Female","other")
        employeeGen_combo.current(0)
        employeeGen_combo.grid(row=2,column=3,padx=10,pady=5,sticky =W)

        #Home number
        employeeNum_label = Label(employee_frame,text="Home Contact:",font = ("Times new roman",12,"bold"),bg="White")
        employeeNum_label.grid(row=2,column=0,padx=10,pady=5,sticky =W)

        employeeNum_entry = ttk.Entry(employee_frame,textvariable=self.var_employeeNum, width=20,font = ("Times new roman",12,"bold"))
        employeeNum_entry.grid(row=2,column=1,padx=10,pady=5,sticky =W)

        # Salary
        employeeSal_label = Label(employee_frame,text="Salary:",font = ("Times new roman",12,"bold"),bg="White")
        employeeSal_label.grid(row=3,column=0,padx=10,pady=5,sticky =W)

        employeeSal_entry = ttk.Entry(employee_frame,textvariable=self.var_employeeSal, width=20,font = ("Times new roman",12,"bold"))
        employeeSal_entry.grid(row=3,column=1,padx=10,pady=5,sticky =W)

        #Address
        employeeAdd_label = Label(employee_frame,text="Address:",font = ("Times new roman",12,"bold"),bg="White")
        employeeAdd_label.grid(row=3,column=2,padx=10,pady=5,sticky =W)

        employeeAdd_entry = ttk.Entry(employee_frame, textvariable=self.var_employeeAdd,width=20,font = ("Times new roman",12,"bold"))
        employeeAdd_entry.grid(row=3,column=3,padx=10,pady=5,sticky =W)

        #Date of birth
        employeeDOB_label = Label(employee_frame,text="DOB:",font = ("Times new roman",12,"bold"),bg="White")
        employeeDOB_label.grid(row=4,column=0,padx=10,pady=5,sticky =W)

        employeeDOB_entry = ttk.Entry(employee_frame,textvariable=self.var_employeeDOB, width=20,font = ("Times new roman",12,"bold"))
        employeeDOB_entry.grid(row=4,column=1,padx=10,pady=5,sticky =W)
        
        #Branch
        employeeB_label = Label(employee_frame,text="Branch:",font = ("Times new roman",12,"bold"),bg="White")
        employeeB_label.grid(row=4,column=2,padx=10,pady=5,sticky =W)

        employeeB_entry = ttk.Entry(employee_frame,textvariable=self.var_employeeB, width=20,font = ("Times new roman",12,"bold"))
        employeeB_entry.grid(row=4,column=3,padx=10,pady=5,sticky =W)

        # Radio button
        self.var_radio1 = StringVar()
        radiobtn1=ttk.Radiobutton(employee_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)

        self.var_radio2 = StringVar()
        radiobtn1=ttk.Radiobutton(employee_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn1.grid(row=6,column=1)

        # button frame
        btn_frame=Frame(employee_frame,bd=2,relief=RIDGE,bg="Blue")
        btn_frame.place(x=0,y=200,width=680,height=35)
        
        save_btn = Button(btn_frame,text="Save",command=self.add_data,width=18,font = ("Times new roman",12,"bold"),bg="blue",fg="Blue")
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame,text="Update",command=self.update_data,width=18,font = ("Times new roman",12,"bold"),bg="blue",fg="Blue")
        update_btn.grid(row=0,column=1)

        delete_btn = Button(btn_frame,text="Delete",command=self.delete_data,width=18,font = ("Times new roman",12,"bold"),bg="blue",fg="Blue")
        delete_btn.grid(row=0,column=2)

        reset_btn = Button(btn_frame,text="Reset",command=self.reset_data,width=18,font = ("Times new roman",12,"bold"),bg="blue",fg="Blue")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(employee_frame,bd=2,relief=RIDGE,bg="White")
        btn_frame1.place(x=0,y=230,width=680,height=35)

        take_photo_btn = Button(btn_frame1,text="Take Photo Sample",command = self.generate_dataset,width=36,font = ("Times new roman",12,"bold"),bg="blue",fg="Blue")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn = Button(btn_frame1,text="Take Photo Sample",width=36,font = ("Times new roman",12,"bold"),bg="blue",fg="Blue")
        update_photo_btn.grid(row=0,column=1)
               
        
 

        # Right label frame
        Right_frame = LabelFrame(main_frame,bd=2,bg="White",relief=RIDGE,text="Employee Details",font =("Times new roman",12,"bold"))
        Right_frame.place(x=675,y=10,width=650,height=565)

        img_right = Image.open(r"/Users/harshbhatt/Desktop/Face Recogition system/college_images/student.jpg")
        img_right = img_right.resize((635,130),Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        
        f_lbl = Label(Right_frame ,image = self.photoimg_right)
        f_lbl.place(x=5,y=0,width = 635,height = 130)

        
        #========================Search System=====================
        search_frame = LabelFrame(Right_frame,bd=2,bg="White",relief=RIDGE,text="Search System",font = ("Times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=635,height=70)

        search_label = Label(search_frame,text="Search By:",font = ("Times new roman",12,"bold"),bg="Red",fg="White")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky =W)

        search_combo = ttk.Combobox(search_frame, font = ("Times new roman",12,"bold"),width=17,state="readonly")
        search_combo["values"] = ("Select","Employee_id","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky =W)    

        search_entry = ttk.Entry(search_frame, width=13,font = ("Times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky =W) 

        search_btn = Button(search_frame,text="Search",width=14,font = ("Times new roman",12,"bold"),bg="white",fg="blue")
        search_btn.grid(row=0,column=3)

        ShowAll_btn = Button(search_frame,text="Show All",width=14,font = ("Times new roman",12,"bold"),bg="white",fg="blue")
        ShowAll_btn.grid(row=0,column=4,padx=5)

        #==========================Table Frame========================
        table_frame = Frame(Right_frame,bd=2,bg="White",relief=RIDGE)
        table_frame.place(x=5,y=210,width=635,height=350)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employee_table = ttk.Treeview(table_frame,column=("dep","Work Type","Year","Experience","Employee ID","Employee Name","Employee EmailID","Phone no.","Home Contact","Gender","Salary","Address","DOB","Branch","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading("dep",text="Department")
        self.employee_table.heading("Work Type",text="Work Type")
        self.employee_table.heading("Year",text="Year")
        self.employee_table.heading("Experience",text="Experience")
        self.employee_table.heading("Employee ID",text="Employee ID")
        self.employee_table.heading("Employee Name",text="Employee Name")
        self.employee_table.heading("Employee EmailID",text="Employee EmailID")
        self.employee_table.heading("Phone no.",text="Phone no.")
        self.employee_table.heading("Home Contact",text="Home Contact")
        self.employee_table.heading("Gender",text="Gender")
        self.employee_table.heading("Salary",text="Salary")
        self.employee_table.heading("Address",text="Address")
        self.employee_table.heading("DOB",text="Date Of Birth")
        self.employee_table.heading("Branch",text="Branch")
        self.employee_table.heading("Photo",text="PhotoSampleStatus")
        self.employee_table["show"]="headings"

        self.employee_table.column("dep",width=100)
        self.employee_table.column("Work Type",width=100)
        self.employee_table.column("Year",width=100)
        self.employee_table.column("Experience",width=100)
        self.employee_table.column("Employee ID",width=100)
        self.employee_table.column("Employee Name",width=100)
        self.employee_table.column("Employee EmailID",width=120)
        self.employee_table.column("Phone no.",width=100)
        self.employee_table.column("Home Contact",width=100)
        self.employee_table.column("Gender",width=100)
        self.employee_table.column("Salary",width=100)
        self.employee_table.column("Address",width=100)
        self.employee_table.column("DOB",width=100)
        self.employee_table.column("Branch",width=100)
        self.employee_table.column("Photo",width=150)
        
        self.employee_table.pack(fill=BOTH,expand=1)
        '''
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        '''

    #========================Function Declaration===========================

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_employeeName.get()=="" or self.var_employeeID.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="13055Don@",database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                            self.var_dep.get(),
                            self.var_work.get(),
                            self.var_year.get(),
                            self.var_exp.get(),
                            self.var_employeeID.get(),
                            self.var_employeeName.get(),
                            self.var_employeeEmailID.get(),
                            self.var_employeeContact.get(),
                            self.var_employeeGen.get(),
                            self.var_employeeNum.get(),
                            self.var_employeeSal.get(),
                            self.var_employeeAdd.get(),
                            self.var_employeeDOB.get(),
                            self.var_employeeB.get(),
                            self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Employee details has been added successfully!!!",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #====================Fetch data=========================
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="13055Don@",database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from employee")
        data = my_cursor.fetchall()

        if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())

            for i in data:
                self.employee_table.insert("",END,values=i)

            conn.commit()
        conn.close()

    #======================get cursor=========================
    def get_cursor(self,event=""):
        cursor_focus = self.employee_table.focus()
        content = self.employee_table.item(cursor_focus)
        data = content["values"]
        self.var_dep.set(data[0]),
        self.var_work.set(data[1]),
        self.var_year.set(data[2]),
        self.var_exp.set(data[3]),
        self.var_employeeID.set(data[4]),
        self.var_employeeName.set(data[5]),
        self.var_employeeEmailID.set(data[6]),
        self.var_employeeContact.set(data[7]),
        self.var_employeeGen.set(data[8]),
        self.var_employeeNum.set(data[9]),
        self.var_employeeSal.set(data[10]),
        self.var_employeeAdd.set(data[11]),
        self.var_employeeDOB.set(data[12]),
        self.var_employeeB.set(data[13]),
        self.var_radio1.set(data[14])

    #==============Update function===============
    def update_data(self,event=""):
        if self.var_dep.get()=="Select Department" or self.var_employeeName.get()=="" or self.var_employeeID.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        
        else:
            try:
                Update = messagebox.askyesno("Update","Do you want to update this employee details",parent=self.root)
                if Update>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="13055Don@",database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update employee set Dep=%s,Work_Type=%s,Year=%s,Experience=%s,EmployeeName=%s,EmployeeEmailId=%s,EmployeeContact=%s,EmployeeGen=%s,EmployeeNumber=%s,Salary=%s,Address=%s,DOB=%s,Branch=%s,Photosample=%s where EmployeeId=%s",(
                            self.var_dep.get(),
                            self.var_work.get(),
                            self.var_year.get(),
                            self.var_exp.get(),
                            self.var_employeeName.get(),
                            self.var_employeeEmailID.get(),
                            self.var_employeeContact.get(),
                            self.var_employeeGen.get(),
                            self.var_employeeNum.get(),
                            self.var_employeeSal.get(),
                            self.var_employeeAdd.get(),
                            self.var_employeeDOB.get(),
                            self.var_employeeB.get(),
                            self.var_radio1.get(),
                            self.var_employeeID.get()
                        ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Employee details successfully updated!!!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #======================Delete Function======================
    def delete_data(self):
        if self.var_employeeID.get()=="":
            messagebox.showerror("Error","EmployeeId must be required",parent=self.root)
        
        else:
            try:
                delete=messagebox.askyesno("Employee Delete page","Do you want to delete employee",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="13055Don@",database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql = "delete from employee where EmployeeId=%s"
                    val = (self.var_employeeID.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted employee details!!!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #=============Reset===============
    def reset_data(self):
        self.var_dep.set("Select department")
        self.var_work.set("Select Work"),
        self.var_year.set("Select Year"),
        self.var_exp.set("Select Experience"),
        self.var_employeeName.set(""),
        self.var_employeeEmailID.set(""),
        self.var_employeeContact.set(""),
        self.var_employeeGen.set("Male"),
        self.var_employeeNum.set(""),
        self.var_employeeSal.set(""),
        self.var_employeeAdd.set(""),
        self.var_employeeDOB.set(""),
        self.var_employeeB.set(""),
        self.var_radio1.set(""),
        self.var_employeeID.set("")


    #======================= Generate  data set  Take  photo samples ====================
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_employeeName.get()=="" or self.var_employeeID.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="13055Don@",database="face_recognizer")
                my_cursor = conn.cursor()   
                my_cursor.execute("select * from employee")
                myresult = my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update employee set Dep=%s,Work_Type=%s,Year=%s,Experience=%s,EmployeeName=%s,EmployeeEmailId=%s,EmployeeContact=%s,EmployeeGen=%s,EmployeeNumber=%s,Salary=%s,Address=%s,DOB=%s,Branch=%s,Photosample=%s where EmployeeId=%s",(
                            self.var_dep.get(),
                            self.var_work.get(),
                            self.var_year.get(),
                            self.var_exp.get(),
                            self.var_employeeName.get(),
                            self.var_employeeEmailID.get(),
                            self.var_employeeContact.get(),
                            self.var_employeeGen.get(),
                            self.var_employeeNum.get(),
                            self.var_employeeSal.get(),
                            self.var_employeeAdd.get(),
                            self.var_employeeDOB.get(),
                            self.var_employeeB.get(),
                            self.var_radio1.get(),
                            self.var_employeeID.get()==id+1
                        ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #==================Load predefined data on face frontals from opencv==============

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_croped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)

                    for (x,y,w,h) in faces:
                        face_croped=img[y:y+h,x:x+w]
                        return face_croped
                  
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret,my_frame = cap.read()
                    if face_croped(my_frame) is not None:
                        img_id+=1
                        face =cv2.resize(face_croped(my_frame),(450,450))
                        face =cv2.cvtColor(face,cv2.COLOR_BGR2GRAY) #gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        file_name_path ="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("cropped Face",face)

                    if cv2.waitKey(1)==13 or int (img_id)==100:
                        break
                
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!")   
        
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)






    
        


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()