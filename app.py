from tkinter import *

# Create Window object
app = Tk()

app.title('Part Time Manager')
app.geometry('700x500')

#  Label : First Name
label1 = Label(app, text="First Name", font=('bold', 14), pady=14, padx=14)
label1.grid(row=0, column=0)
text1 = StringVar()
entry1 = Entry(app, textvariable=text1)
entry1.grid(row=0, column=1)

#  Label : Last Name
label2 = Label(app, text="Last Name", font=('bold', 14), pady=14, padx=14)
label2.grid(row=0, column=2)
text2 = StringVar()
entry2 = Entry(app, textvariable=text2)
entry2.grid(row=0, column=3)

#  Label : movie
movie_label = Label(app, text="Enter Movie Name", font=('bold', 14), padx=24)
movie_label.grid(row=1, column=0)
movie_text = StringVar()
movie_entry = Entry(app, textvariable=movie_text)
movie_entry.grid(row=1, column=1)

#  Label : User's Rating
user_label = Label(app, text="Your Rating", font=('bold', 14), padx=24)
user_label.grid(row=2, column=0)
user_text = StringVar()
user_entry = Entry(app, textvariable=user_text)
user_entry.grid(row=2, column=1)


# Start Program
app.mainloop()
