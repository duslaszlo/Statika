from tkinter import * 
from tkinter import messagebox

def click():
     #messagebox.showinfo(title='Information',message='Click OK')
     #messagebox.showerror(title='Warning',message='Click OK')
     if messagebox.askretrycancel(title='Warning',message='Click OK'):
         print("Ok pushed")
     else:
         print('Next to Ok pushed')

window = Tk()

button = Button(window,
                command=click,
                text='Click me')

button.pack()

window.mainloop()
 