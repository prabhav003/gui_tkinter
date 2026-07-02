from tkinter import *
from PIL import ImageTk,Image
import os

def rotate_image():
    global counter
    img_label.config(image=img_arr[counter%len(img_arr)])
    counter = counter = counter+1


counter = 1
root = Tk()

root.title('image viewer')
root.geometry('600x400')
root.configure(background='black')

files = os.listdir('images')
# print(files)

img_arr = []
for file in files:
    img = Image.open(os.path.join('images',file))
    resized_img = img.resize((300,300))
    img_arr.append(ImageTk.PhotoImage(resized_img))

img_label = Label(root,image=img_arr[0])
img_label.pack(pady=(15,10))

next_btn = Button(root,text='Next',bg='white',fg='black',width=28,height=2,command=rotate_image)
next_btn.pack()





root.mainloop()