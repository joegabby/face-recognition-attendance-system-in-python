from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os.path
class Student:
        def __init__(self,root):
                self.root=root
                self.root.geometry("1530x790+0+0")
                self.root.title("Student Registration")
                # =============variables=================
                self.var_dep=StringVar()
                self.var_matNo=StringVar()
                self.var_name=StringVar()
                self.var_gender=StringVar()
                self.var_dob=StringVar()
                self.var_email=StringVar()
                self.var_phone=StringVar()
                self.var_level=StringVar()
                self.var_query=StringVar()
                
                header = Label(self.root, text="STUDENTS PORTAL", font=("verdana",20,"bold"),bg="blue",fg="white",padx=50,pady=80)
                header.place(x=0,y=0,width=1370,height=50)

                main_frame= Frame(self.root,bd=0,bg="#f1f1f1")
                main_frame.place(x=50,y=50,width=1265,height=650)

                left_frame= LabelFrame(main_frame,bd=1,bg="white",relief=RIDGE, text="Student Registeration",font=("verdana",10))
                left_frame.place(x=50,y=50,width=640,height=550)
                
                current_course_frame= LabelFrame(left_frame,bd=1,bg="white",relief=RIDGE, text="Current course",font=("verdana",10),padx=10,pady=10)
                current_course_frame.place(x=10,y=10,width=620,height=130)
        # department
                # dept_label=Label(current_course_frame,text="Department",font=("verdana",10),bg="white")
                # dept_label.grid(row=0,column=0)

                # dept_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("verdana",10),state="readonly")
                # dept_combo["values"]=("Select Department","Computer Science","Physics","Chemistry")
                # dept_combo.current(0)
                # dept_combo.grid(row=0,column=1,padx=10,pady=10,sticky=W)
        # course
                # course_label=Label(current_course_frame,text="Course",font=("verdana",10),bg="white")
                # course_label.grid(row=0,column=2)

                # course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course, font=("verdana",10),state="readonly")
                # course_combo["values"]=("Select Course","CMP 411","CMP 412","CMP 413")
                # course_combo.current(0)
                # course_combo.grid(row=0,column=3,padx=10,pady=10,sticky=W)
                
        # Year
                # year_label=Label(current_course_frame,text="Year",font=("verdana",10),bg="white")
                # year_label.grid(row=1,column=0,padx=10,sticky=W)

                # year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("verdana",10),state="readonly")
                # year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
                # year_combo.current(0)
                # year_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)
                
        # Semester
                # year_label=Label(current_course_frame,text="Semester",font=("verdana",10),bg="white")
                # year_label.grid(row=1,column=2,padx=10,sticky=W)

                # year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("verdana",10),state="readonly")
                # year_combo["values"]=("Select Semester","First Semester","Second Semester")
                # year_combo.current(0)
                # year_combo.grid(row=1,column=3,padx=10,pady=10,sticky=W)
        # students personal information
                students_info_frame= LabelFrame(left_frame,bd=1,bg="white",relief=RIDGE, text="Students Information",font=("verdana",10),padx=10,pady=10)
                students_info_frame.place(x=10,y=150,width=620,height=370)
                # name
                Student_name= Label(students_info_frame,text="Full Name:",bg="white",font=("verdana",10))
                Student_name.grid(row=0,column=0,padx=10,pady=10,sticky=W)
                
                Student_name_entry=ttk.Entry(students_info_frame,textvariable=self.var_name, width=20,font=("verdana",10))
                Student_name_entry.grid(row=0,column=1)
                # matric number
                Student_mat_number= Label(students_info_frame,text="Matric number:",bg="white",font=("verdana",10))
                Student_mat_number.grid(row=0,column=2,padx=20,pady=10,sticky=W)

                Student_mat_number_entry=ttk.Entry(students_info_frame,textvariable=self.var_matNo, width=20,font=("verdana",10))
                Student_mat_number_entry.grid(row=0,column=3)
                # gender
                Student_gender= Label(students_info_frame,text="Gender:",bg="white",font=("verdana",10))
                Student_gender.grid(row=1,column=0,padx=20,pady=10,sticky=W)

                Student_gender_entry=ttk.Combobox(students_info_frame,textvariable=self.var_gender, width=18,font=("verdana",10),state="readonly")
                Student_gender_entry["values"]=("Select Gender","Male","Female")
                Student_gender_entry.current(0)
                Student_gender_entry.grid(row=1,column=1)
                # Email
                Student_email= Label(students_info_frame,text="Email:",bg="white",font=("verdana",10))
                Student_email.grid(row=1,column=2,padx=20,pady=10,sticky=W)

                Student_email_entry=ttk.Entry(students_info_frame,textvariable=self.var_email, width=20,font=("verdana",10))
                Student_email_entry.grid(row=1,column=3)
                # phone
                Student_phone= Label(students_info_frame,text="Phone:",bg="white",font=("verdana",10))
                Student_phone.grid(row=2,column=0,padx=20,pady=10,sticky=W)

                Student_phone_entry=ttk.Entry(students_info_frame,textvariable=self.var_phone, font=("verdana",10))
                Student_phone_entry.grid(row=2,column=1)
                # DOB
                Student_DOB= Label(students_info_frame,text="DOB:",bg="white",font=("verdana",10))
                Student_DOB.grid(row=2,column=2,padx=20,pady=10,sticky=W)

                Student_DOB_entry=ttk.Entry(students_info_frame,textvariable=self.var_dob, width=20,font=("verdana",10))
                Student_DOB_entry.grid(row=2,column=3)
                # level
                Student_level= Label(students_info_frame,text="Level:",bg="white",font=("verdana",10))
                Student_level.grid(row=3,column=0,padx=20,pady=10,sticky=W)

                Student_level_entry=ttk.Combobox(students_info_frame,textvariable=self.var_level, width=18,font=("verdana",10),state="readonly")
                Student_level_entry["values"]=("Select Level","100","200","300","400")
                Student_level_entry.current(0)
                Student_level_entry.grid(row=3,column=1)
                # department
                dept_label=Label(students_info_frame,text="Department:",bg="white",font=("verdana",10))
                dept_label.grid(row=3,column=2,padx=20,pady=10,sticky=W)

                dept_combo=ttk.Combobox(students_info_frame,width=18,textvariable=self.var_dep,font=("verdana",10),state="readonly")
                dept_combo["values"]=("Select Department","Computer Science","Physics","Chemistry")
                dept_combo.current(0)
                dept_combo.grid(row=3,column=3,sticky=W)
                # radio buttons
                # self.var_radiobtn1=StringVar()
                # radiobtn1=ttk.Radiobutton(students_info_frame,variable=self.var_radiobtn1,text="Take Photo Sample",value="Yes")
                # radiobtn1.grid(row=3,column=1,pady=20)

                # radiobtn2=ttk.Radiobutton(students_info_frame,variable=self.var_radiobtn1,text="No Photo Sample",value="No")
                # radiobtn2.grid(row=3,column=2,pady=20)
        # button container
                action_button_frame= LabelFrame(left_frame,bd=1,bg="white",relief=RIDGE, text="Actions",font=("verdana",10),padx=5,pady=10)
                action_button_frame.place(x=10,y=420,width=620,height=100)
                # save button
                save_btn=Button(action_button_frame,command=self.add_data, text="Save",bd=1,cursor="hand2",font=("verdana",10),bg="blue",fg="white",width=18)
                save_btn.grid(row=0,column=1)
                # update button
                update_btn=Button(action_button_frame,command=self.update_data,text="Update",bd=1,cursor="hand2",font=("verdana",10),bg="blue",fg="white",width=18)
                update_btn.grid(row=0,column=2)
                # delete button
                delete_btn=Button(action_button_frame,command=self.delete_data,text="Delete",bd=1,cursor="hand2",font=("verdana",10),bg="blue",fg="white",width=18)
                delete_btn.grid(row=0,column=3)
                # reset button
                reset_btn=Button(action_button_frame,command=self.reset_data,text="Reset",bd=1,cursor="hand2",font=("verdana",10),bg="blue",fg="white",width=18)
                reset_btn.grid(row=0,column=4)
                # inner action btn
                action_button_frame1= LabelFrame(action_button_frame,bd=0,bg="white",relief=RIDGE,font=("verdana",10))
                action_button_frame1.place(x=0,y=30)
                # Take photo button
                # take_photo_btn=Button(action_button_frame1,command=self.generate_dataset,text="Take Photo",bd=1,cursor="hand2",font=("verdana",10),bg="blue",fg="white",width=37)
                # take_photo_btn.grid(row=0,column=0)
                # Update photo button
                update_photo_btn=Button(action_button_frame1,command=self.update_photo,text="Update Photo",bd=1,cursor="hand2",font=("verdana",10),bg="blue",fg="white",width=37)
                update_photo_btn.grid(row=0,column=0,pady=0)
        # right frame
                right_frame= LabelFrame(main_frame,bd=1,bg="white",relief=RIDGE, text="Student Details",font=("verdana",10),padx=10,pady=10)
                right_frame.place(x=700,y=50,width=500,height=550)
                # search frame
                search_frame= LabelFrame(right_frame,bd=1,bg="white",padx=50,relief=RIDGE, text="Search",font=("verdana",10))
                search_frame.place(x=0,y=0,width=480,height=50)
                # search by
                # Search_combo_label= Label(search_frame,text="Search By:",bg="white",font=("verdana",10))
                # Search_combo_label.grid(row=0,column=0,padx=5,pady=0,sticky=W)

                # Search_combo_entry=ttk.Combobox(search_frame,width=10,font=("verdana",10),state="readonly")
                # Search_combo_entry["values"]=("Select","Matric Number","Name")
                # Search_combo_entry.current(0)
                # Search_combo_entry.grid(row=0,column=1)

                Search_entry=ttk.Entry(search_frame,textvariable=self.var_query,width=30,font=("verdana",10))
                Search_entry.grid(row=0,column=2,padx=2)

                search_btn=Button(search_frame,command=self.search,text="Search",bd=0,cursor="hand2",font=("verdana",10),bg="blue",fg="white",width=7)
                search_btn.grid(row=0,column=3)

                show_all_btn=Button(search_frame,command=self.fetch_data,text="Show All",bd=0,cursor="hand2",font=("verdana",10),bg="blue",fg="white",width=8)
                show_all_btn.grid(row=0,column=4,padx=2)

                # table frame
                table_frame= Frame(right_frame,bd=1,bg="white",relief=RIDGE)
                table_frame.place(x=0,y=60,width=480,height=450)

                scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
                scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

                self.student_table=ttk.Treeview(table_frame,columns=("matNo","name","gender","dob","email","phone","dep","level"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)
                scroll_x.config(command=self.student_table.xview)
                scroll_y.config(command=self.student_table.yview)

                self.student_table.heading("matNo",text="Matric")
                self.student_table.heading("name",text="Name")
                self.student_table.heading("gender",text="Gender")
                self.student_table.heading("dob",text="D.O.B")
                self.student_table.heading("email",text="E-mail")
                self.student_table.heading("phone",text="Phone")
                self.student_table.heading("dep",text="Department")
                self.student_table.heading("level",text="Level")
                self.student_table["show"]="headings"

                

                self.student_table.column("dep",width="100")
                self.student_table.column("level",width="100")
                self.student_table.column("matNo",width="100")
                self.student_table.column("name",width="100")
                self.student_table.column("gender",width="100")
                self.student_table.column("dob",width="100")
                self.student_table.column("email",width="100")
                self.student_table.column("phone",width="100")

                self.student_table.pack(fill=BOTH,expand=1)
                self.student_table.bind("<ButtonRelease>",self.get_cursor)
                self.fetch_data()

# ============================functions===================================

        def add_data(self):
                if self.var_dep.get()=="select Department" or self.var_name.get()=="" or self.var_matNo.get()=="" or self.var_gender.get()=="Select Gender":
                        messagebox.showerror("Error","All fields are required please",parent=self.root)
                else:
                        try:
                                conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_verification")
                                my_cursor=conn.cursor()
                                my_cursor.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                self.var_matNo.get(),
                                                                                                self.var_name.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_dob.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_phone.get(),
                                                                                                self.var_dep.get(),
                                                                                                self.var_level.get()
                                                                                                ))      
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                self.capture_face()
                                messagebox.showinfo("Succes","Student registered successfully",parent=self.root)
                        except Exception as es:
                                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

        def capture_face(self):
                cam = cv2.VideoCapture(0)
                
                self.db_dir ='./db'
                        
                if not os.path.exists(self.db_dir):
                        os.mkdir(self.db_dir)
                
                messagebox.showinfo("Succes","please position your face then hold the space bar for capturing",parent=self.root)
                while True:
                        ret,frame = cam.read()
                        if not ret:
                                print("failed to capture frame")
                                break
                        cv2.imshow("please position your face then hold the space bar for capturing",frame)
                        
                        k = cv2.waitKey(1)

                        user_name = self.var_name.get()

                        if k%256 == 32:
                                cv2.imwrite(os.path.join(self.db_dir,'{}.jpg'.format(user_name)),frame)
                                messagebox.showinfo("Succes","Frame captured successfully",parent=self.root)
                                break
                        
                cam.release()

                cv2.destroyAllWindows()
