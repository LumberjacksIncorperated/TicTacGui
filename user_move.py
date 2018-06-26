#------------------------------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------------------------------
import unittest
from conditions import preconditions, PreconditionError
import sys
from tic_tac_board import Board

#------------------------------------------------------------------------------------------------------
# TEST FLAG
#------------------------------------------------------------------------------------------------------
testFlag = None

#------------------------------------------------------------------------------------------------------
# IMPLEMENTATION
#------------------------------------------------------------------------------------------------------
class UserMove:

    #------------------------------------------------------------------------------------------------------
    # CONSTANTS
    #------------------------------------------------------------------------------------------------------
    _BOARD_INDEX_TO_PIXEL_NUMBER_CONVERSION = 1/60
    _MAX_POSITION_IN_RESPECT_TO_PIXELS = 180

    #------------------------------------------------------------------------------------------------------
    # EXPORTED METHODS
    #------------------------------------------------------------------------------------------------------
    @preconditions( (lambda self: True),
                    (lambda boardXPosition: ( (isinstance(boardXPosition, int))) and (boardXPosition >= 0) and (boardXPosition < UserMove._MAX_POSITION_IN_RESPECT_TO_PIXELS) ), 
                    (lambda boardYPosition: ( (isinstance(boardYPosition, int))) and (boardYPosition >= 0) and (boardYPosition < UserMove._MAX_POSITION_IN_RESPECT_TO_PIXELS) ) ) 
    def __init__(self, xPosition, yPosition):
        '''
        DESCRIPTION:
            Creates a user move that places a marker on the board for a given board when user move is executed

        PARAMETERS:
            xPosition: a board coordinate in the x direction between 0 and 180 as an integer
            yPosition: a board coordinate in the y direction between 0 and 180 as an integer

        RETURNS:
            (valid arguement) 
                The User Move Object
            (invalid arguement)
                a PreconditionError is thrown
        '''
        self._xPosition = xPosition * UserMove._BOARD_INDEX_TO_PIXEL_NUMBER_CONVERSION
        self._yPosition = yPosition * UserMove._BOARD_INDEX_TO_PIXEL_NUMBER_CONVERSION
	#END

    @preconditions( (lambda self: True),
                    (lambda board: (board is not None) ) ) 
    def executeMoveOnBoard(self, board):
        '''
        DESCRIPTION:
            Places a token at a given board position for a player token that is alternating for the given board

        PARAMETERS:
            board: The board the player marker will be placed on

        RETURNS:
            (valid arguement) 
                None
            (invalid arguement)
                a PreconditionError is thrown
        '''
        board.placePlayerMarkerOnBoardAtPosition(self._xPosition, self._yPosition)
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
 
    #------------------------------------------------------------------------------------------------------
    # POSITIVE TESTING
    #------------------------------------------------------------------------------------------------------
    def test_construction_for_corrext_x_position_value(self):
        for xPosition in range(UserMove._MAX_POSITION_IN_RESPECT_TO_PIXELS):
            for yPosition in range(UserMove._MAX_POSITION_IN_RESPECT_TO_PIXELS):
            	newUserMove = UserMove(xPosition, yPosition)
                self.assertEqual( newUserMove._xPosition, xPosition * UserMove._BOARD_INDEX_TO_PIXEL_NUMBER_CONVERSION )

    def test_construction_for_corrext_y_position_value(self):
        for xPosition in range(UserMove._MAX_POSITION_IN_RESPECT_TO_PIXELS):
            for yPosition in range(UserMove._MAX_POSITION_IN_RESPECT_TO_PIXELS):
            	newUserMove = UserMove(xPosition, yPosition)
                self.assertEqual( newUserMove._yPosition, yPosition * UserMove._BOARD_INDEX_TO_PIXEL_NUMBER_CONVERSION )

    #------------------------------------------------------------------------------------------------------
    # NEGATIVE TESTING
    #------------------------------------------------------------------------------------------------------
    def test_construction_for_x_position_value_too_high(self):
        for xPosition in range(UserMove._MAX_POSITION_IN_RESPECT_TO_PIXELS,UserMove._MAX_POSITION_IN_RESPECT_TO_PIXELS*2):
            for yPosition in range(UserMove._MAX_POSITION_IN_RESPECT_TO_PIXELS):
                self.assertRaises( PreconditionError, UserMove, (xPosition, yPosition))

    def test_construction_for_y_position_value_too_high(self):
        for xPosition in range(UserMove._MAX_POSITION_IN_RESPECT_TO_PIXELS):
            for yPosition in range(UserMove._MAX_POSITION_IN_RESPECT_TO_PIXELS,UserMove._MAX_POSITION_IN_RESPECT_TO_PIXELS*2):
            	self.assertRaises( PreconditionError, UserMove, (xPosition, yPosition))

    def test_construction_for_x_position_value_too_low(self):
        for xPosition in range(-UserMove._MAX_POSITION_IN_RESPECT_TO_PIXELS,0):
            for yPosition in range(UserMove._MAX_POSITION_IN_RESPECT_TO_PIXELS):
                self.assertRaises( PreconditionError, UserMove, (xPosition, yPosition))

    def test_construction_for_y_position_value_too_low(self):
        for xPosition in range(UserMove._MAX_POSITION_IN_RESPECT_TO_PIXELS):
            for yPosition in range(-UserMove._MAX_POSITION_IN_RESPECT_TO_PIXELS,0):
            	self.assertRaises( PreconditionError, UserMove, (xPosition, yPosition))

    def test_construction_for_x_position_invalid_type(self):
        for xPosition in ['asd', (), [], 1.2]:
            for yPosition in range(UserMove._MAX_POSITION_IN_RESPECT_TO_PIXELS):
                self.assertRaises( PreconditionError, UserMove, (xPosition, yPosition))

    def test_construction_for_y_position_value_invalid_type(self):
        for xPosition in range(UserMove._MAX_POSITION_IN_RESPECT_TO_PIXELS):
            for yPosition in ['asd', (), [], 1.2]:
            	self.assertRaises( PreconditionError, UserMove, (xPosition, yPosition))

