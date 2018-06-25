#------------------------------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------------------------------
import unittest
from conditions import preconditions, PreconditionError
import sys

#------------------------------------------------------------------------------------------------------
# TEST FLAG
#------------------------------------------------------------------------------------------------------
testFlag = None

#------------------------------------------------------------------------------------------------------
# IMPLEMENTATION
#------------------------------------------------------------------------------------------------------
class Board:
    """ A Tic Tac Toe Board """

    BOARD_SIZE = 3
    EMPTY_VALUE = 0
    PLAYER_TOKEN_VALUE = [1, 2]
    INITIAL_PLAYER_TURN = 1

    def _create_column_of_empty_value(self):
        column = []
        numberColumnEntriesFilled = 0
        while (numberColumnEntriesFilled < Board.BOARD_SIZE):
                column += [Board.EMPTY_VALUE]
                numberColumnEntriesFilled +=1
        return column
    #END

    def __init__(self):
        self._playerTurn = Board.INITIAL_PLAYER_TURN
        self._boardGrid = []
        numberOfBoardRowsCreated = 0
        while (numberOfBoardRowsCreated < Board.BOARD_SIZE):
            newColumn = self._create_column_of_empty_value()
            numberOfBoardRowsCreated +=1
            self._boardGrid += [newColumn]
    #END

    @preconditions( (lambda self: True),
                    (lambda boardXPosition: ((isinstance(boardXPosition, int))) and (boardXPosition >= 0) and (boardXPosition < Board.BOARD_SIZE)), 
                    (lambda boardYPosition: ((isinstance(boardYPosition, int))) and (boardYPosition >= 0) and (boardYPosition < Board.BOARD_SIZE)) ) 
    def placePlayerMarkerOnBoardAtPosition(self, boardXPosition, boardYPosition):
        '''
        DESCRIPTION:
            Places a token at a given board position for a player token that is alternating

        PARAMETERS:
            boardXPosition: a board coordinate in the x direction between 0 and 2 as an integer
            boardYPosition: a board coordinate in the y direction between 0 and 2 as an integer

        RETURNS:
            (valid arguement) 
                None
            (invalid arguement)
                a PreconditionError is thrown
        '''
        self._boardGrid[boardXPosition][boardYPosition] = Board.PLAYER_TOKEN_VALUE[self._playerTurn]
        
        if self._playerTurn == 1:
            self._playerTurn = 0
        else:
            self._playerTurn = 1
    #END

    @preconditions( (lambda self: True),
                    (lambda boardXPosition: ((isinstance(boardXPosition, int))) and (boardXPosition >= 0) and (boardXPosition < Board.BOARD_SIZE)), 
                    (lambda boardYPosition: ((isinstance(boardYPosition, int))) and (boardYPosition >= 0) and (boardYPosition < Board.BOARD_SIZE)) ) 
    def getMarkerAtBoardPosition(self, boardXPosition, boardYPosition):
        '''
        DESCRIPTION:
            Retrieves the token value at a given board position

        PARAMETERS:
            boardXPosition: a board coordinate in the x direction between 0 and 2 as an integer
            boardYPosition: a board coordinate in the y direction between 0 and 2 as an integer

        RETURNS:
            (valid arguement) 
                Integer: Representing the token value, which is an integer defined as Board.EMPTY_VALUE, or
                         board.PLAYER_TOKEN_VALUE[0], or board.PLAYER_TOKEN_VALUE[1]
            (invalid arguement)
                a PreconditionError is thrown
        '''
        markerValue = self._boardGrid[boardXPosition][boardYPosition]
        return markerValue
    #END

