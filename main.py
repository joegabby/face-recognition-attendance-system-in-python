from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
from face_recog import Face_Recognition_module
from train import Train
import face_recognition
import cv2
import dlib
import util
import subprocess
import os
 
class Face_Recognition_System:
        def __init__(self,root):
                self.root=root
                self.root.geometry("1530x790+0+0")
                self.root.title("face Recognition System")
                
                header = Label(self.root, text="STUDENTS FACIAL RECOGNITION ATTENDANCE SYSTEM", font=("verdana",20,"bold"),bg="blue",fg="white")
                header.place(x=0,y=0,width=1370,height=50)

                main_frame= Frame(self.root,bd=0,bg="#f1f1f1")
                main_frame.place(x=50,y=50,width=1265,height=650)
        # btn1
                img1=Image.open(r"images\group_1.png")
                img1=img1.resize((196,245),Image.ANTIALIAS)
                self.photoimg1=ImageTk.PhotoImage(img1)        

                btn1=Button(main_frame,image=self.photoimg1,command=self.process_webcam,cursor="hand2",bd=0)
                btn1.place(x=100,y=200,width=196,height=245)

        # btn2
                img2=Image.open(r"images\group_2.png")
                img2=img2.resize((196,245),Image.ANTIALIAS)
                self.photoimg2=ImageTk.PhotoImage(img2)

                btn2_1=Button(main_frame,command=self.student_details,image=self.photoimg2,cursor="hand2",bd=0)
                btn2_1.place(x=400,y=200,width=196,height=245)

        # btn3
                img3=Image.open(r"images\group_3.png")
                img3=img3.resize((196,245),Image.ANTIALIAS)
                self.photoimg3=ImageTk.PhotoImage(img3)

                btn3_1=Button(main_frame,image=self.photoimg3,cursor="hand2",bd=0)
                btn3_1.place(x=700,y=200,width=196,height=245)
        # btn4
                img4=Image.open(r"images\group_4.png")
                img4=img4.resize((196,245),Image.ANTIALIAS)
                self.photoimg4=ImageTk.PhotoImage(img4)

                btn3_1=Button(main_frame,image=self.photoimg4,cursor="hand2",bd=0)
                btn3_1.place(x=1000,y=200,width=196,height=245)

                 
        # ========================= functions ========================
        def student_details(self):
                self.new_window=Toplevel(self.root)
                self.app=Student(self.new_window)
        # =========== train data =============== 
        # def open_image_folder(self):
        #         os.startfile("db")
                
        # =========== face recognizer =============== 
        def face_recognition(self):
                self.new_window=Toplevel(self.root)
                self.app=Face_Recognition(self.new_window)

# ==============login===========
        def add_webcam(self,label):
                
                
                self.process_webcam()

        def process_webcam(self):
                
                # self.new_window=Toplevel(self.root)
                # self.app=Face_Recognition(self.new_window)
                sfr = Face_Recognition_module(self.root)
                sfr.load_encoding_images("db/")

                # Load Camera
                cap = cv2.VideoCapture(0)


                while True:
                        ret, frame = cap.read()

                        # Detect Faces
                        face_locations, face_names = sfr.detect_known_faces(frame)
                        for face_loc, name in zip(face_locations, face_names):
                                y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

                                cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
                                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

                        cv2.imshow("Frame", frame)

                        key = cv2.waitKey(1)
                        if key == 27:
                                print('you just hit esc key!!!')

                                break
                                
                cap.release()
                cv2.destroyAllWindows()

                # ==================
        # def login(self):
        #         unknown_img_path = './.tmp.jpg'
        #         cv2.imwrite(unknown_img_path, self.most_recent_capture_arr)
        

        #         output = str(subprocess.check_output(['face_recognition', self.db_dir, unknown_img_path]))
        #         name = output.split(',')[1][:-5]

        #         if name in ['unknown_person', 'no_persons_found']:
        #                 util.msg_box('oopss!!', 'no registered user found please register or try again')
        #         else:
        #                 util.msg_box('success', 'welcome, {}'.format(name))
        #                 with open(self.log_path, 'a') as f:
        #                         f.write('{},{}\n'.format(name, datetime.datetime.now()))
        #                         f.close()
                
        #         print(name)
        #         os.remove(unknown_img_path)
                
        
if __name__ == "__main__":
    
        root=Tk()
        obj=Face_Recognition_System(root)
        root.mainloop()