# ====================================== fetch data=====================================


        def fetch_data(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_verification")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from students order by name asc")
                data=my_cursor.fetchall()

                if len(data)!=0:
                        self.student_table.delete(*self.student_table.get_children())
                        for i in data:
                                self.student_table.insert("", END,values=i)
                        conn.commit()
                conn.close()

# ============================get cursor======================
        def get_cursor(self,event=""):
                cursor_focus=self.student_table.focus()
                content=self.student_table.item(cursor_focus)
                data=content["values"]

                self.var_matNo.set(data[0]),
                self.var_name.set(data[1]),
                self.var_gender.set(data[2]),
                self.var_dob.set(data[3]),
                self.var_email.set(data[4]),
                self.var_phone.set(data[5]),
                self.var_dep.set(data[6]),
                self.var_level.set(data[7])
                

# ===========================update function==========================
        def update_data(self):
                if self.var_dep.get()=="select Department" or self.var_name.get()=="" or self.var_matNo.get()=="" or self.var_gender.get()=="Select Gender":
                        messagebox.showerror("Error","All fields are required please",parent=self.root)
                else:
                        try:
                                Update=messagebox.askyesno("Update","Update details?",parent=self.root)
                                if Update>0:
                                        conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_verification")
                                        my_cursor=conn.cursor()
                                        
                                        my_cursor.execute("update students set name=%s,gender=%s,dob=%s,email=%s,phone=%s,department=%s,level=%s where matno=%s",(
                                                                                                
                                                                                                self.var_name.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_dob.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_phone.get(),
                                                                                                self.var_dep.get(),
                                                                                                self.var_level.get(),
                                                                                                self.var_matNo.get()
                                                                                                ))      
                                else:
                                        if not Update:
                                                return
                                messagebox.showinfo("Success","Updated successfully",parent=self.root)
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                        except Exception as es:
                                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