#------------------------------------------------------------------------------------------------------
# TESTING IMPLEMENTATION
#------------------------------------------------------------------------------------------------------
class TestConstructor(unittest.TestCase):
 
    #------------------------------------------------------------------------------------------------------
    # TESTING SUPPORT CODE
    #------------------------------------------------------------------------------------------------------
    _known_initial_board_value = [[0,0,0],[0,0,0],[0,0,0]]
    _board = None

    def setUp(self):
        self._board = Board()

    def tearDown(self):
    	self._board = None
 
    #------------------------------------------------------------------------------------------------------
    # POSITIVE TESTING
    #------------------------------------------------------------------------------------------------------
    def test_construction(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                self.assertEqual( self._board._boardGrid[boardXPosition][boardYPosition], 
                                  self._known_initial_board_value[boardXPosition][boardYPosition])  

class TestCreateColumnWithEmptyMarking(unittest.TestCase):
 
    #------------------------------------------------------------------------------------------------------
    # TESTING SUPPORT CODE
    #------------------------------------------------------------------------------------------------------
    _board = None

    def setUp(self):
        self._board = Board()

    def tearDown(self):
        self._board = None
 
    #------------------------------------------------------------------------------------------------------
    # POSITIVE TESTING
    #------------------------------------------------------------------------------------------------------
    def test_column_create_of_correct_length(self):
        createdColumn = self._board._create_column_of_empty_value()
        self.assertEqual( len(createdColumn), 3) 

    def test_column_create_of_correct_entries(self):
        createdColumn = self._board._create_column_of_empty_value()
        for columnIndex in range(Board.BOARD_SIZE):
            self.assertEqual( createdColumn[columnIndex], Board.EMPTY_VALUE) 

class TestPlacePlayerMarkerOnBoardAtPosition(unittest.TestCase):
 
    #------------------------------------------------------------------------------------------------------
    # TESTING SUPPORT CODE
    #------------------------------------------------------------------------------------------------------
    _board = None

    def setUp(self):
        self._board = Board()

    def tearDown(self):
        self._board = None
 
    #------------------------------------------------------------------------------------------------------
    # POSITIVE TESTING
    #------------------------------------------------------------------------------------------------------
    def test_board_intially_empty_marked(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                self.assertEqual( self._board._boardGrid[boardXPosition][boardYPosition], Board.EMPTY_VALUE)  

    def test_board_alternating_turns(self):
        playerTurn = Board.INITIAL_PLAYER_TURN
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                self._board.placePlayerMarkerOnBoardAtPosition(boardXPosition, boardYPosition)
                self.assertTrue( self._board._boardGrid[boardXPosition][boardYPosition], playerTurn)
                if playerTurn == 1:
                    playerTurn = 0
                else:
                    playerTurn = 1

    #------------------------------------------------------------------------------------------------------
    # NEGATIVE TESTING
    #------------------------------------------------------------------------------------------------------
    def test_marking_invalid_positions_too_high(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                for invalidPosition in range(3,100):
                    self._board = Board()
                    self.assertRaises( PreconditionError, self._board.placePlayerMarkerOnBoardAtPosition, (invalidPosition, boardYPosition) )
                    self._board = None 
                for invalidPosition in range(3,100):
                    self._board = Board()
                    self.assertRaises( PreconditionError, self._board.placePlayerMarkerOnBoardAtPosition, (boardXPosition, invalidPosition) )
                    self._board = None 

    def test_marking_invalid_positions_too_low(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                for invalidPosition in (0, -1, -2, -3, -4, -5, -6, -7):
                    self._board = Board()
                    self.assertRaises( PreconditionError, self._board.placePlayerMarkerOnBoardAtPosition, (invalidPosition, boardYPosition) )
                    self._board = None
                for invalidPosition in (0, -1, -2, -3, -4, -5, -6, -7):
                    self._board = Board()
                    self.assertRaises( PreconditionError, self._board.placePlayerMarkerOnBoardAtPosition, (invalidPosition, boardYPosition) )
                    self._board = None 

    def test_marking_invalid_positions_invalid_type(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                for invalidPosition in (0.0, -1.134234, "asd", [1, 2], (1, 2)):
                    self._board = Board()
                    self.assertRaises( PreconditionError, self._board.placePlayerMarkerOnBoardAtPosition, (invalidPosition, boardYPosition) )
                    self._board = None
                for invalidPosition in (0.0, -1.134234, "asd", [1, 2], (1, 2)):
                    self._board = Board()
                    self.assertRaises( PreconditionError, self._board.placePlayerMarkerOnBoardAtPosition, (invalidPosition, boardYPosition) )
                    self._board = None 

class TestGetMarkerOnBoardAtPosition(unittest.TestCase):
 
    #------------------------------------------------------------------------------------------------------
    # TESTING SUPPORT CODE
    #------------------------------------------------------------------------------------------------------
    _board = None

    def setUp(self):
        self._board = Board()

    def tearDown(self):
        self._board = None
 
    #------------------------------------------------------------------------------------------------------
    # POSITIVE TESTING
    #------------------------------------------------------------------------------------------------------
    def test_board_intially_empty_marked(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                self.assertEqual( self._board.getMarkerAtBoardPosition(boardXPosition,boardYPosition), Board.EMPTY_VALUE)  

    def test_marking_random_position_player1(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                self._board = Board()
                self._board._boardGrid[boardXPosition][boardYPosition] = Board.PLAYER_TOKEN_VALUE[0]
                self.assertTrue( self._board.getMarkerAtBoardPosition(boardXPosition,boardYPosition), Board.PLAYER_TOKEN_VALUE[1 - 1] )
                self._board = None


    def test_marking_random_position_player2(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                self._board = Board()
                self._board._boardGrid[boardXPosition][boardYPosition] = Board.PLAYER_TOKEN_VALUE[1]
                self.assertTrue( self._board.getMarkerAtBoardPosition(boardXPosition,boardYPosition), Board.PLAYER_TOKEN_VALUE[2 - 1] )
                self._board = None

    #------------------------------------------------------------------------------------------------------
    # NEGATIVE TESTING
    #------------------------------------------------------------------------------------------------------
    def test_marking_invalid_positions_too_high(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                for invalidPosition in range(3,100):
                    self._board = Board()
                    self.assertRaises( PreconditionError, self._board.getMarkerAtBoardPosition, (invalidPosition, boardYPosition) )
                    self._board = None 
                for player in range(3,100):
                    self._board = Board()
                    self.assertRaises( PreconditionError, self._board.getMarkerAtBoardPosition, (boardXPosition, invalidPosition) )
                    self._board = None 

    def test_marking_invalid_positions_too_low(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                for invalidPosition in (0, -1, -2, -3, -4, -5, -6, -7):
                    self._board = Board()
                    self.assertRaises( PreconditionError, self._board.getMarkerAtBoardPosition, (invalidPosition, boardYPosition) )
                    self._board = None
                for invalidPosition in (0, -1, -2, -3, -4, -5, -6, -7):
                    self._board = Board()
                    self.assertRaises( PreconditionError, self._board.getMarkerAtBoardPosition, (invalidPosition, boardYPosition) )
                    self._board = None 

    def test_marking_invalid_positions_invalid_type(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                for invalidPosition in (0.0, -1.134234, "asd", [1, 2], (1, 2)):
                    self._board = Board()
                    self.assertRaises( PreconditionError, self._board.getMarkerAtBoardPosition, (invalidPosition, boardYPosition) )
                    self._board = None
                for invalidPosition in (0.0, -1.134234, "asd", [1, 2], (1, 2)):
                    self._board = Board()
                    self.assertRaises( PreconditionError, self._board.getMarkerAtBoardPosition, (invalidPosition, boardYPosition) )
                    self._board = None 

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
    if testFlag == "-compilation":
        sys.argv[1] = "-v"
    else:
        del sys.argv[1]
    
    # Run test harness
    unittest.main()

#END