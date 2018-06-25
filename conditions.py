#------------------------------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------------------------------
import sys
import unittest
import types

#------------------------------------------------------------------------------------------------------
# TEST FLAG
#------------------------------------------------------------------------------------------------------
testFlag = None

#------------------------------------------------------------------------------------------------------
# IMPLEMENTATION
#------------------------------------------------------------------------------------------------------
class PreconditionError(Exception):
    '''
    This exception is given when the arguements applied to a function fail the given precondition tests
    '''

class ArguementError(Exception):
    '''
    This exception is given when the precondition tests given in the precondition decorator are invalid
    '''

def preconditions(*preconditions):
    '''
    DESCRIPTION:
        Takes a list of preconditions as lambda expressions, and decorates a function in a check
        of these preconditions on the applied function arguements at runtime

    PARAMETERS:
        *preconditions: A tuple containing lambda expressions representing preconditions for the
                        wrapped function's arguements

    RETURNS:
        (valid arguement)
            Returns the function that is wrapped in a check of the preconditions
            when applied to arguements
        (invalid arguement)
            An ArguementError is raised
    '''
    for precondition in preconditions:
        if not isinstance(precondition, types.LambdaType):
            raise ArguementError

    def decorator(function):
        def function_wrapper(*args):
            for i in range(len(preconditions)):
            	if (preconditions[i] is not None) and (args[i] is not None):
            	    try:
            	    	assert preconditions[i](args[i])
            	    except AssertionError:
            	        #print "PreconditionError: with arguement number[", i, "] in function:", function.__name__, "with arg:", args[i]
            	    	raise PreconditionError()
            result = function(*args)
            return result
        return function_wrapper
    return decorator

#------------------------------------------------------------------------------------------------------
# TESTING IMPLEMENTATION
#------------------------------------------------------------------------------------------------------
class TestPrecondition(unittest.TestCase):
 
    #------------------------------------------------------------------------------------------------------
    # TESTING SUPPORT CODE
    #------------------------------------------------------------------------------------------------------
    ''' Test functions designed to test out different sets of valid preconditions '''
    @preconditions(     (lambda arg1: arg1 > 2)
                    and (lambda arg2: arg2 > 2)
                    and (lambda arg3: arg3 > 2) )
    def dummyFunctionOne(arg1, arg2, arg3):
        return True

    @preconditions(     (lambda arg1: arg1 > 20)
                    and (lambda arg2: arg2 > 29) )
    def dummyFunctionTwo(arg1, arg2):
        return True

    ''' Tuples containing the pairs of test functions and aguements for these test functions '''
    testFunctionPositiveApplicationList = ((dummyFunctionOne, (3, 3, 3)), (dummyFunctionTwo, (30,30)))
    testFunctionNegativeApplicationList = ((dummyFunctionOne, (1, 3, 3)), (dummyFunctionTwo, (2,30)))

    def setUp(self):
        pass
 
    #------------------------------------------------------------------------------------------------------
    # POSITIVE TESTING
    #------------------------------------------------------------------------------------------------------
    def test_known_valid_preconditions(self):
        for testFunction, testFunctionArguements in self.testFunctionPositiveApplicationList:
            self.assertTrue(testFunction(*testFunctionArguements))  

    #------------------------------------------------------------------------------------------------------
    # NEGATIVE TESTING
    #------------------------------------------------------------------------------------------------------
    def test_known_invalid_precondition_arguements(self):
        for testFunction, testFunctionArguements in self.testFunctionNegativeApplicationList:
            self.assertRaises(PreconditionError, testFunction, *testFunctionArguements) 

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