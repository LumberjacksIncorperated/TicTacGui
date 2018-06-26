#------------------------------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------------------------------
import unittest
from conditions import preconditions, PreconditionError
import sys
import Tkinter as tk
from tic_tac_board import Board
import time

#------------------------------------------------------------------------------------------------------
# TEST FLAG
#------------------------------------------------------------------------------------------------------
testFlag = None

#------------------------------------------------------------------------------------------------------
# IMPLEMENTATION
#------------------------------------------------------------------------------------------------------
class TicTacCanvas(tk.Canvas):

    #------------------------------------------------------------------------------------------------------
    # CONSTANTS
    #------------------------------------------------------------------------------------------------------
    _BOX_LENGTH = 60
    _MAX_BOARD_POSITION = 3
    _MAX_MARKER = 3

    #------------------------------------------------------------------------------------------------------
    # SUPPORT METHODS
    #------------------------------------------------------------------------------------------------------
    @preconditions( (lambda self: True),
    				(lambda marker: ( (isinstance(marker, int))) and (marker >= 0) and (marker < TicTacCanvas._MAX_MARKER) ) )
    def _get_colour_for_marker(self, marker):
        if marker == 0:
            return "red"
        if marker == 1:
            return "blue"
        if marker == 2:
            return "white"
    #END

    @preconditions( (lambda self: True),
    				(lambda marker: ( (isinstance(marker, int))) and (marker >= 0) and (marker < TicTacCanvas._MAX_MARKER) ),
                    (lambda boardXPosition: ( (isinstance(boardXPosition, int))) and (boardXPosition >= 0) and (boardXPosition < TicTacCanvas._MAX_BOARD_POSITION) ), 
                    (lambda boardYPosition: ( (isinstance(boardYPosition, int))) and (boardYPosition >= 0) and (boardYPosition < TicTacCanvas._MAX_BOARD_POSITION) ) ) 
    def _paint_board_for_marker_and_position(self, marker, xPosition, yPosition):
        colour = self._get_colour_for_marker(marker)
        xStartPositionInPixels = xPosition*TicTacCanvas._BOX_LENGTH
        yStartPositionInPixels = yPosition*TicTacCanvas._BOX_LENGTH
        xEndPositionInPixels = xPosition*TicTacCanvas._BOX_LENGTH+TicTacCanvas._BOX_LENGTH
        yEndPositionInPixels = yPosition*TicTacCanvas._BOX_LENGTH+TicTacCanvas._BOX_LENGTH
        self.create_rectangle(xStartPositionInPixels, yStartPositionInPixels, xEndPositionInPixels, yEndPositionInPixels, fill=colour)
    #END

    def __init__(self, parent, *args, **kwargs):
        #--------------------------------
        # Required by Tkinter
        #--------------------------------
        tk.Canvas.__init__(self, parent)
        self.pack()
        #--------------------------------
        self._board = Board()
        self.paint_game_board_to_screen()
    #END

    #------------------------------------------------------------------------------------------------------
    #  EXPORTED METHODS
    #------------------------------------------------------------------------------------------------------
    def paint_game_board_to_screen(self):
        '''
        DESCRIPTION:
            Paints the current board to user screen

        RETURNS:
            None
        '''
        self.delete("all")
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                currentBoardMarker = self._board.getMarkerAtBoardPosition(boardXPosition, boardYPosition)
                self._paint_board_for_marker_and_position(currentBoardMarker, boardXPosition, boardYPosition)
    #END

    def getBoard(self):
        '''
        DESCRIPTION:
            Retrieves that game board that this canas will paint to the screen

        RETURNS: 
            The game board associated with this canvas
        '''
        return self._board
    #END

