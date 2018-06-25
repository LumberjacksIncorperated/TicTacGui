#!/bin/sh

#----------------------------------------------------------------------------------------------------------------------
#
# PROJECT
# -------
# Tic Tac
#
# AUTHOR
# ------
# Lumberjacks Incorperated (2018)
#
#----------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------
# GLOBAL FLAGS
#----------------------------------------------------------------------------------------------------------------------
testResultForFastTesting="PASSED"

#----------------------------------------------------------------------------------------------------------------------
# MAIN
#----------------------------------------------------------------------------------------------------------------------
main()
{
    echo "<START>"
    
    echo "    Testing All Modules"
    testAllModules "$1"
    
    cleanupTestFiles

    echo "<DONE>"
}

#----------------------------------------------------------------------------------------------------------------------
# INTERNAL FUNCTIONS
#----------------------------------------------------------------------------------------------------------------------
function testAllModules()
{
    # Enter Project Files Directory
    cd ./

    # Loop through testing all files in Project Files Directory
    for filename in ./*.py; do
        file=$(echo "$filename" | cut -c 3-)
        testModule "$file" "$1"
    done

    # Output testing result if fast compilation was chosen
    if [ "$1" = "-fast" ]; then
        echo "    Test Result = "$testResultForFastTesting""
    fi
}

function testModule()
{
    filename="$1"
    testFlag="$2"

    if [ "$2" = "-fast" ]; then
        fastTestModule "$1" "$2"
    else
        slowTestModule "$1" "$2"
    fi
}

function fastTestModule()
{
    python "$filename" "-compilation" 2>./testResult.txt 1>/dev/null
    result=`cat ./testResult.txt`
    
    if [[ "$result" = *"FAILED"* ]]; then
        testResultForFastTesting="FAILED"
    fi
}

function slowTestModule()
{
    filename="$1"
    testFlag="$2"
    
    # 'Press Enter To Continue' so that user has chance to read previous results
    read -p "Press enter to continue"
    
    echo ""
    echo "##################################################################################################################"
    echo "                                            Testing "$filename" Module..."
    echo "##################################################################################################################"
    python "$filename" "$testFlag" 
    echo "##################################################################################################################"
    echo ""
}

function cleanupTestFiles()
{
    rm testResult.txt
}

#----------------------------------------------------------------------------------------------------------------------
# SCRIPT
#----------------------------------------------------------------------------------------------------------------------
    main "$1"