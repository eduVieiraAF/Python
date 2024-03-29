from tkinter import *

food = ["Pizza", "Hamburger", "Hotdog"]


def order():
    if x.get() == 0:
        print("Pizza! Good ordering.")

    elif x.get() == 1:
        print("Hmm... Burger. Awesome!")

    else:
        print("A hotdog might hit the spot.")


window = Tk()

x = IntVar()

window.title("Python coding")
window.resizable(False, False)
window.config(padx=25, pady=25)

pizza_image = PhotoImage(file='pizza.png')
burger_image = PhotoImage(file='burger.png')
hotdog_image = PhotoImage(file='hotdog.png')

food_images = [pizza_image, burger_image, hotdog_image]

for index in range(len(food)):
    radiobutton = Radiobutton(
        window,
        text=food[index],
        variable=x,
        value=index,
        padx=25,
        pady=10,
        font=("MV Boli", 24),
        image=food_images[index],
        compound="right",
        indicatoron=False,
        width=225,
        command=order,
        bd=3,
    )

    radiobutton.pack()

window.mainloop()
