from tkinter import *
from tkinter import ttk

root = Tk()
root.title("My App")
root.geometry("250x200")

def select():
    result = "Выбрано: "
    if python.get() == 1: result += " " + python_checkbutton.cget("text")
    if javascript.get() == 1: result += " " + javascript_checkbutton.cget("text")
    if java.get() == 1: result += " " + java_checkbutton.cget("text")
    if ruby.get() == 1: result += " " + ruby_checkbutton.cget("text")
    if c.get() == 1: result += " " + c_checkbutton.cget("text")
    languages.set(result)


position = {"padx": 6, "pady": 6, "anchor": NW}

languages = StringVar()
languages_label = ttk.Label(textvariable=languages)
languages_label.pack(**position)

python = IntVar()
python_checkbutton = ttk.Checkbutton(text="Python", variable=python, command=select)
python_checkbutton.pack(**position)

javascript = IntVar()
javascript_checkbutton = ttk.Checkbutton(text="JavaScript", variable=javascript, command=select)
javascript_checkbutton.pack(**position)

java = IntVar()
java_checkbutton = ttk.Checkbutton(text="Java", variable=java, command=select)
java_checkbutton.pack(**position)

ruby = IntVar()
ruby_checkbutton = ttk.Checkbutton(text="Ruby", variable=ruby, command=select)
ruby_checkbutton.pack(**position)

c = IntVar()
c_checkbutton = ttk.Checkbutton(text="C", variable=c, command=select)
c_checkbutton.pack(**position)

root.mainloop()
