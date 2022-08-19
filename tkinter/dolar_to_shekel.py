from tkinter import *


window = Tk()
window.title("Currency Converter")

dollars_input = Entry()
dollars_input.grid(column=1 , row=0 )

dollars_label = Label(text="Dollars")

is_equal_label = Label(text="equal to")

shekel_result_label = Label(text="0")

shekel_symbol = Label(text="₪")

calculate_button = Button(text="Calculate")







window.mainloop()