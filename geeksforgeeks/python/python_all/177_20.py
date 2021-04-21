Python program to implement Rock Paper Scissor game



Python is a multipurpose language and one can do literally anything with it.
Python can also be used for game development. Let’s create a simple command
line Rock-Paper-Scissor game without using any external game libraries like
PyGame.

In this game, user gets the first chance to pick the option among Rock, paper
and scissor. After that computer select from remaining two choices(randomly),
then winner is decided as per the rules.

    
    
    Winning Rules as follows :
    
    Rock vs paper-> paper wins
    Rock vs scissor-> Rock wins
    paper vs scissor-> scissor wins.

In this game, randint() inbuilt function is used for generating random integer
value within the given range.

Below is the implementation :

 __

 __  
 __

 __

 __  
 __  
 __

# import random module

import random

 

# Print multiline instruction

# performstring concatenation of string

print("Winning Rules of the Rock paper scissor game as follows: \n"

 +"Rock vs paper->paper wins \n"

 + "Rock vs scissor->Rock wins \n"

 +"paper vs scissor->scissor wins \n")

 

while True:

 print("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n")

 

 # take the input from user

 choice = int(input("User turn: "))

 

 # OR is the short-circuit operator

 # if any one of the condition is true

 # then it return True value

 

 # looping until user enter invalid input

 while choice > 3 or choice < 1:

 choice = int(input("enter valid input: "))

 

 

 # initialize value of choice_name variable

 # corresponding to the choice value

 if choice == 1:

 choice_name = 'Rock'

 elif choice == 2:

 choice_name = 'paper'

 else:

 choice_name = 'scissor'

 

 # print user choice 

 print("user choice is: " + choice_name)

 print("\nNow its computer turn.......")

 

 # Computer chooses randomly any number 

 # among 1 , 2 and 3. Using randint method

 # of random module

 comp_choice = random.randint(1, 3)

 

 # looping until comp_choice value 

 # is equal to the choice value

 while comp_choice == choice:

 comp_choice = random.randint(1, 3)

 

 # initialize value of comp_choice_name 

 # variable corresponding to the choice value

 if comp_choice == 1:

 comp_choice_name = 'Rock'

 elif comp_choice == 2:

 comp_choice_name = 'paper'

 else:

 comp_choice_name = 'scissor'

 

 print("Computer choice is: " + comp_choice_name)

 

 print(choice_name + " V/s " + comp_choice_name)

 

 # condition for winning

 if((choice == 1 and comp_choice == 2) or

 (choice == 2 and comp_choice ==1 )):

 print("paper wins => ", end = "")

 result = "paper"

 

 elif((choice == 1 and comp_choice == 3) or

 (choice == 3 and comp_choice == 1)):

 print("Rock wins =>", end = "")

 result = "Rock"

 else:

 print("scissor wins =>", end = "")

 result = "scissor"

 

 # Printing either user or computer wins

 if result == choice_name:

 print("<== User wins ==>")

 else:

 print("<== Computer wins ==>")

 

 print("Do you want to play again? (Y/N)")

 ans = input()

 

 

 # if user input n or N then condition is True

 if ans == 'n' or ans == 'N':

 break

 

# after coming out of the while loop

# we print thanks for playing

print("\nThanks for playing")  
  
---  
  
 __

 __

 **Output :**

    
    
    winning Rules of the Rock paper and scissor game as follows:
    rock vs paper->paper wins 
    rock vs scissors->rock wins 
    paper vs scissors->scissors wins 
    
    Enter choice 
     1. Rock 
     2. paper 
     3. scissor 
    
    User turn: 1
    User choice is: Rock
    
    Now its computer turn.......
    
    computer choice is: paper
    Rock V/s paper
    paper wins =>computer wins
    do you want to play again?
    N
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

