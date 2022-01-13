from tkinter import *
from PIL import ImageTk, Image
from main import *

result = ""

window = Tk()
window.title('Movie Success Predictor')

window.geometry("805x560")

# Define Background Image
bg = ImageTk.PhotoImage(file="background.png")

# Define Canvas
my_canvas = Canvas(
    window,
    bg="#000000",
    height=635,
    width=805,
    bd=0,
    highlightthickness=0)
my_canvas.pack(fill="both", expand=True)


# Remove Close Button
def hello():
    btn2.destroy()
    home()


# Define Close Button
def close():
    global btn2, btn2_window
    btn2 = Button(
        window,
        text="Search Another Movie",
        font=("Lucida Console", 15),
        width=22,
        fg="white",
        bg="green",
        command=hello)
    btn2_window = my_canvas.create_window(412, 310, window=btn2)


# Define entry_clear function to clear screen
def entry_clear():
    my_canvas.create_image(0, 0, image=bg, anchor="nw")
    input_mov.delete(0, END)
    input_year.delete(0, END)
    input_mov.destroy()
    input_year.destroy()
    btn1.destroy()
    close()


# Display Output
def display(result):
    entry_clear()
    if result == 'Super-Hit':
        my_canvas.create_text(410, 130, text=result, font=("Segoe UI", 35), fill="white")
        my_canvas.create_text(410, 180, text="8.5-10", font=("Segoe UI", 20), fill="white")
    elif result == 'Hit':
        my_canvas.create_text(410, 130, text=result, font=("Segoe UI", 35), fill="white")
        my_canvas.create_text(410, 180, text="7.8-8.5", font=("Segoe UI", 20), fill="white")
    elif result == 'Above Average':
        my_canvas.create_text(410, 130, text=result, font=("Segoe UI", 35), fill="white")
        my_canvas.create_text(410, 180, text="7-7.8", font=("Segoe UI", 20), fill="white")
    elif result == 'Average':
        my_canvas.create_text(410, 130, text=result, font=("Segoe UI", 35), fill="white")
        my_canvas.create_text(410, 180, text="6-7", font=("Segoe UI", 20), fill="white")
    elif result == 'Below Average':
        my_canvas.create_text(410, 130, text=result, font=("Segoe UI", 35), fill="white")
        my_canvas.create_text(410, 180, text="5-6", font=("Segoe UI", 20), fill="white")
    elif result == 'Flop':
        my_canvas.create_text(410, 130, text=result, font=("Segoe UI", 35), fill="white")
        my_canvas.create_text(410, 180, text="1-5", font=("Segoe UI", 20), fill="white")
    else:
        my_canvas.create_text(410, 150, text=result, font=("Segoe UI", 35), fill="white")


# Function after Predict Button is Clicked
def btn_clicked():
    mov = input_mov.get()
    year = input_year.get()
    result = main_file_run(mov, year)
    if '.' in result:
        # result stores imdb rating of the movie searched
        entry_clear()
        my_canvas.create_text(410, 115, text="Movie already released", font=("Segoe UI", 20), fill="white")
        my_canvas.create_text(410, 155, text="IMDb Rating", font=("Segoe UI", 20), fill="white")
        my_canvas.create_text(410, 185, text=result, font=("Segoe UI", 25), fill="white")
    else:
        # result stores the predicted rating of movie searched
        print(result)
        display(result)


# Displaying Home Page
def home():
    # Put the image on the canvas
    my_canvas.create_image(0, 0, image=bg, anchor="nw")

    # Text Message
    my_canvas.create_text(160, 70, text="Enter Movie Name :", font=("HP Simplified Hans", 20), fill="white")
    my_canvas.create_text(180, 190, text="Enter Year of Release :", font=("HP Simplified Hans", 20), fill="white")
    # my_canvas.create_text(600,200, text="Fetching Data...", font=("Segoe UI", 30), fill="white")

    # Define entry boxes
    global input_mov, input_year
    input_mov = Entry(window, font=("Segoe UI", 18), width=45, bg="#ade5f1", bd=0)
    input_year = Entry(window, font=("Segoe UI", 18), width=15, bg="#ade5f1", bd=0)

    # Add the entry boxes to the canvas
    global mov_window, year_window
    mov_window = my_canvas.create_window(34, 100, anchor="nw", window=input_mov)
    year_window = my_canvas.create_window(34, 220, anchor="nw", window=input_year)

    #  Define Predict Button
    global btn1_window, btn1
    btn1 = Button(
        window,
        text="Predict",
        font=("Lucida Console", 20),
        width=15,
        bg="#ade5f1",
        command=btn_clicked)
    btn1_window = my_canvas.create_window(36, 350, anchor="nw", window=btn1)


home()

window.resizable(False, False)
window.mainloop()
