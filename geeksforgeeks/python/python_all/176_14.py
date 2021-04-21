Python | Program to implement Jumbled word game



Python is a multipurpose language and one can do literally anything with it.
Python can also be used for game development. Let’s create a simple Jumbled
word game without using any external game libraries like PyGame.

 **Jumbled word game :** Jumbled word is given to player, player has to
rearrange the characters of the word to make a correct meaningful word.

 **Example :**

    
    
    **Input:** erwta
    **Output:** water
    
    **Input:** mehtatasmci
    **Output:** mathematics
    
    **Input:** keseg
    **Output:** geeks
    

This is a two players game, firstly program pick a random word from the given
list of words using choice() method of random module. After shuffling the
characters of picked word using sample method of random module and shows the
jumbled word on the screen. Current player should give the answer; if it gives
the correct answer after rearranging the characters then player’s score is
incremented by one otherwise not. After quitting the game, winner is decided
on the basis of scores.

 **Using Inbuilt functions :**

  

  

    
    
     **choice() method** randomly choose any word from the list.
    **sample() method** shuffling the characters of the word.

 **User defined functions :**

>  **choose() :** Choosing random word from the list .  
>  **jumble() :** Shuffling the characters of the choosen word. we have to
> pass a choosen word as an argument.  
>  **thank() :** Showing the final scores of both players. Pass a player1
> name, player2 name and score of player1, player2 as an argument.  
>  **check_win() :** Declaring the winner. Pass a player1 name, player2 name,
> and score of player1 and player2 as argument.  
>  **play() :** Starting the game.

Below is the implementation :

 __

 __  
 __

 __

 __  
 __  
 __

# Python program for jumbled words game.

 

# import random module

import random

 

 

# function for choosing random word.

def choose():

 # list of word

 words = ['rainbow', 'computer', 'science',
'programming',

 'mathematics', 'player', 'condition', 'reverse',

 'water', 'board', 'geeks']

 

 # choice() method randomly choose

 # any word from the list.

 pick = random.choice(words)

 

 return pick

 

 

# Function for shuffling the

# characters of the chosen word.

def jumble(word):

 # sample() method shuffling the characters of the word

 random_word = random.sample(word, len(word))

 

 # join() method join the elements

 # of the iterator(e.g. list) with particular character .

 jumbled = ''.join(random_word)

 return jumbled

 

 

# Function for showing final score.

def thank(p1n, p2n, p1, p2):

 print(p1n, 'Your score is :', p1)

 print(p2n, 'Your score is :', p2)

 

 # check_win() function calling

 check_win(p1n, p2n, p1, p2)

 

 print('Thanks for playing...')

 

 

# Function for declaring winner

def check_win(player1, player2, p1score, p2score):

 if p1score > p2score:

 print("winner is :", player1)

 elif p2score > p1score:

 print("winner is :", player2)

 else:

 print("Draw..Well Played guys..")

 

 

# Function for playing the game.

def play():

 # enter player1 and player2 name

 p1name = input("player 1, Please enter your name :")

 p2name = input("Player 2 , Please enter your name: ")

 

 # variable for counting score.

 pp1 = 0

 pp2 = 0

 

 # variable for counting turn

 turn = 0

 

 # keep looping

 while True:

 

 # choose() function calling

 picked_word = choose()

 

 # jumble() fucntion calling

 qn = jumble(picked_word)

 print("jumbled word is :", qn)

 

 # checking turn is odd or even

 if turn % 2 == 0:

 

 # if turn no. is even

 # player1 turn

 print(p1name, 'Your Turn.')

 

 ans = input("what is in your mind? ")

 

 # checking ans is equal to picked_word or not

 if ans == picked_word:

 

 # incremented by 1

 pp1 += 1

 

 print('Your score is :', pp1)

 turn += 1

 

 else:

 print("Better luck next time ..")

 

 # player 2 turn

 print(p2name, 'Your turn.')

 

 ans = input('what is in your mind? ')

 

 if ans == picked_word:

 pp2 += 1

 print("Your Score is :", pp2)

 

 else:

 print("Better luck next time...correct word is :", picked_word)

 

 c = int(input("press 1 to continue and 0 to quit :"))

 

 # checking the c is equal to 0 or not

 # if c is equal to 0 then break out

 # of the while loop o/w keep looping.

 if c == 0:

 # thank() function calling

 thank(p1name, p2name, pp1, pp2)

 break

 

 else:

 

 # if turn no. is odd

 # player2 turn

 print(p2name, 'Your turn.')

 ans = input('what is in your mind? ')

 

 if ans == picked_word:

 pp2 += 1

 print("Your Score is :", pp2)

 turn += 1

 

 else:

 print("Better luck next time.. :")

 print(p1name, 'Your turn.')

 ans = input('what is in your mind? ')

 

 if ans == picked_word:

 pp1 += 1

 print("Your Score is :", pp1)

 

 else:

 print("Better luck next time...correct word is :", picked_word)

 

 c = int(input("press 1 to continue and 0 to quit :"))

 

 if c == 0:

 # thank() function calling

 thank(p1name, p2name, pp1, pp2)

 break

 

 c = int(input("press 1 to continue and 0 to quit :"))

 if c == 0:

 # thank() function calling

 thank(p1name, p2name, pp1, pp2)

 break

 

 

# Driver code

if __name__ == '__main__':

 

 # play() function calling

 play()  
  
---  
  
 __

 __

 **Output:**

    
    
    player 1, Please enter your name :Ankit
    Player 2 , Please enter your name: John
    jumbled word is : abiwrno
    Ankit Your Turn.
    what is in your mind? rainbow
    Your score is : 1
    jumbled word is : rbado
    John Your turn.
    what is in your mind? borad
    Better luck next time.. :
    Ankit Your turn.
    what is in your mind? board
    Your Score is : 2
    press 1 to continue and 0 to quit :1
    jumbled word is : wbrinao
    John Your turn.
    what is in your mind? rainbow
    Your Score is : 1
    
    _press 1 to continue and 0 to quit :1_
    
    jumbled word is : bnrawio
    Ankit Your Turn.
    what is in your mind? rainbow
    Your score is : 3
    jumbled word is : enecsic
    John Your turn.
    what is in your mind? science
    Your Score is : 2
    press 1 to continue and 0 to quit :0
    Ankit Your score is : 3
    John Your score is : 2
    winner is : Ankit
    Thanks for playing...
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

