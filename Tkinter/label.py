#label is an area widget that holds text and/or image

from tkinter import *

window = Tk()
window.title("Labels")
window.iconbitmap('./Tkinter/Phoenix.ico')

photo = PhotoImage(file='./Tkinter/spaceship.png')

label = Label(
    window, 
    text="hello, Earth dwellers!", 
    font=("Arial", 40,"bold"), 
    fg="#562f7e",
    bg="#e7eef5",
    relief=SUNKEN, #border
    bd=5, #border width
    padx=20,
    pady=20,
    image=photo,
    compound="top"
    )
#label.place(x=0,y=0) places whereever i choose
label.pack()


window.mainloop()