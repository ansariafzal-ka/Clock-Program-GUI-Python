from tkinter import *
from time import *

def update():
    time_str = strftime("%I:%M:%S %p")
    time_label.config(text=time_str)
    
    time_label.after(1000, update )

window = Tk()
window.title("Clock")

time_label = Label(window,font=("Arial", 50), fg="white", bg="black")
time_label.pack()

update()

window.mainloop()