# ==========================Delete function=====================================================
        def delete_data(self):
                if self.var_matNo.get()=="":
                        messagebox.showerror("Error","No Matric Number",parent=self.root)
                else:
                        try:
                                delete=messagebox.askyesno("Delete","Delete entry?",parent=self.root)
                                if delete>0:
                                        conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_verification")
                                        my_cursor=conn.cursor()
                                        sql="delete from students where matNo=%s"
                                        val=(self.var_matNo.get(),)
                                        my_cursor.execute(sql,val)
                                else:
                                        if not delete:
                                                return
                                conn.commit()
                                self.fetch_data()
                                self.reset_data()
                                conn.close()
                                messagebox.showinfo("Delete","Deleted Successfully",parent=self.root)
                        except Exception as es:
                                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                    
                            
# =============================reset===================================
        def reset_data(self):
                self.var_matNo.set(""),
                self.var_name.set(""),
                self.var_gender.set("Select Gender"),
                self.var_dob.set(""),
                self.var_email.set(""),
                self.var_phone.set(""),
                self.var_dep.set("Select Department"),
                self.var_level.set("Select Level")
               

# ==============update photo===================
        def update_photo(self):
                if self.var_dep.get()=="select Department" or self.var_name.get()=="" or self.var_matNo.get()=="" or self.var_gender.get()=="Select Gender":
                        messagebox.showerror("Error","All fields are required please",parent=self.root)
                else:
                        try:
                            self.capture_face()    
                        except Exception as es:
                                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
        
# ==============search===================
        def search(self):
                query = self.var_query.get()
                if query=="" or query==" ":
                        messagebox.showerror("Error","Please type a query into the search box",parent=self.root)
                        self.fetch_data()
                else:
                        try:
                                conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_verification")
                                my_cursor=conn.cursor()
                                my_cursor.execute("select * from students where name like %s",(query,))
                                data=my_cursor.fetchall()
                        
                                if len(data)!=0:
                                        self.student_table.delete(*self.student_table.get_children())
                                        for i in data:
                                                self.student_table.insert("", END,values=i)
                                        conn.commit()
                                else:
                                         messagebox.showinfo("oops!!","nothing found",parent=self.root)
                                conn.close()    
                        except Exception as es:
                                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


if __name__ == "__main__":

        root=Tk()
        obj=Student(root)
        root.mainloop()



