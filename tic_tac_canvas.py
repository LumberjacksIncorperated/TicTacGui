import unittest
from conditions import preconditions, PreconditionError
import sys
import Tkinter as tk


class TicTacCanvas(tk.Canvas):

    def __init__(self, parent, *args, **kwargs):
        tk.Canvas.__init__(self, parent)
        self.pack()
        i = self.create_rectangle(0, 0, 30, 30, fill="blue")
        self.itemconfig(i, fill="red")
        #self.text = tk.Text(self, *args, **kwar