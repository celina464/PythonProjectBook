from tkinter import *

import /rock_paper_scissors.py
import /hangman.py
import /poker.py

root = Tk()
root.title("Games")

mainframe = Frame(root, height=200, width=500)
mainframe.pack_propagate(0)
mainframe.pack(padx=5, pady=5)

intro = Label(mainframe, text="Welcome to the Games app!")

intro.pack(side = TOP)

rps_button = Button(mainframe, text="Rock, Paper, Scissors", command=rock_paper_scissors)
rps_button.pack()

hm_button = Button(mainframe, text="Hangman", command=hangman)
hm_button.pack()

hm_button = Button(mainframe, text="Poker", command=poker)
hm_button.pack()

exit_button = Button(mainframe, text="Exit", command=root.destroy)
exit_button.pack(side = BOTTOM)

root.mainloop()
