from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)


def calculation():
    input = int(new_input.get())
    value = round((input*1.60934), 2)
    new_answer = answer.config(text=value)
    return new_answer


miles = Label(text="Miles", font=("Arial", 15, "normal"))
miles.grid(column=2, row=0)

is_equal_to = Label(text="is equal to", font=("Arial", 15, "normal"))
is_equal_to.grid(column=0, row=1)

km = Label(text="Km", font=("Arial", 15, "normal"))
km.grid(column=2, row=1)

button = Button(text="Calculate", font=("Arial", 15, "normal"), command=calculation)
button.grid(column=1, row=2)

answer = Label(text="0", font=("Arial", 15, "normal"))
answer.grid(column=1, row=1)

new_input = Entry(width=10, font=("Arial", 15, "normal"))
new_input.insert(END, string="0")
new_input.grid(column=1, row=0)

































window.mainloop()