from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)


#Button

def button_click():
    my_label.config(text=input.get())


button = Button(text="Click Me", command=button_click)
button.grid(column=1, row=1)

#Entry

input = Entry(width=10)
input.grid(column=2, row=2)
input.get()

window.mainloop()