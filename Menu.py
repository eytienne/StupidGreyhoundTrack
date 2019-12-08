from tkinter import *
from Game import Game
from threading import Thread


class Menu(Tk):

    def __init__(self):
        super().__init__(className=Game.WINDOW_TITLE)

        playBTN = Button(self, text="Play", command=self.run_game)
        playBTN.grid(row=0, column=0)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w, h))

    def run_game(self):
        self.withdraw()
        gameThread = Thread(target=lambda: Game().run())
        gameThread.start()
        gameThread.join()
        self.state('normal')

    pass

if __name__ == '__main__':
    Menu().mainloop()

# dictLocals = vars(pygame.key)
# for key in dictLocals:
#     print(key, dictLocals[key])
