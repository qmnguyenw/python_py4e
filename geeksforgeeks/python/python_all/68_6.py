Number Guessing Game in Python using Binary Search



In the number guessing game, the user selects a number within a defined range
and then the program guesses the number. If the number guessed is wrong then
the user tells the program that is the actual number is greater than the
guessed number or not. Similarly, the program again guesses the number until
the actual number is not guessed.

 **Approach:** The idea is to use binary search, where in each step the half
portion of the search space is reduced. Below is the illustration of the
approach:

  * Intialize the start and end range of the number guessing.
  * Guess the number as middle of the search space. That is

![Number  = \\frac{startRange +
endRange}{2}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-3e9781800fa669881a9a57c5f1d2cf9f_l3.png)

  * If the number guessed is correct, then terminate the program.
  * Otherwise, Ask the user that guessed number is less than the guessed number or not. If yes then reduce the search space accordingly.

Below is the implementation of the above approach:

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python implementation for the

# number guessing using 

# Binary Search

 

# Global Arguments for playing game

args = ["N", "N", "Y"]

index = -1

 

# Temporary function for taking

# input from the local arguments list

def input():

 global index, args;

 index += 1

 return args[index]

 

# Function to guess the number in 

# a defined range of the number

def guessNumber(startRange, endRange):

 if startRange > endRange:

 return True

 

 # Middle of the range

 mid = (startRange + endRange)//2

 

 # Asking user about the 

 # actual number

 print("Is the number is ",

 mid, "?", end = " ")

 user = input()

 print(user)

 

 # Condition to check if the 

 # guessed number is actual number

 if user == "Y" or user == "y":

 print("Voila ! Successfully Guessed Number.")

 return False

 

 # Condition to check if the 

 # guessed number is not correct

 elif user == "N" or user == "n":

 print("Actual number is greater than",\

 mid, "?", end = " ")

 user = input()

 print(user)

 if user == "Y" or user == "y":

 return guessNumber(mid+1, endRange)

 elif user == "N" or user == "n":

 return guessNumber(startRange, mid-1)

 else:

 print("Invalid Input. Print 'Y'/'N'")

 return guessNumber(startRange, endRange)

 

 # Condition to check if the user

 # input was invalid 

 else:

 print("Invalid Input. Print 'Y'/'N' ")

 return guessNumber(startRange, endRange)

 

# Driver Code

if __name__ == "__main__":

 print("Number Guessing game in python")

 startRange = 1

 endRange = 10

 print("Guess a number in range (1 to 10)")

 

 out = guessNumber(startRange, endRange)

 

 if out:

 print("Bad Choices")  
  
---  
  
 __

 __

 **Inputs:**

    
    
    N
    N
    Y
    

**Outputs:**

    
    
    Number Guessing game in python
    Guess a number in range (1 to 10)
    Is the number is  5 ? N
    Actual number is greater than 5 ? N
    Is the number is  2 ? Y
    Voila ! Successfully Guessed Number.
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

