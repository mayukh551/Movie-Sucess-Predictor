from tkinter import *
from main import *


def display(res):
    canvas.create_text(630, 280, text=res, font=("Poppins", 20), fill="white")


def btn_clicked():
    print("Button Clicked")
    # Movie Name
    input_mov = entry1.get()
    # Release Year of Movie
    input_year = entry0.get()
    result = main_file_run(input_mov, input_year)
    print(result)
    display(result)


window = Tk()

window.geometry("805x635")
window.configure(bg="#000000")
canvas = Canvas(
    window,
    bg="#000000",
    height=635,
    width=805,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file=f"background.png")
background = canvas.create_image(
    402.0, 317.5,
    image=background_img)

# canvas.create_text(630, 280, text="Output", font=("Poppins", 20), fill="white")


img0 = PhotoImage(file=f"img0.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

b0.place(
    x=49, y=296,
    width=183,
    height=66)

entry0_img = PhotoImage(file=f"img_textBox0.png")
entry0_bg = canvas.create_image(
    264.5, 245.0,
    image=entry0_img)

entry0 = Entry(
    bd=0,
    bg="#ade5f1",
    highlightthickness=0, font="Roboto")

entry0.place(
    x=63, y=227,
    width=403,
    height=34)

entry1_img = PhotoImage(file=f"img_textBox1.png")
entry1_bg = canvas.create_image(
    414.5, 154.0,
    image=entry1_img)

entry1 = Entry(
    bd=0,
    bg="#ade5f1",
    highlightthickness=0, font="Roboto")

entry1.place(
    x=63, y=136,
    width=703,
    height=34)

window.resizable(False, False)
window.mainloop()
