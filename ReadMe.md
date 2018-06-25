# Project Title

Tic Tac Game

## Description

This project creates an application that is a version of the 'Tradtional Tic Tac Toe' game, and is implemented
in the Python programming language.

This project aims to focus on good coding, and as such each Python module is implemented with good structure,
commenting, and testing.

### Installing

First, you need to clone the repository

```
git clone https://github.com/LumberjacksIncorperated/TicTacGui.git
```

Then change permissions on the testing script

```
chmod u+x ./test.sh
```

### Running The Application

To run the game as a GUI:

```
python TicTacApplication.py -run
```

## Running the tests

There are three levels of testing in this project.

"Fast"
This level of test just displays a pass or fail message for the entire project. This level of test should be performed
the most often, as you make incremental changes to the code, to ensure that it is mostly functional

"Compilation"
This level of test displays all the output pass fail messages for the modules, so that if tests pass or fail, the user
can discern which pass or fail

"Interactive"
This is the highest level of test, which runs all the project tests, which include tests that require user involvement

```
Testing Commands:

# Fast
./test.sh -fast

# Compilation
./test.sh -compilation

# Interactive
./test.sh -interactive

```

## Authors

 LumberJacks Incorperated (2018)
