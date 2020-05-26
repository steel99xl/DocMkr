## This is a simple python3 program writen as a demo for the DocMkr program
# by steel99xl
## Imports
import time
from random import randint


## Main Function
# This function goes through a couple of print statments, and taking user input
def main():



    ### Variables
    userInput = ""
    x = 0
    i = 0


    ### Greets the user
    print("Hello World")


    #### Takes user input and prints it back to the user
    userInput = input("Please enter some text : ")
    print("The text you enterd is : " + userInput)


    ### This generates a random number and returns it to the user
    print("This is a random number from 1 to 100 : " + str(randint(1,100)))
    
    ### Randomly generate the number 5
    while x != 5:
        x = randint(1,100);
        i += 1

    print("The number 5 was generated after " + str(i) + " random generations")


    ### Prints off total run time of program
    print("Total time application took to run : " + str(time.process_time()))


### This starts the main function in the program
main()