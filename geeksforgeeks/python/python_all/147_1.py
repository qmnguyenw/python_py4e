Python program for word guessing game



Python is a powerful multi-purpose programming language used by multiple giant
companies. It has simple and easy to use syntax making it perfect language for
someone trying to learn computer programming for first time. It is a high-
level programming language, and its core design philosophy is all about code
readability and a syntax which allows programmers to express concepts in a few
lines of code.  
In this article, we will use random module to make a word guessing game. This
game is for beginners learning to code in python and to give them a little
brief about using strings, loops and conditional(If, else) statements.  

> **random module** :  
> Sometimes we want the computer to pick a random number in a given range,
> pick a random element from a list, pick a random card from a deck, flip a
> coin, etc. The random module provides access to functions that support these
> types of operations. One such operation is random.choice() method (returns a
> random item from a list, tuple, or string.) that we are going to use in
> order to select one random word from a list of words that we’ve created.

In this game, there is a list of words present, out of which our interpreter
will choose 1 random word. The user first has to input their names and then,
will be asked to guess any alphabet. If the random word contains that
alphabet, it will be shown as the output(with correct placement) else the
program will ask you to guess another alphabet. User will be given 12
turns(can be changed accordingly) to guess the complete word.  
Below is the Python implementation:  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import random

# library that we use in order to choose

# on random words from a list of words

name = input("What is your name? ")

# Here the user is asked to enter the name first

print("Good Luck ! ", name)

words = ['rainbow', 'computer', 'science',
'programming',

 'python', 'mathematics', 'player', 'condition',

 'reverse', 'water', 'board', 'geeks']

# Function will choose one random

# word from this list of words

word = random.choice(words)

print("Guess the characters")

guesses = ''

# any number of turns can be used here

turns = 12

while turns > 0:

 

 # counts the number of times a user fails

 failed = 0

 

 # all characters from the input

 # word taking one at a time.

 for char in word:

 

 # comparing that character with

 # the character in guesses

 if char in guesses:

 print(char)

 

 else:

 print("_")

 

 # for every failure 1 will be

 # incremented in failure

 failed += 1

 

 if failed == 0:

 # user will win the game if failure is 0

 # and 'You Win' will be given as output

 print("You Win")

 

 # this print the correct word

 print("The word is: ", word)

 break

 

 # if user has input the wrong alphabet then

 # it will ask user to enter another alphabet

 guess = input("guess a character:")

 

 # every input character will be stored in guesses

 guesses += guess

 

 # check input with the character in word

 if guess not in word:

 

 turns -= 1

 

 # if the character doesn’t match the word

 # then “Wrong” will be given as output

 print("Wrong")

 

 # this will print the number of

 # turns left for the user

 print("You have", + turns, 'more guesses')

 

 

 if turns == 0:

 print("You Loose")  
  
---  
  
 __

 __

 **Output:**  

  

  

    
    
    What is your name? Gautam
    Good Luck!  Gautam
    Guess the characters
    _
    _
    _
    _
    _
    guess a character:g
    g
    _
    _
    _
    _
    guess a character:e
    g
    e
    e
    _
    _
    guess a character:k
    g
    e
    e
    k
    _
    guess a character:s
    g
    e
    e
    k
    s
    You Win
    The word is:  geeks 
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

