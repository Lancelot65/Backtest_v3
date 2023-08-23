from tkinter import Tk, Button, Label, Checkbutton, IntVar

root = Tk()

option = IntVar()
existe = False

def test():
    global existe
    if option.get() == 1:
        root.text = Label(root, text='test')
        root.text.pack()
        existe = True
    if option.get() == 0:
        root.text.destroy()   
        existe = False


Checkbutton(root, text='click', command=test, onvalue=1, offvalue=0, variable=option).pack()
text = Label(root, text='test')

root.mainloop()