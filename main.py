from tkinter import *

window = Tk()
window.title("Miles to KM Converter")
window.minsize(400, 200)
window.config(padx=20, pady=20)

def convert_miles():
    miles_value = input1.get()
    miles_value = int(miles_value)
    km_value = ((miles_value * 1.609))
    value.config(text=km_value)

input1 = Entry(width=10)
input1.grid(row=0, column=1)

miles = Label(text="Miles")
miles.grid(row=0, column=2)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(row=1, column=0)

value = Label(text="0")
value.grid(row=1, column=1)

km = Label(text="KM")
km.grid(row=1, column=2)

calculate=Button(text="Calculate", command=convert_miles)
calculate.grid(row=2, column=1)







window.mainloop()