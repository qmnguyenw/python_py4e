Hangman Game in Python



 **Hangman Wiki:**  
The origins of Hangman are obscure meaning not discovered, but it seems to
have arisen in Victorian times, ” says Tony Augarde, author of The Oxford
Guide to Word Games. The game is mentioned in Alice Bertha Gomme’s
“Traditional Games” in 1894 under the name “Birds, Beasts and Fishes.” The
rules are simple; a player writes down the first and last letters of a word
and another player guesses the letters in between. In other sources, [where?]
the game is called “Gallows”, “The Game of Hangin”, or “Hanger”.

 **Implementation**

This is a simple Hangman game using Python programming language. Beginners can
use this as a small project to boost their programming skills and
understanding logic.

  1. The Hangman program randomly selects a secret word from a list of secret words. The random module will provide this ability, so line 1 in program imports it.
  2.  **The Game:** Here, a random word (a fruit name) is picked up from our collection and the player gets limited chances to win the game.
  3. When a letter in that word is guessed correctly, that letter position in the word is made visible. In this way, all letters of the word are to be guessed before all the chances are over.
  4. For convenience, we have given length of word + 2 chances. For example, word to be guessed is mango, then user gets 5 + 2 = 7 chances, as mango is a five letter word.

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program to illustrate

# Hangman Game

import random

from collections import Counter

 

someWords = '''apple banana mango strawberry 

orange grape pineapple apricot lemon coconut watermelon

cherry papaya berry peach lychee muskmelon'''

 

someWords = someWords.split(' ')

# randomly choose a secret word from our "someWords" LIST.

word = random.choice(someWords) 

 

if __name__ == '__main__':

 print('Guess the word! HINT: word is a name of a fruit')

 

 for i in word:

 # For printing the empty spaces for letters of the word

 print('_', end = ' ') 

 print()

 

 playing = True

 # list for storing the letters guessed by the player

 letterGuessed = '' 

 chances = len(word) + 2

 correct = 0

 flag = 0

 try:

 while (chances != 0) and flag == 0: #flag is updated
when the word is correctly guessed 

 print()

 chances -= 1

 

 try:

 guess = str(input('Enter a letter to guess: '))

 except:

 print('Enter only a letter!')

 continue

 

 # Validation of the guess

 if not guess.isalpha():

 print('Enter only a LETTER')

 continue

 elif len(guess) > 1:

 print('Enter only a SINGLE letter')

 continue

 elif guess in letterGuessed:

 print('You have already guessed that letter')

 continue

 

 

 # If letter is guessed correctly

 if guess in word:

 k = word.count(guess) #k stores the number of times the guessed
letter occurs in the word

 for _ in range(k): 

 letterGuessed += guess # The guess letter is added as many times
as it occurs

 

 # Print the word

 for char in word:

 if char in letterGuessed and (Counter(letterGuessed) !=
Counter(word)):

 print(char, end = ' ')

 correct += 1

 # If user has guessed all the letters

 elif (Counter(letterGuessed) == Counter(word)): # Once the
correct word is guessed fully, 

 # the game ends, even if chances remain

 print("The word is: ", end=' ')

 print(word)

 flag = 1

 print('Congratulations, You won!')

 break # To break out of the for loop

 break # To break out of the while loop

 else:

 print('_', end = ' ')

 

 

 

 # If user has used all of his chances

 if chances <= 0 and (Counter(letterGuessed) !=
Counter(word)):

 print()

 print('You lost! Try again..')

 print('The word was {}'.format(word))

 

 except KeyboardInterrupt:

 print()

 print('Bye! Try again.')

 exit()  
  
---  
  
 __

 __

 **Note:** Please run the program on your terminal.

    
    
    omkarpathak@omkarpathak-Inspiron-3542:~/Documents/
    Python-Programs$ python P37_HangmanGame.py 
    Guess the word! HINT: word is a name of a fruit
    _ _ _ _ _ 
    
    Enter a letter to guess: m
    _ _ m _ _ 
    Enter a letter to guess: o
    _ _ m o _ 
    Enter a letter to guess: l
    l _ m o _ 
    Enter a letter to guess: e
    l e m o _ 
    Enter a letter to guess: n
    l e m o n 
    Congratulations, You won!
    

**Try it yourself Exercises:**

  

  

  * You can further enhance program by adding timer after every Guess
  * You can also give hints from the beginning to make the task a bit easier for user
  * You can also decrease the chance by one only if player’s guess is WRONG. If the guess is right,  
player’s chance is not reduced

This article is contributed by **Omkar Pathak**. If you like GeeksforGeeks and
would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

