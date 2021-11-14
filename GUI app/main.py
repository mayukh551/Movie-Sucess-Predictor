from tkinter import *

#create window object
app=Tk()

app.title('EDITH')
app.geometry('700x500')


#ID
ID_text=StringVar()
ID_label=Label(app, text='MOVIE PLUS', font=('bold',25),pady=20)
ID_label.grid(row=0, column=2,sticky=W)
