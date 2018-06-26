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
# AUXILLARY CLASSES
#------------------------------------------------------------------------------------------------------
class PreconditionError(Exception):
    '''
    This exception is given when the arguements applied to a function fail the given precondition tests
    '''

class ArguementError(Exception):
    '''
    This exception is given when the precondition tests given in the precondition decorator are invalid
    '''

#------------------------------------------------------------------------------------------------------
# SUPPORT FUNCTIONS
#------------------------------------------------------------------------------------------------------
def _check_preconditions_are_all_lambda_expressions(preconditions):
    for precondition in preconditions:
        if not isinstance(precondition, types.LambdaType):
            raise ArguementError

def _check_precondition_for_arguement(precondition, arg):
    try:
        assert precondition(arg)
    except AssertionError:
        raise PreconditionError()  #print "PreconditionError: with arguement number[", i, "] in function:", function.__name__, "with arg:", args[i]

def _perform_precondition_check_on_arguements(preconditions, args):
    for preconditionIndex in range(len(preconditions)):
        if (preconditions[preconditionIndex] is not None): #and (args[i] is not None):
            _check_precondition_for_arguement(preconditions[preconditionIndex], args[preconditionIndex])

def _wrap_function_in_precondition_check_with_preconditions_and_args(function, preconditions, args):
    _perform_precondition_check_on_arguements(preconditions, args)
    return function(*args)

def _wrap_function_in_precondition_decorator(preconditions):
    def decorator(function):
        def function_wrapper(*args):
            return _wrap_function_in_precondition_check_with_preconditions_and_args(function, preconditions, args)
        return function_wrapper
    return decorator

#------------------------------------------------------------------------------------------------------
# IMPLEMENTATION
#------------------------------------------------------------------------------------------------------
def preconditions(*preconditions):
    '''
    DESCRIPTION:
        Applies preconditions to a function or method

    PARAMETERS:
        *preconditions: A tuple containing lambda expressions that represent the preconditions

    RETURNS:
        (valid arguement)
            A function that has been wrapped with the preconditions
        (invalid arguement)
            An ArguementError is raised
    '''
    _check_preconditions_are_all_lambda_expressions(preconditions)
    return _wrap_function_in_precondition_decorator(preconditions)
#END

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

    ''' Tuples containing the pairs of test functions and arguements for these test functions '''
    testFunctionPositiveApplicationList = ((dummyFunctionOne, (3, 3, 3)), (dummyFunctionTwo, (30,30)))
    testFunctionNegativeApplicationList = ((dummyFunctionOne, (1, 3, 3)), (dummyFunctionTwo, (2,30)))
 
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
    if (testFlag == "-compilation") or (testFlag == "-interactive"):
        sys.argv[1] = "-v"
    else:
        del sys.argv[1]

    # Run test harness
    unittest.main()

#END
