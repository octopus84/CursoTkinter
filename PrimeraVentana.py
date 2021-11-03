from tkinter import *
from tkinter import * #importaciond e libreria

root = Tk() # creacion de ventana

# myLabel = Label(root, text = "First Label Tkinter") #Creando un label widget
# myLabel1 = Label(root, text = "Second Label Tkinter") #Creando un label widget
# myLabel2 = Label(root, text = "Tercer Label Tkinter") #Creando un label widget

# myLabel.grid(row=0,column=0)
# myLabel1.grid(row=1,column=1)
# myLabel2.grid(row=3,column=5)

myInput = Entry(root, width=50, bg="yellow", fg="blue")
myInput.pack()
myInput.insert(0,"Insert your name: ")

def myClick():
    myLabel = Label(root, text = "Hallo , " + myInput.get()) #Creando un label widget
    myLabel.pack()

# myBtn = Button(root, text="Click Me!", state=DISABLED)
myBtn = Button(root, text="Click Me!", pady=50, command=myClick, fg="blue", bg="white")
myBtn.pack()

#myLabel.pack()
root.mainloop()