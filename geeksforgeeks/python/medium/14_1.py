Mastermind Game using Python



Given the present generation’s acquaintance with gaming and its highly
demanded technology, many aspire to pursue the idea of developing and
advancing it further. Eventually, everyone starts at the beginning. Mastermind
is an old code-breaking game played by two players. The game goes back to the
19th century and can be played with paper and pencil.

 **Prerequisite:**  
Random Numbers in Python

#### Rules of the game

Two players play the game against each other; let’s assume Player 1 and Player
2.

  *  **Player 1** plays first by setting a multi-digit number.
  *  **Player 2** now tries his first attempt at guessing the number.
  * If Player 2 succeeds in his first attempt (despite odds which are highly unlikely) he wins the game and is crowned Mastermind! If not, then Player 1 hints by revealing which digits or numbers Player 2 got correct.
  * The game continues till Player 2 eventually is able to guess the number entirely.
  * Now, **Player 2** gets to set the number and Player 1 plays the part of guessing the number.
  * If Player 1 is able to guess the number within a lesser number of tries than Player 2 took, then Player 1 wins the game and is crowned Mastermind.
  * If not, then Player 2 wins the game.
  * The real game, however, has proved aesthetics since the numbers are represented by color-coded buttons.

For example:  
 **Input:**

    
    
    Player 1, set the number: 5672
    Player 2, guess the number: 1472
    

**Output:**

  

  

    
    
    Not quite the number. You did get 2 digits correct.
    X X 7 2
    
    Enter your next choice of numbers:
    

We shall not be using any of the Pygame Libraries, to aid us with additional
graphics, and therefore shall be dealing only with the framework and concept.
Furthermore, we are going to be playing against the Computer i.e, the Computer
would generate the number to be guessed.

Below is the implementation of the above idea.

 __

 __  
 __

 __

 __  
 __  
 __

import random

 

 

# the .randrange() function generates a

# random number within the specified range.

num = random.randrange(1000, 10000) 

 

n = int(input("Guess the 4 digit number:"))

 

# condition to test equality of the

# guess made. Program terminates if true.

if (n == num): 

 print("Great! You guessed the number in just 1 try! You're a
Mastermind!")

else:

 # ctr variable initialized. It will keep count of 

 # the number of tries the Player takes to guess the number.

 ctr = 0

 

 # while loop repeats as long as the 

 # Player fails to guess the number correctly.

 while (n != num): 

 # variable increments every time the loop

 # is executed, giving an idea of how many

 # guesses were made.

 ctr += 1

 

 count = 0

 

 # explicit type conversion of an integer to

 # a string in order to ease extraction of digits

 n = str(n) 

 

 # explicit type conversion of a string to an integer

 num = str(num) 

 

 # correct[] list stores digits which are correct

 correct = ['X']*4

 

 # for loop runs 4 times since the number has 4 digits.

 for i in range(0, 4): 

 

 # checking for equality of digits

 if (n[i] == num[i]): 

 # number of digits guessed correctly increments

 count += 1

 # hence, the digit is stored in correct[].

 correct[i] = n[i] 

 else:

 continue

 

 # when not all the digits are guessed correctly.

 if (count < 4) and (count != 0): 

 print("Not quite the number. But you did get ", count, " digit(s)
correct!")

 print("Also these numbers in your input were correct.")

 for k in correct:

 print(k, end=' ')

 print('\n')

 print('\n')

 n = int(input("Enter your next choice of numbers: "))

 

 # when none of the digits are guessed correctly.

 elif (count == 0): 

 print("None of the numbers in your input match.")

 n = int(input("Enter your next choice of numbers: "))

 

 # condition for equality.

 if n == num: 

 print("You've become a Mastermind!")

 print("It took you only", ctr, "tries.")  
  
---  
  
 __

 __

Let’s suppose the number set by computer is 1564

 **Output:**

    
    
    Guess the 4 digit number: 1564
    
    Great! You guessed the number in just 1 try! You're a Mastermind!
    

If the number is not guessed in one chance.

 **Output:**

    
    
    Guess the 4 digit number: 2164    
    
    Not quite the number. But you did get 2 digit(s) correct!
    Also these numbers in your input were correct.
    X X 6 4
    
    Enter your next choice of numbers: 3564
    Not quite the number. But you did get 2 digit(s) correct!
    Also these numbers in your input were correct.
    X 5 6 4
    
    Enter your next choice of numbers: 1564
    You've become a Mastermind.
    It took you only 3 tries.
    

You can make the game harder by either increasing the number of digits of the
input or by not disclosing which numbers in the input were correctly placed.  
This has been explained in the code below.

 __

 __  
 __

 __

 __  
 __  
 __

import random

 

 

#the .randrange() function generates

# a random number within the specified range.

num = random.randrange(1000,10000) 

 

n = int(input("Guess the 4 digit number:"))

 

# condition to test equality of the 

# guess made. Program terminates if true.

if(n == num): 

 print("Great! You guessed the number in just 1 try! You're a
Mastermind!")

else:

 # ctr variable initialized. It will keep count of 

 # the number of tries the Player takes to guess the number.

 ctr = 0

 

 # while loop repeats as long as the Player

 # fails to guess the number correctly.

 while(n!=num):

 # variable increments every time the loop 

 # is executed, giving an idea of how many 

 # guesses were made.

 ctr += 1

 

 count = 0

 

 # explicit type conversion of an integer to 

 # a string in order to ease extraction of digits

 n = str(n) 

 

 # explicit type conversion of a string to an integer 

 num = str(num)

 

 # correct[] list stores digits which are correct 

 correct=[] 

 

 # for loop runs 4 times since the number has 4 digits. 

 for i in range(0,4): 

 # checking for equality of digits

 if(n[i] == num[i]): 

 # number of digits guessed correctly increments

 count += 1

 # hence, the digit is stored in correct[].

 correct.append(n[i]) 

 else:

 continue

 

 # when not all the digits are guessed correctly.

 if (count < 4) and (count != 0): 

 print("Not quite the number. But you did get ",count," digit(s)
correct!")

 print("Also these numbers in your input were correct.")

 

 for k in correct:

 print(k, end=' ')

 

 print('\n')

 print('\n')

 n = int(input("Enter your next choice of numbers: "))

 

 # when none of the digits are guessed correctly.

 elif(count == 0): 

 print("None of the numbers in your input match.")

 n=int(input("Enter your next choice of numbers: ")) 

 

 if n==num: 

 print("You've become a Mastermind!")

 print("It took you only",ctr,"tries.")

   
  
---  
  
__

__

Suppose the number set by computer is 54876.

 **Output:**

    
    
    Guess the 5 digit number: 38476
    
    Not quite the number. But you did get 2 digit(s) correct! 
    Enter your next choice of numbers: 41876
    
    Not quite the number. But you did get 4 digit(s) correct!
    Enter the next choice of numbers: 54876
    
    Great you've become a Mastermind!
    It took you only 3 tries!
    

The entire scope of modifying this code is massive. The idea here is to get a
sense of what the concept is. There are plenty of games such as this one which
relies on similar basic code.

By utilizing this code, developing it further while incorporating libraries
from Pygame, would make it more like the real deal, not to mention much more
involving!

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