#------------------------------------------------------------------------------------------------------
# TESTING IMPLEMENTATION
#------------------------------------------------------------------------------------------------------
class TestConstructor(unittest.TestCase):
 
    #------------------------------------------------------------------------------------------------------
    # TESTING SUPPORT CODE
    #------------------------------------------------------------------------------------------------------
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def _doneShowing(self):
    	self._tk_root.destroy()
    	self._tk_root.quit()

    def _request_user_confirmation(self):
        user_answer = raw_input("Enter <y> if Tic Tac board is completely red or <n> if it wasn't:\n")
        if(user_answer == 'y'):
            return
        if(user_answer == 'n'):
            raise Exception('Test Failed')
        raise Exception('Incorrect user testing arguement: Test Discounted and Failed')
 
    #------------------------------------------------------------------------------------------------------
    # POSITIVE TESTING
    #------------------------------------------------------------------------------------------------------
    def test_construction(self):
    	if not (testFlag == "-interactive"):
            print("\n<Test function 'test_construction' is not run on this testing mode.>")
            return
        print(chr(27) + "[2J") # Just clears terminal screen
        
        self._tk_root = tk.Tk()
        self._tk_root.title("TEST")
        self._tk_root.geometry("180x180")
        self._canvas = TicTacCanvas(self._tk_root, width=180, height=180)
        self._tk_root.after(3000, self._doneShowing)
        self._tk_root.mainloop()
        
        try:
            self._request_user_confirmation()
        except Exception:
            raise Exception

