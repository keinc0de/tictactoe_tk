import tkinter as tk
from skin_ttt import SkinTicTacToe
from player import Player


class TicTacToe(SkinTicTacToe):
    def __init__(self):
        super(TicTacToe, self).__init__()
        
        
        
if __name__=="__main__":
    t3 = TicTacToe()
    t3.mainloop()