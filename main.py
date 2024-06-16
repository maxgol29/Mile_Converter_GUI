from tkinter import *

window = Tk()

window.title("First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

text = Label(text="is equal to ", font=("Arial", 12))
text.grid(column=0, row=1)

input = Entry(width=10)
input.grid(column=1, row=0, padx=50)
miles_label = Label(text="Miles", font=("Arial", 12))
miles_label.grid(column=2, row=0)

km_label = Label(text='Km', font=("Arial", 12))
km_label.grid(column=2, row=1)


def converter():
    km_converter.config(text = round(int(input.get()) * 1.609344, 2))


button = Button(text="Calculate", command=converter)
button.grid(column=1, row=2)


km_converter = Label(text='0')
km_converter.grid(column=1, row=1)


print(input)

window.mainloop()
