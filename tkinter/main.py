from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label.config(text="New Text")

#Button

def button_click():
    my_label.config(text=input.get())

button = Button(text="Click Me", command=button_click)
button.pack()

#Entry

input = Entry(width=10)
input.pack()
input.get()

window.mainloop()