#Kiev Zogg
#9/23/2021
#A program that does an assortment of actions with numbers
#calculations on them

#Imports
from random import randrange
#Calculation Method
def calc():
#Program loop
    #Boolean Program Loop
    runProgram = True

    #While loop that executes until Boolean is False
    while runProgram == True:

        print("\n\n--Calculations--")

        #Number inputs
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter a number: "))

        #Calculations
        #Addition
        print(num1, " + ", num2, " = ", num1 + num2)
        #Subtraction
        print(num1, " - ", num2, " = ", num1 - num2)
        #Division
        print(num1, " / ", num2, " = ", num1 / num2)
        #Power of
        print(num1, " to the power of ", num2, " = ", num1**num2)
        #Retuns remainder
        print(num1, " % ", num2, " = ", num1 % num2)
        #Floor Division
        print(num1, " // ", num2, " = ", format(num1 // num2, ".0f"))

        #Asks user if they would like to run calculations with new numbers
        runProgramBool = input("\nRun program again? (y/n)")

        #If/Else statement that turns the Loop Boolean False if the answer is
        # anything but "y"
        if runProgramBool.lower() == "n":
            runProgram = False
        elif runProgramBool.lower() != "y":
            #Handles unexpcted input / Reverts to Menu Screen menu()
            print("Unexpected answer! Reverting to Menu Screen")
            runProgram = False
            menu()

#Number Guesser Method
def numGuesser():
    ##Print Message to User
    print("\nGuess a number 0-20 within 4 tries!")
    #Assigns Random Number
    randomInt = randrange(21)

    falseGuess = True
    numOfGueses = 0

    #Loop that runs until Guesses are used up or correct answer is choosen
    while(falseGuess and not(numOfGueses == 4)):
        #User Guess
        userGuess = int(input("Your Guess: "))
        #Correct Guess
        if(userGuess == randomInt):
            falseGuess = False
            print("Congratulations you guessed the correct number!")
        #High Guess
        elif(userGuess > randomInt):
            numOfGueses+=1
            print("You guessed to high\nYou have", 4-numOfGueses, "remaining.")
        #Low Guess
        elif(userGuess < randomInt):
            numOfGueses+=1
            print("You guessed to low\nYou have", 4-numOfGueses, "remaining.")
        #Informs user if they run out of guesses
        if(numOfGueses == 4):
            print("\nYou are out of guesses. The number was", randomInt)
    #Returns to menu screen
    menu()

#Method that print a random rectangle to the screen
def funMethod(row, column):
    #Rows
    for x in range(row):
        #Columns
        for y in range(column):
            print("#", sep="", end="")
        print("")
    #Spooky Suprise, if either the row or column equal 4 BOO is printed
    if((row or column) == 4):
        print("BOOO")
    #Calls menu
    menu()





#Menu Method
def menu():
    #Prints UI to Screen
    print("\n--Weclome to Numbers Fun", end="--\n")
    print("Programs")
    print("-Calculations (s)")
    print("-Number Guesser (n)")
    print("Fun Suprise (f)")
    print("-Close program(c)", end="\n\n")

    #Command
    command = input("Enter command: ")

    #S = Starts program
    #C = Close program
    if(command.lower() == "s"):
        print("Starting Calculations\n")
        calc()
    elif(command.lower() == "n"):
        print("Starting Number Guesser")
        numGuesser()
    elif(command.lower() == "f"):
        print("SUPRISE LOADING...")
        funMethod(randrange(7), randrange(20))
    elif(command.lower() == "c"):
        print("Closing program\n")
        #Prints Bye 3 Times
        print("Bye" * 3, command, sep="")
    else:
        #Handles unexpcted input
        print("\nInvalid Command\nExample, inputing c closes the program")
        # String Concatenation
        print("s: To enter program\n" + "c: To close program")
        menu()



#Call menu function
menu()
