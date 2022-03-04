#ImagesP
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Learn to code  at house by octopus")
# root.iconbitmap("~/Imágenes/icons/python_104451.ico")
# root.iconbitmap(Image.open('images/python_104451.ico'))

my_img = ImageTk.PhotoImage(Image.open("images/aspen.png"))
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()