#------------------------------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------------------------------
import unittest
from conditions import preconditions, PreconditionError
import sys
from Tkinter import *
from tic_tac_canvas import TicTacCanvas
from user_move import UserMove

#------------------------------------------------------------------------------------------------------
# TEST FLAG
#------------------------------------------------------------------------------------------------------
testFlag = None

#------------------------------------------------------------------------------------------------------
# IMPLEMENTATION
#------------------------------------------------------------------------------------------------------
class TicTacApplication():
    
    def _user_pressed_mouse(self, event):
        currentUserMove = UserMove(event.x, event.y)
        currentUserMove.executeMoveOnBoard(self._board)
        self._canvas.paint_game_board_to_screen()
    
    def start(self):
        self._tk_root = Tk()
        self._tk_root.title("Tic Tac Game")
        self._tk_root.geometry("180x180")
        self._canvas = TicTacCanvas(self._tk_root, width=180, height=180)
        self._board = self._canvas.getBoard()
        self._tk_root.bind("<Button-1>", self._user_pressed_mouse)
        mainloop()
    
    def __init__(self):
        pass

#------------------------------------------------------------------------------------------------------
# Application Main
#------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    
    # Check corret length of command line arguement string
    if not (len(sys.argv) == 2):
        print "Test Bench: Not Correct Number Testing Arguements\n"
        sys.exit(0)
    
    # Check valid command line arguements entered
    if ((not (sys.argv[1] == '-interactive')) and (not (sys.argv[1] == '-compilation')) and (not (sys.argv[1] == '-run')) ):
        print "Test Bench: Not Correct Testing Arguements\n"
        sys.exit(0)
    
    # Set the testing flag for the testing level for the module
    testFlag = ((sys.argv[1]) + '.')[:-1]
    del sys.argv[1]
    
    if(testFlag == '-run'):
        app = TicTacApplication()
        app.start()
#END
