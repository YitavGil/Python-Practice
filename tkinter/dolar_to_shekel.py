from tkinter import *


def dollars_to_sheckels():
    dollars = float(dollars_input.get())
    shekel = dollars * 3.25
    shekel_result_label.config(text=f"{shekel}")


window = Tk()
window.title("Currency Converter")
window.config(padx=20, pady=20)

dollars_input = Entry(width=7)
dollars_input.grid(column=1, row=0)

dollars_label = Label(text="Dollars")
dollars_label.grid(column=2, row=0)

is_equal_label = Label(text="equal to")
is_equal_label.grid(column=0, row=1)

shekel_result_label = Label(text="0")
shekel_result_label.grid(column=1, row=1)

shekel_symbol = Label(text="₪")
shekel_symbol.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=dollars_to_sheckels)
calculate_button.grid(column=1, row=2)






window.mainloop()