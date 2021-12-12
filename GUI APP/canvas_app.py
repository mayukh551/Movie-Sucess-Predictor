from tkinter import *
from PIL import ImageTk, Image


def btn_clicked():
    pw_entry.config(show="Done")


root = Tk()
root.title('FuckOFF!!')
root.geometry('500x500')

# Define Background Image
bg = ImageTk.PhotoImage(file="meditation.jpg")

# Define Canvas
myCanvas = Canvas(root, width=500, height=500, bd=0, highlightthickness=0)
myCanvas.pack(fill="both", expand=True)

# Put image on canvas
myCanvas.create_image(0, 0, image=bg, anchor="nw")

# Define Entry boxes
un_entry = Entry(root, font=("Roboto", 20), width=14, fg="#336d92", bd=0)
pw_entry = Entry(root, font=("Roboto", 20), width=14, fg="#336d92", bd=0)

# Add entry boxes to canvas
un_window = myCanvas.create_window(34, 290, anchor="nw", window=un_entry)
pw_window = myCanvas.create_window(34, 290, anchor="nw", window=pw_entry)

# Define Button
login_btn = Button(root, text="Login", font=("Roboto", 20), width=15, fg="#336d92", command=btn_clicked)
login_btn_window = myCanvas.create_window(36, 470, anchor="nw", window=login_btn)

# output = Entry(root, font=("Roboto", 20), width=14, fg="#336d92", bd=0)

un_entry.insert(0, "username")
pw_entry.insert(0, "password")

root.mainloop()
