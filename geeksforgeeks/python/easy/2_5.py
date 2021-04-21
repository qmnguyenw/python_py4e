Snake Water Gun game using Python and C



Snake Water Gun is one of the famous two-player game played by many people. It
is a hand game in which the player randomly chooses any of the three forms
i.e. snake, water, and gun. Here, we are going to implement this game using
python.

This python project is to build a game for a single player that plays with the
computer

**Following are the rules of the game:**

>  **Snake vs. Water:** Snake drinks the water hence wins.  
>  **Water vs. Gun:** The gun will drown in water, hence a point for water  
>  **Gun vs. Snake:** Gun will kill the snake and win.
>
> In situations where both players choose the same object, the result will be
> a draw.
>
>  
>
>
>  
>

We will use _random.choice()_ _method_ and __ nested _if-else_ __ statements
__ to select a random item from a list.

 **Below is the implementation:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import random module

import random

print('Snake - Water - Gun')

# Input no. of rounds

n = int(input('Enter number of rounds: '))

# List containing Snake(s), Water(w), Gun(g)

options = ['s', 'w', 'g']

# Round numbers

rounds = 1

# Count of computer wins

comp_win = 0

# Count of player wins

user_win = 0

# There will be n rounds of game

while rounds <= n:

 # Display round

 print(f"Round :{rounds}\nSnake - 's'\nWater - 'w'\nGun - 'g'")

 # Exception handling

 try:

 player = input("Chose your option: ")

 except EOFError as e:

 print(e)

 # Control of bad inputs

 if player != 's' and player != 'w' and player !=
'g':

 print("Invalid input, try again\n")

 continue

 # random.choice() will randomly chose

 # item from list- options

 computer = random.choice(options)

 # Conditions based on the game rule

 if computer == 's':

 if player == 'w':

 comp_win += 1

 elif player == 'g':

 user_win += 1

 elif computer == 'w':

 if player == 'g':

 comp_win += 1

 elif player == 's':

 user_win += 1

 elif computer == 'g':

 if player == 's':

 comp_win += 1

 elif player == 'w':

 user_win += 1

 # Announce winner of every round

 if user_win > comp_win:

 print(f"You Won round {rounds}\n")

 elif comp_win > user_win:

 print(f"Computer Won round {rounds}\n")

 else:

 print("Draw!!\n")

 rounds += 1

# Final winner based on the number of wons

if user_win > comp_win:

 print("Congratulations!! You Won")

elif comp_win > user_win:

 print("You lose!!")

else:

 print("Match Draw!!")  
  
---  
  
 __

 __

## C

 __

 __  
 __

 __

 __  
 __  
 __

#include<stdio.h>

#include <stdlib.h>

#include <time.h>

int snakeWaterGun(char you, char comp)

{

 // returns 1 if you win, -1 if you lose and 0 if draw

 // Condition for draw // Cases

 // covered: | snake snake |

 // gun gun | water water

 if (you == comp) {

 return 0;

 }

 // Non-draw conditions

 // Cases covered:// snake gun

 // | gun snake | snake water

 // | water sanke | gun water | water gun

 if (you == 's' && comp == 'g')

 {

 return -1;

 }

 else if (you == 'g' && comp == 's')

 {

 return 1;

 }

 if (you == 's' && comp == 'w')

 {

 return 1;

 }

 else if (you == 'w' && comp == 's')

 {

 return -1;

 }

 if (you == 'g' && comp == 'w')

 {

 return -1;

 }

 else if (you == 'w' && comp == 'g')

 {

 return 1;

 }

}

// Driver Code

int main()

{

 char you, comp;

 srand(time(0));

 int number = rand() % 100 + 1;

 if (number < 33)

 {

 comp = 's';

 }

 else if (number > 33 && number < 66)

 {

 comp = 'w';

 }

 else

 {

 comp = 'g';

 }

 printf("Enter 's' for snake, 'w' for "

 "water and 'g' for gun\n");

 scanf("%c", &you;);

 int result = snakeWaterGun(you, comp);

 if (result == 0) {

 printf("Game draw!\n");

 }

 else if (result == 1)

 {

 printf("You win!\n");

 }

 else

 {

 printf("You Lose!\n");

 }

 printf("You chose %c and computer chose %c. ", you,

 comp);

 return 0;

}

// this code is provided by harsh sinha username-

// harshsinha03  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201229160354/Screenshot247.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

