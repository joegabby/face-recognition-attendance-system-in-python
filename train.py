from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
        def __init__(self,root):
                self.root=root
                self.root.geometry("1530x790+0+0")
                self.root.title("Train Data")

                header = Label(self.root, text="TRAIN DATA", font=("verdana",20,"bold"),bg="blue",fg="white",padx=50,pady=80)
                header.place(x=0,y=0,width=1370,height=50)

                main_frame= Frame(self.root,bd=0,bg="lightgrey")
                main_frame.place(x=50,y=50,width=1265,height=650)
# train data button
                img2=Image.open(r"images\student.png")
                img2=img2.resize((100,100),Image.ANTIALIAS)
                self.photoimg2=ImageTk.PhotoImage(img2)

                btn2_1=Button(main_frame,command=self.train_classifier,image=self.photoimg2,cursor="hand2",bd=0)
                btn2_1.place(x=500,y=100,width=200,height=200)

                btn2_2=Button(main_frame,command=self.train_classifier,text="Train Data",cursor="hand2",font=("verdana"),bg="blue",fg="white",padx=50,pady=80,bd=0)
                btn2_2.place(x=500,y=300,width=200,height=30)

# ==================functions=======================
        def train_classifier(self):
            data_dir=("data")
            path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

            faces=[]
            ids=[]

            for image in path:
                img=Image.open(image).convert('L') #grey scale image
                imageNp=np.array(img,'uint8')
                id=int(os.path.split(image)[1].split('.')[1])

                faces.append(imageNp)
                ids.append(id)
                cv2.imshow("Training",imageNp)
                cv2.waitKey(1)==13
            ids=np.array(ids)

    # =======================train the classifier and save=========================
            clf=cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces,ids)
            clf.write("classifier.xml")
            cv2.destroyAllWindows()
            messagebox.showinfo("Result","Datasets trained successfully!!!")
                



if __name__ == "__main__":
    
        root=Tk()
        obj=Train(root)
        root.mainloop()
