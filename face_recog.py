from tkinter import*
# import tkinter as tk
# from tkinter import ttk
import util
# import cv2
# from PIL import Image, ImageTk
# import os.path
# import datetime
# import face_recognition
# import dlib
# import subprocess
# import glob
# import mysql.connector
# from tkinter import messagebox
# import xlsxwriter
import face_recognition
import cv2
import os
import glob
import numpy as np
class Face_Recognition_module:
    def __init__(self,root):
        self.root=root
        # self.root.geometry("1530x790+0+0")
        # self.webcam_label = util.get_img_label(self.root)
        # self.webcam_label.place(x=350,y=10,width=700,height=500)

        self.known_face_encodings = []
        self.known_face_names = []
        # Resize frame for a faster speed
        self.frame_resizing = 0.25
        # self.login_button_main_window = util.get_button(self.root,'login','blue',self.login)
        # self.login_button_main_window.place(x=950,y=300)

        # sign_in_btn=Button(self.root,text="Sign in",bd=1,cursor="hand2",font=("verdana",20),bg="blue",fg="white",width=35)
        # sign_in_btn.place(x=400,y=550)

    def load_encoding_images(self, images_path):
        """
        Load encoding images from path
        :param images_path:
        :return:
        """
        # Load Images
        images_path = glob.glob(os.path.join(images_path, "*.*"))

        print("{} encoding images found.".format(len(images_path)))

        # Store image encoding and names
        for img_path in images_path:
            img = cv2.imread(img_path)
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Get the filename only from the initial file path.
            basename = os.path.basename(img_path)
            (filename, ext) = os.path.splitext(basename)
            # Get encoding
            img_encoding = face_recognition.face_encodings(rgb_img)[0]

            # Store file name and file encoding
            self.known_face_encodings.append(img_encoding)
            self.known_face_names.append(filename)
        print("Encoding images loaded")

    def detect_known_faces(self, frame):
        small_frame = cv2.resize(frame, (0, 0), fx=self.frame_resizing, fy=self.frame_resizing)
        # Find all the faces and face encodings in the current frame of video
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding, tolerance=0.5)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]
            face_names.append(name)

        # Convert to numpy array to adjust coordinates with frame resizing quickly
        face_locations = np.array(face_locations)
        face_locations = face_locations / self.frame_resizing
        return face_locations.astype(int), face_names
        # ======================================================
        # def draw_boundry(img,classifier,scaleFactor,minNeighbors,color,text,clf):
        #     gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #     features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

        #     coord=[]
        
        #     for(x,y,w,h) in features:
        #         cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
        #         id,predict=clf.predict(gray_image[y:y+h,x:x+w])
        #         confidence=int((100*(1-predict/300)))
            
        #         conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_verification")
        #         my_cursor=conn.cursor()
        #         # t= "2016/1/61010CT"
        #         my_cursor.execute("select name from students where matNo="+str(id))
        #         n=my_cursor.fetchone()
        #         # n="+".join(my_cursor.fetchone())

        #         my_cursor.execute("select matNo from students where matNo="+str(id))
        #         m=my_cursor.fetchone()
        #         # m="+".join(my_cursor.fetchone())

        #         my_cursor.execute("select department from students where matNo="+str(id))
        #         d=my_cursor.fetchone()
        #         # d="+".join(my_cursor.fetchone())

        #         if confidence>77:
        #             cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
        #             cv2.putText(img,f"Matric:{m}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
        #             cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
        #         else:
        #             cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
        #             cv2.putText(img,"Unknown face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

        #         coord=[x,y,w,h]

        #     return coord
        
        # def recognize(img,clf,faceCascade):
        #     coord=draw_boundry(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
        #     return img

        # faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        # clf=cv2.face.LBPHFaceRecognizer_create()
        # clf.read("classifier.xml")

        # video_cap=cv2.VideoCapture(0)

        # while True:
        #     ret,img=video_cap.read()
        #     img=recognize(img,clf,faceCascade)
        #     cv2.imshow("welcome to face detection",img)

        #     if cv2.waitKey(1)==13:
        #         break
            
        # video_cap.release()
        # cv2.destroyAllWindows()

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()