class TestPaintBoardForMarkerAndPosition(unittest.TestCase):
 
    #------------------------------------------------------------------------------------------------------
    # TESTING SUPPORT CODE
    #------------------------------------------------------------------------------------------------------
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def _doneShowing(self):
    	self._tk_root.destroy()
    	self._tk_root.quit()

    def _request_user_confirmation(self):
        user_answer = raw_input("Enter <y> if Tic Tac board is as described or <n> if it wasn't:\n")
        if(user_answer == 'y'):
            return
        if(user_answer == 'n'):
            raise Exception('Test Failed')
        raise Exception('Incorrect user testing arguement: Test Discounted and Failed')

    def _create_and_display_paint_board_for_marker_and_position(self, marker, xPosition, yPosition):
        self._tk_root = tk.Tk()
        self._tk_root.title("TEST")
        self._tk_root.geometry("180x180")
        self._canvas = TicTacCanvas(self._tk_root, width=180, height=180)
        self._canvas._paint_board_for_marker_and_position(marker, xPosition, yPosition)
        print("<Should see marker colour for marker number: {}>".format(marker))
        print("<Should see x position as the marker colour above: {}>".format(xPosition))
        print("<Should see y position as the marker colour above: {}>".format(yPosition))
        self._tk_root.after(1000, self._doneShowing)
        self._tk_root.mainloop()

    def _test_paint_board_for_marker_and_position(self, marker, xPosition, yPosition):
        self._create_and_display_paint_board_for_marker_and_position(marker, xPosition, yPosition)
        try:
        	self._request_user_confirmation()
        except Exception:
        	raise Exception

    #------------------------------------------------------------------------------------------------------
    # POSITIVE TESTING
    #------------------------------------------------------------------------------------------------------
    def test_paint_board_for_all_markers_and_positions_that_are_valid(self):
    	if not (testFlag == "-interactive"):
            print("\n<Test function 'test_paint_board_for_all_markers_and_positions_that_are_valid' is not run on this testing mode.>")
            return

        for xPosition in range(Board.BOARD_SIZE):
        	for yPosition in range(Board.BOARD_SIZE):
        		for marker in [0,1,2]:
        			print(chr(27) + "[2J") # Just clears terminal screen
        			self._test_paint_board_for_marker_and_position(marker, xPosition, yPosition)

    #------------------------------------------------------------------------------------------------------
    # NEGATIVE TESTING
    #------------------------------------------------------------------------------------------------------
    def test_paint_board_invalid_positions_too_high(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
            	for marker in [0,1,2]:
                	for invalidPosition in range(3,10):
        				self._tk_root = tk.Tk()
        				self._tk_root.title("TEST")
        				self._tk_root.geometry("180x180")
        				self._canvas = TicTacCanvas(self._tk_root, width=180, height=180)
        				self.assertRaises(PreconditionError, self._canvas._paint_board_for_marker_and_position, (marker, invalidPosition, boardYPosition))
        				self._tk_root.after(25, self._doneShowing)
        				self._tk_root.mainloop()                	 
                	for invalidPosition in range(3,10):
        				self._tk_root = tk.Tk()
        				self._tk_root.title("TEST")
        				self._tk_root.geometry("180x180")
        				self._canvas = TicTacCanvas(self._tk_root, width=180, height=180)
        				self.assertRaises(PreconditionError, self._canvas._paint_board_for_marker_and_position, (marker, boardXPosition, invalidPosition))
        				self._tk_root.after(25, self._doneShowing)
        				self._tk_root.mainloop()

    def test_paint_board_invalid_positions_too_low(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                for marker in [0,1,2]:	
                	for invalidPosition in (0, -1, -2, -3, -4, -5, -6, -7):
        				self._tk_root = tk.Tk()
        				self._tk_root.title("TEST")
        				self._tk_root.geometry("180x180")
        				self._canvas = TicTacCanvas(self._tk_root, width=180, height=180)
        				self.assertRaises(PreconditionError, self._canvas._paint_board_for_marker_and_position, (marker, invalidPosition, boardYPosition))
        				self._tk_root.after(25, self._doneShowing)
        				self._tk_root.mainloop()
                	for invalidPosition in (0, -1, -2, -3, -4, -5, -6, -7):
        				self._tk_root = tk.Tk()
        				self._tk_root.title("TEST")
        				self._tk_root.geometry("180x180")
        				self._canvas = TicTacCanvas(self._tk_root, width=180, height=180)
        				self.assertRaises(PreconditionError, self._canvas._paint_board_for_marker_and_position, (marker, boardXPosition, invalidPosition))
        				self._tk_root.after(25, self._doneShowing)
        				self._tk_root.mainloop()

    def test_paint_board_invalid_positions_invalid_type(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
            	for marker in [0,1,2]:	
                	for invalidPosition in (0.0, -1.134234, "asd", [1, 2], (1, 2)):
        				self._tk_root = tk.Tk()
        				self._tk_root.title("TEST")
        				self._tk_root.geometry("180x180")
        				self._canvas = TicTacCanvas(self._tk_root, width=180, height=180)
        				self.assertRaises(PreconditionError, self._canvas._paint_board_for_marker_and_position, (marker, invalidPosition, boardYPosition))
        				self._tk_root.after(25, self._doneShowing)
        				self._tk_root.mainloop() 
                	for invalidPosition in (0.0, -1.134234, "asd", [1, 2], (1, 2)):
        				self._tk_root = tk.Tk()
        				self._tk_root.title("TEST")
        				self._tk_root.geometry("180x180")
        				self._canvas = TicTacCanvas(self._tk_root, width=180, height=180)
        				self.assertRaises(PreconditionError, self._canvas._paint_board_for_marker_and_position, (marker, boardXPosition, invalidPosition))
        				self._tk_root.after(25, self._doneShowing)
        				self._tk_root.mainloop() 

    def test_paint_board_invalid_marker_too_high(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
            	for marker in range(3,10):
        			self._tk_root = tk.Tk()
        			self._tk_root.title("TEST")
        			self._tk_root.geometry("180x180")
        			self._canvas = TicTacCanvas(self._tk_root, width=180, height=180)
        			self.assertRaises(PreconditionError, self._canvas._paint_board_for_marker_and_position, (marker, boardXPosition, boardYPosition))
        			self._tk_root.after(25, self._doneShowing)
        			self._tk_root.mainloop() 

    def test_paint_board_invalid_marker_too_low(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                for marker in (0, -1, -2, -3, -4, -5, -6, -7):	
        			self._tk_root = tk.Tk()
        			self._tk_root.title("TEST")
        			self._tk_root.geometry("180x180")
        			self._canvas = TicTacCanvas(self._tk_root, width=180, height=180)
        			self.assertRaises(PreconditionError, self._canvas._paint_board_for_marker_and_position, (marker, boardXPosition, boardYPosition))
        			self._tk_root.after(25, self._doneShowing)
        			self._tk_root.mainloop() 

    def test_paint_board_invalid_marker_invalid_type(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
            	for marker in (0.0, -1.134234, "asd", [1, 2], (1, 2)):	
        			self._tk_root = tk.Tk()
        			self._tk_root.title("TEST")
        			self._tk_root.geometry("180x180")
        			self._canvas = TicTacCanvas(self._tk_root, width=180, height=180)
        			self.assertRaises(PreconditionError, self._canvas._paint_board_for_marker_and_position, (marker, boardXPosition, boardYPosition))
        			self._tk_root.after(25, self._doneShowing)
        			self._tk_root.mainloop() 

class TestGetBoard(unittest.TestCase):
 
    #------------------------------------------------------------------------------------------------------
    # TESTING SUPPORT CODE
    #------------------------------------------------------------------------------------------------------
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def _doneShowing(self):
    	self._tk_root.destroy()
    	self._tk_root.quit()
 
    #------------------------------------------------------------------------------------------------------
    # POSITIVE TESTING
    #------------------------------------------------------------------------------------------------------
    def test_get_a_board_that_is_new(self):
        self._tk_root = tk.Tk()
        self._tk_root.title("TEST")
        self._tk_root.geometry("180x180")
        self._canvas = TicTacCanvas(self._tk_root, width=180, height=180)
        self._board = self._canvas.getBoard()
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):    
                self.assertEqual( self._board._boardGrid[boardXPosition][boardYPosition], 0 )
        self._tk_root.after(10, self._doneShowing)
        self._tk_root.mainloop()

class TestPaintGameBoardToScreen(unittest.TestCase):
 
    #------------------------------------------------------------------------------------------------------
    # TESTING SUPPORT CODE
    #------------------------------------------------------------------------------------------------------
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def _doneShowing(self):
    	self._tk_root.destroy()
    	self._tk_root.quit()

    def _request_user_confirmation(self):
        user_answer = raw_input("Enter <y> if Tic Tac board is as described or <n> if it wasn't:\n")
        if(user_answer == 'y'):
            return
        if(user_answer == 'n'):
            raise Exception('Test Failed')
        raise Exception('Incorrect user testing arguement: Test Discounted and Failed')

    #------------------------------------------------------------------------------------------------------
    # POSITIVE TESTING
    #------------------------------------------------------------------------------------------------------
    def test_for_expected_boards(self):
    	if not (testFlag == "-interactive"):
            print("\n<Test function 'test_for_expected_boards' is not run on this testing mode.>")
            return

        # TEST BOARD ONE
        print(chr(27) + "[2J") # Just clears terminal screen
        self._tk_root = tk.Tk()
        self._tk_root.title("TEST")
        self._tk_root.geometry("180x180")
        self._canvas = TicTacCanvas(self._tk_root, width=180, height=180)
        self._board = self._canvas.getBoard()
        self._board._boardGrid[0][0] = 1
        self._board._boardGrid[1][1] = 1
        self._board._boardGrid[2][2] = 1
        self._canvas.paint_game_board_to_screen()
        print("< Should see a diagonal white stripe going top left to bottom right >")
        self._tk_root.after(3000, self._doneShowing)
        self._tk_root.mainloop()
        try:
        	self._request_user_confirmation()
        except Exception:
        	raise Exception

        # TEST BOARD TWO
        print(chr(27) + "[2J") # Just clears terminal screen
        self._tk_root = tk.Tk()
        self._tk_root.title("TEST")
        self._tk_root.geometry("180x180")
        self._canvas = TicTacCanvas(self._tk_root, width=180, height=180)
        self._board = self._canvas.getBoard()
        self._board._boardGrid[0][2] = 1
        self._board._boardGrid[1][1] = 1
        self._board._boardGrid[2][0] = 1
        self._canvas.paint_game_board_to_screen()
        print("< Should see a diagonal white stripe going bottom left to top right >")
        self._tk_root.after(3000, self._doneShowing)
        self._tk_root.mainloop()
        try:
        	self._request_user_confirmation()
        except Exception:
        	raise Exception

#------------------------------------------------------------------------------------------------------
# TESTING DRIVER
#------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    
    # Check corret length of command line arguement string
    if not (len(sys.argv) == 2):
        print "Test Bench: Not Correct Number Testing Arguements\n"
        sys.exit(0)

    # Check valid command line arguements entered
    if ((not (sys.argv[1] == '-interactive')) and (not (sys.argv[1] == '-compilation'))):
        print "Test Bench: Not Correct Testing Arguements\n"
        sys.exit(0)

    # Set the testing flag for the testing level for the module
    testFlag = ((sys.argv[1]) + '.')[:-1]

    # Add verbose output for compilation testing
    if (testFlag == "-compilation") or (testFlag == "-interactive"):
        sys.argv[1] = "-v"
    else:
        del sys.argv[1]
    
    # Run test harness
    unittest.main()

#END