class TestExecuteMoveOnBoard(unittest.TestCase):
 
    #------------------------------------------------------------------------------------------------------
    # TESTING SUPPORT CODE
    #------------------------------------------------------------------------------------------------------
    def setUp(self):
        pass

    def tearDown(self):
        pass
 
    #------------------------------------------------------------------------------------------------------
    # POSITIVE TESTING
    #------------------------------------------------------------------------------------------------------
    def test_moves_for_player_one(self):
        for xPosition in range(UserMove._MAX_POSITION_IN_RESPECT_TO_PIXELS):
            for yPosition in range(UserMove._MAX_POSITION_IN_RESPECT_TO_PIXELS):
            	self._board = Board()
            	newUserMove = UserMove(xPosition, yPosition)
            	newUserMove.executeMoveOnBoard(self._board)
                xPositionInTermsOfIndex = xPosition * UserMove._BOARD_INDEX_TO_PIXEL_NUMBER_CONVERSION
            	yPositionInTermsOfIndex = yPosition * UserMove._BOARD_INDEX_TO_PIXEL_NUMBER_CONVERSION
            	markerAtCurrentPosition = self._board._boardGrid[xPositionInTermsOfIndex][yPositionInTermsOfIndex]
                self.assertEqual( markerAtCurrentPosition, 2 )
                self._board = None


    def test_moves_for_player_two(self):
        for xPosition in range(UserMove._MAX_POSITION_IN_RESPECT_TO_PIXELS):
            for yPosition in range(UserMove._MAX_POSITION_IN_RESPECT_TO_PIXELS):
            	self._board = Board()
            	newUserMove = UserMove(0, 0)
            	newUserMove.executeMoveOnBoard(self._board)
            	newUserMove = UserMove(xPosition, yPosition)
            	newUserMove.executeMoveOnBoard(self._board)
            	xPositionInTermsOfIndex = xPosition * UserMove._BOARD_INDEX_TO_PIXEL_NUMBER_CONVERSION
            	yPositionInTermsOfIndex = yPosition * UserMove._BOARD_INDEX_TO_PIXEL_NUMBER_CONVERSION
            	markerAtCurrentPosition = self._board._boardGrid[xPositionInTermsOfIndex][yPositionInTermsOfIndex]
                self.assertEqual( markerAtCurrentPosition, 1 )
                self._board = None

    #------------------------------------------------------------------------------------------------------
    # NEGATIVE TESTING
    #------------------------------------------------------------------------------------------------------
    def test_move_with_no_board(self):
        for xPosition in range(UserMove._MAX_POSITION_IN_RESPECT_TO_PIXELS):
            for yPosition in range(UserMove._MAX_POSITION_IN_RESPECT_TO_PIXELS):
            	newUserMove = UserMove(xPosition, yPosition)
            	board = None
            	self.assertRaises(PreconditionError, newUserMove.executeMoveOnBoard, (board))

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