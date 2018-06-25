import unittest
from conditions import preconditions, PreconditionError
import sys
from Tkinter import *
from tic_tac_canvas import TicTacCanvas
from user_move import UserMove


class GUI():

    def _user_pressed_mouse(self, event):
        currentUserMove = UserMove(event.x, event.y)
        currentUserMove.executeMoveOnBoard(self._board)
        self._canvas.paint_game_board_to_screen()

    def __init__(self):
        self._tk_root = Tk()
        self._tk_root.title("Tic Tac Game")
        self._tk_root.geometry("180x180")
        self._canvas = TicTacCanvas(self._tk_root, width=180, height=180)
        self._board = self._canvas.getBoard()
        self._tk_root.bind("<Button-1>", self._user_pressed_mouse)
        mainloop()


gui = GUI()


