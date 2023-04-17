from tkinter import * 

def submit():
    print("The temperature is:"+str(scale.get())+' °C')

window = Tk()

hotimage = PhotoImage(file='hot.png')
hotlabel = Label(image=hotimage)
hotlabel.pack()

scale =Scale(window,
             from_=100,
             to=0,
             length=600,
             orient=VERTICAL,
             font=('Courier',20),
             tickinterval=10,
             showvalue=0,
             resolution=5,
             troughcolor = '#69EAFF',
             fg='#FF1C00',
             bg='#111111'
             )
scale.pack()

coldimage = PhotoImage(file='cold.png')
coldlabel = Label(image=coldimage)
coldlabel.pack()

button = Button(window,text='submit',command=submit)
button.pack()

window.mainloop()
 