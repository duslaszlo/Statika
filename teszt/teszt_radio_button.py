from tkinter import * 

def order():
    if (x.get()==0) :
        print('Pizza')
    elif (x.get()==1):
        print('Hotdog')
    else :
        print('Hamburger')

window = Tk()

food = ['Pizza','Hotdog','Hamburger']

pizzaimage = PhotoImage(file='pizza.png')
hotdogimage = PhotoImage(file='hotdog.png')
hamburgerimage = PhotoImage(file='hamburger.png')
foodimages = [pizzaimage,hotdogimage,hamburgerimage]

x= IntVar() 

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],
                              variable=x,
                              value=index,
                              padx=25,
                              font=('Arial',50),
                              image= foodimages[index],
                              compound='left',
                              indicatoron=0,
                              width = 375,
                              command=order
                              )
    radiobutton.pack(anchor=NW)

window.mainloop()
 