from tkinter import *
from PIL import ImageTk, Image
from main import *
result = ""


# Display Output
def display(result):
    my_canvas.create_text(650, 250, text=result, font=("Exo 2", 30), fill="white")


# Function after Button is Clicked
def btn_clicked():
    print("Button Clicked")
    mov = input_mov.get()
    year = input_year.get()
    result = main_file_run(mov, year)
    print(result)
    display(result)


# Define entry_clear function
def entry_clear():
    input_mov.delete(0, END)
    input_year.delete(0, END)



window = Tk()
window.title('Movie Success Predictor')

window.geometry("805x560")

# Define Background Image
bg = ImageTk.PhotoImage(file="background.png")

# Define Output displaying area
# output_image = ImageTk.PhotoImage(file="output.png")

# Define Canvas
my_canvas = Canvas(
    window,
    bg="#000000",
    height=635,
    width=805,
    bd=0,
    highlightthickness=0)
my_canvas.pack(fill="both", expand=True)

# Put the image on the canvas
my_canvas.create_image(0,0, image=bg, anchor="nw")

# Text Message
my_canvas.create_text(160,70, text="Enter Movie Name :", font=("Times",22), fill="white")
my_canvas.create_text(180,190, text="Enter Year of Release :", font=("Ubuntu", 20), fill="white")

# Define entry boxes
input_mov = Entry(window, font=("Helvetica", 20), width=40, bg="#ade5f1", bd=0)
input_year = Entry(window, font=("Helvetica", 24), width=15, bg="#ade5f1", bd=0)

# Add the entry boxes to the canvas
mov_window = my_canvas.create_window(34,100, anchor="nw", window=input_mov)
year_window = my_canvas.create_window(34,220, anchor="nw", window=input_year)

#  Define Predict Button
btn1 = Button(
    window,
    text="Predict",
    font=("Times", 20),
    width=15,
    bg="#ade5f1",
    command=btn_clicked)
btn1_window = my_canvas.create_window(36,350, anchor="nw", window=btn1)

# Define Clear Button
btn2 = Button(
    window,
    text="Clear",
    font=("Helvetica", 15),
    width=15,
    bg="red",
    command=entry_clear)
btn2_window = my_canvas.create_window(65,430, anchor="nw", window=btn2)


window.resizable(False, False)
window.mainloop()
