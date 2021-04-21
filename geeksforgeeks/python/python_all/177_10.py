Hangman Game in Python



Hangman is a word game in which computer will randomly select a word from the
dictionary and player has to guess it correctly in given number of turns. The
word to be guessed is represented by row of stars. If the guessed letter is
present is word, script will automatically be placed to correct places.

>  **Rules to guess the word :**
>
>   1. Input single letter in one turn.
>   2. Don’t use repeated letters.
>   3. Turns will be decremented after every guess.
>

This is the text file used inside the code words.txt, which contains 50,000
English words.

 **Module needed :**

    
    
    import random

Below is the implementation :

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to implement Hangman game

 

# Importing random module

import random

 

# Function to randomly select

# a word from dictionary

def get_word():

 

 # Path to the text file

 with open('/Users/Admin/Desktop/words.txt', 'r') as f:

 

 # Reads each word after splitting

 words1 = f.read().splitlines()

 

 # Returns any random word 

 return random.choice(words1)

 

myword = get_word()

 

# Function prints row of

# stars in place of words

for i in myword:

 

 print("*", end = " ")

 

# Calculating length of word

l = len(myword)

print("\nWord has %d letters" %l)

 

# Check if entered letter is correct

def check(myword, your_word, guess1):

 status = ''

 matches = 0

 

 for letter in myword:

 if letter in your_word:

 status += letter

 else:

 status += '*'

 if letter == guess1:

 matches += 1

 

 if matches > 1:

 print(matches, guess1)

 

 elif matches == 1:

 print(guess1)

 return status

 

# Main Game function

def game():

 guess = 0

 guessed = False

 your_word = []

 turns = len(myword) + 1

 turns1 = turns

 

 print("Total turns: ", turns)

 while guess < turns1:

 guess1 = input("Enter your guess: ")

 

 # Decrementing turn

 # after every guess

 turns -= 1

 

 # Print turns left

 print("Turns left", turns)

 

 # If letter is already guessed

 if guess1 in your_word:

 print("You already guessed")

 elif len(guess1) == 1:

 

 # Appending the letters

 # on their place

 your_word.append(guess1)

 result = check(myword, your_word, guess1)

 

 if result == myword:

 guessed = True

 print("You won " + name)

 print(myword)

 else:

 print(result)

 else:

 print("Invalid entry")

 guess += 1

 if guess == turns1:

 print("Word is:")

 print(myword)

 

# Driver Code

game()  
  
---  
  
 __

 __

 **Output :**

    
    
    * * * * * 
    Word has 5 letters
    Total turns:  11
    
    Enter your guess: a
    Turns left 10
    **********
    
    Enter your guess: i
    Turns left 9
    i
    **i**i****
    
    Enter your guess: s
    Turns left 8
    s
    **i**i**ss
    
    Enter your guess: r
    Turns left 7
    **i**i**ss
    
    Enter your guess: h
    Turns left 6
    **i**i**ss
    
    Enter your guess: e
    Turns left 5
    e
    **i**i*ess
    
    Enter your guess: o
    Turns left 4
    **i**i*ess
    
    Enter your guess: u
    Turns left 3
    u
    *ui**i*ess
    
    Enter your guess: t
    Turns left 2
    t
    *ui*ti*ess
    
    Enter your guess: n
    Turns left 1
    n
    *ui*tiness
    
    Enter your guess: l
    Turns left 0
    l
    *uiltiness
    
    Word is:
    guiltiness
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

