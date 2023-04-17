
import tkinter as tk

window = tk.Tk()

#greeting = tk.Label(text="Test GUI window")
#greeting.pack()
#label = tk.Label(text="Hello, Tkinter",fg="white",bg="black",width=25,height=10)
#label.pack()
#button = tk.Button(text="Click me!",width=25,height=5,bg="blue",fg="yellow",)
#button.pack()
#entry = tk.Entry(fg="yellow", bg="blue", width=25)
#entry.pack()

#text_box = tk.Text()
#text_box.pack()
#text_box.insert("1.0", "Hello \nWorld")
#text_box.insert(tk.END, "Put me at the end!")

#frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
#frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
#frame2 = tk.Frame(master=window, width=100, bg="yellow")
#frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
#frame3 = tk.Frame(master=window, width=50, bg="blue")
#frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

#frame = tk.Frame(master=window, width=150, height=150)
#frame.pack()
#label1 = tk.Label(master=frame, text="I'm at (0, 0)", bg="red")
#label1.place(x=0, y=0)
#label2 = tk.Label(master=frame, text="I'm at (75, 75)", bg="yellow")
#label2.place(x=75, y=75)

#for i in range(3):
#    window.columnconfigure(i, weight=1, minsize=75)
#    window.rowconfigure(i, weight=1, minsize=50)
#    for j in range(0, 3):
#        frame = tk.Frame(
#            master=window,
#            relief=tk.RAISED,
#            borderwidth=1
#        )
#        frame.grid(row=i, column=j, padx=5, pady=5)
#        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
#        label.pack(padx=5, pady=5)

#def handle_keypress(event):
#    print(event.char)
#window.bind("<Key>", handle_keypress)

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)
btn_decrease = tk.Button(master=window, text="-")
btn_decrease.grid(row=0, column=0, sticky="nsew")
lbl_value = tk.Label(master=window, text="0")
lbl_value.grid(row=0, column=1)
btn_increase = tk.Button(master=window, text="+")
btn_increase.grid(row=0, column=2, sticky="nsew")

window.mainloop()
