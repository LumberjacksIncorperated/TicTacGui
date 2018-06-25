import unittest
from conditions import preconditions, PreconditionError
import sys
from Tkinter import *
from tic_tac_canvas import TicTacCanvas


class GUI():

    def callback(self, event):
        print "clicked at", event.x, event.y

    def __init__(self):
        self._tk_root = Tk()
        self._canvas = TicTacCanvas(self._tk_root, width=300, height=300)
        self._tk_root.bind("<Button-1>", self.callback)
        mainloop()


gui = GUI()


