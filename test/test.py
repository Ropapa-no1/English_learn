from tkinter import *

abl1 = Tk()

can = Canvas(abl1, width=200, height=200, bg='ivory')
can.pack(padx=10, pady=10)


tex1 = Label(abl1, text='asdsadsa', fg='red')
tex1.pack()
gomb1 = Button(abl1, text='exit', command=abl1.destroy)
gomb1.pack()

abl1.mainloop()