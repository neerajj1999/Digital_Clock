from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("MY_CLOCk") # clock name show at title

def my_time(): # function created to set time format
    string = strftime(" %H : %M : %S  %p")
    label.config(text = string)
    label.after(1000, my_time)


# giving the clock fonts , font_size, Color to clock
label=Label(root,font=("Digital-7", 75),background="black",foreground="red")
label.pack(anchor='center')
my_time()

mainloop()