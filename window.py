from tkinter import *

window = Tk()
window.title("Dog training simulator")
window.iconbitmap("pictures/dog_icon.ico")
bg_picture = PhotoImage(file = "pictures/grass.png")
bg = Label(window, image=bg_picture)
bg.pack()



window.mainloop()