from tkinter import *
from main import *


def btn_clicked():
    print("Button Clicked")
    input_movie = entry1.get()
    input_year = entry0.get()
    print(main_file_run(input_movie, input_year))


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

print(entry0)
print(entry1)
window.resizable(False, False)
window.mainloop()

print(entry0)
print(entry1)
