from tkinter import * #importaciond e libreria

root = Tk() # creacion de ventana
root.title("Simple Calculator")


myInput = Entry(root, width=35, borderwidth=5)
myInput.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_add():
    return 1

myBtn1 = Button(root, text="1", pady=40,pady=20, command=button_add)
myBtn2 = Button(root, text="2", pady=40,pady=20, command=button_add)
myBtn3 = Button(root, text="3", pady=40,pady=20, command=button_add)
myBtn4 = Button(root, text="4", pady=40,pady=20, command=button_add)
myBtn5 = Button(root, text="5", pady=40,pady=20, command=button_add)
myBtn6 = Button(root, text="6", pady=40,pady=20, command=button_add)
myBtn7 = Button(root, text="7", pady=40,pady=20, command=button_add)
myBtn8 = Button(root, text="8", pady=40,pady=20, command=button_add)
myBtn9 = Button(root, text="9", pady=40,pady=20, command=button_add)
myBtn0 = Button(root, text="0", pady=40,pady=20, command=button_add)

myBtn1.grid(row=3, column=0)
myBtn2.grid(row=3, column=1)
myBtn3.grid(row=3, column=2)

myBtn4.grid(row=2, column=0)
myBtn5.grid(row=2, column=1)
myBtn6.grid(row=2, column=2)

myBtn7.grid(row=1, column=0)
myBtn8.grid(row=1, column=1)
myBtn9.grid(row=1, column=2)

myBtn0.grid(row=4, column=0)

root.mainloop()