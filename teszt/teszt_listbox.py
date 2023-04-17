from tkinter import * 

def submit():
    #print(listbox.get(listbox.curselection()))    # Ha a selectmode nem MULTIPLE
    food = []
    for index in listbox.curselection():
        food.insert(index,listbox.get(index))
    for index in food:
        print(index)

def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())

def delete():
    #listbox.delete(listbox.curselection())  # Ha a selectmode nem MULTIPLE
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())

window = Tk()

listbox = Listbox(window,
                  bg='#f7ffde',
                  font=('Courier',35),
                  width=12,
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1,'Pizza')
listbox.insert(2,'Pasta')
listbox.insert(3,'Garlic bread')
listbox.insert(4,'Soup')
listbox.insert(5,'Salad')
listbox.insert(6,'Bread')

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window,text='Submit',command=submit)
submitButton.pack()

addButton = Button(window,text='Add',command=add)
addButton.pack()

deleteButton = Button(window,text='Delete',command=delete)
deleteButton.pack()

window.mainloop()
 