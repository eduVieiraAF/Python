from tkinter import *


def submit():
    string = entry.get()
    print(string)
    entry.config(state=DISABLED)
    submit_button.config(state=DISABLED)
    backspace_button.config(state=DISABLED)


def delete():
    entry.delete(0, END)


def backspace():
    entry.delete(len(entry.get()) - 1, END)


window = Tk()  # instantiate an instance of a window
window.title("Phoenix code")
window.resizable(False, False)
window.config(padx=10, pady=10)

entry = Entry(
    window,
    font=("Arial", 36),
    fg="#82c59c",
    bg="#3d3d3e",
    # show="•",
)
# entry.insert(0, "Type here...")
entry.pack(side=LEFT, padx=4)

submit_button = Button(window, text="SUBMIT", command=submit)
submit_button.pack(side=RIGHT, padx=4)

delete_button = Button(window, text="DELETE", command=delete)
delete_button.pack(side=RIGHT, padx=4)

backspace_button = Button(window, text="BACKSPACE", command=backspace)
backspace_button.pack(side=RIGHT, padx=4)

window.mainloop()
