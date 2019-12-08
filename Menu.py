from tkinter import messagebox
from tkinter import *
from Game import Game
from threading import Thread


class Menu(Tk):

    def __init__(self):
        super().__init__(className=Game.WINDOW_TITLE)

        homeFrame = Frame(self)
        buttonsFrame = Frame(homeFrame)

        playBTN = Button(buttonsFrame, text="Play", command=self.run_game, bg="red")
        playBTN.pack(fill="x")
        settingsBTN = Button(buttonsFrame, text="Settings", command=self.open_settings, bg="blue", fg="white")
        settingsBTN.pack(fill="x")
        
        buttonsFrame.grid()
        
        homeFrame.rowconfigure(0, weight=1)
        homeFrame.columnconfigure(0, weight=1)
        homeFrame.grid(row=0, column=0, sticky="nesw")

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w, h))

    def run_game(self):
        self.withdraw()
        gameThread = Thread(target=lambda: Game().run())
        gameThread.start()
        gameThread.join()
        self.state('normal')

    def open_settings(self):
        messagebox.showinfo(message="Coming soon...")

    pass

if __name__ == '__main__':
    Menu().mainloop()

# dictLocals = vars(pygame.key)
# for key in dictLocals:
#     print(key, dictLocals[key])
