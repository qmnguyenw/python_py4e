21 Number game in Python



21, Bagram, or Twenty plus one is a game which progresses by counting up 1 to
21, with the player who calls “21” is eliminated. It can be played between any
number of players.

 **Implementation**  
This is a simple 21 number game using Python programming language. The game
illustrated here is between the player and the computer. There can be many
variations in the game.

  * The player can choose to start first or second.
  * The list of numbers is shown before the Player takes his turn so that it becomes convinient.
  * If consecutive numbers are not given in input then the player is automatically disqualified.
  * The player loses if he gets the chance to call 21 and wins otherwise.

Winning against the computer can be possible by choosing to play second. The
strategy is to call numbers till the multiple of 4 which would eventually lead
to 21 on computer hence making the player the winner.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to play 21 Number game

 

# returns the nearest multiple to 4

def nearestMultiple(num):

 if num >= 4:

 near = num + (4 - (num % 4))

 else:

 near = 4

 return near

 

def lose1():

 print ("\n\nYOU LOSE !")

 print("Better luck next time !")

 exit(0)

 

# checks whether the numbers are consecutive

def check(xyz):

 i = 1

 while i<len(xyz):

 if (xyz[i]-xyz[i-1])!= 1:

 return False

 i = i + 1

 return True

 

# starts the game

def start1():

 xyz = []

 last = 0

 while True:

 print ("Enter 'F' to take the first chance.")

 print("Enter 'S' to take the second chance.")

 chance = input('> ')

 

 # player takes the first chance

 if chance == "F":

 while True:

 if last == 20:

 lose1()

 else:

 print ("\nYour Turn.")

 print ("\nHow many numbers do you wish to enter?")

 inp = int(input('> '))

 

 if inp > 0 and inp <= 3:

 comp = 4 - inp

 else:

 print ("Wrong input. You are disqualified from the game.")

 lose1()

 

 i, j = 1, 1

 

 print ("Now enter the values")

 while i <= inp:

 a = input('> ')

 a = int(a)

 xyz.append(a)

 i = i + 1

 

 # store the last element of xyz.

 last = xyz[-1] 

 

 # checks whether the input 

 # numbers are consecutive

 if check(xyz) == True: 

 if last == 21:

 lose1()

 

 else:

 #"Computer's turn."

 while j <= comp:

 xyz.append(last + j)

 j = j + 1

 print ("Order of inputs after computer's turn is: ")

 print (xyz)

 last = xyz[-1]

 else:

 print ("\nYou did not input consecutive integers.")

 lose1()

 

 # player takes the second chance

 elif chance == "S":

 comp = 1

 last = 0

 while last < 20:

 #"Computer's turn"

 j = 1

 while j <= comp:

 xyz.append(last + j)

 j = j + 1

 print ("Order of inputs after computer's turn is:")

 print (xyz)

 if xyz[-1] == 20:

 lose1()

 

 else:

 print ("\nYour turn.")

 print ("\nHow many numbers do you wish to enter?")

 inp = input('> ')

 inp = int(inp)

 i = 1

 print ("Enter your values")

 while i <= inp:

 xyz.append(int(input('> ')))

 i = i + 1

 last = xyz[-1]

 if check(xyz) == True:

 # print (xyz)

 near = nearestMultiple(last)

 comp = near - last

 if comp == 4:

 comp = 3

 else:

 comp = comp

 else:

 # if inputs are not consecutive

 # automatically disqualified

 print ("\nYou did not input consecutive integers.")

 # print ("You are disqualified from the game.")

 lose1()

 print ("\n\nCONGRATULATIONS !!!")

 print ("YOU WON !")

 exit(0)

 

 else:

 print ("wrong choice")

 

 

game = True

while game == True:

 print ("Player 2 is Computer.")

 print("Do you want to play the 21 number game? (Yes / No)")

 ans = input('> ')

 if ans =='Yes':

 start1()

 else:

 print ("Do you want quit the game?(yes / no)")

 nex = input('> ')

 if nex == "yes":

 print ("You are quitting the game...")

 exit(0)

 elif nex == "no":

 print ("Continuing...")

 else:

 print ("Wrong choice")

   
  
---  
  
__

__

**Output:**

    
    
    Player 2 is Computer.
    Do you want to start the game? (Yes/No)
    > Yes
    Enter 'F' to take the first chance.
    Enter 'S' to take the second chance.
    > S
    Order of inputs after computer's turn is:
    [1]
    
    Your turn.
    
    How many numbers do you wish to enter?
    > 3
    Enter your values
    > 2
    > 3
    > 4
    Order of inputs after computer's turn is:
    [1, 2, 3, 4, 5, 6, 7]
    
    Your turn.
    
    How many numbers do you wish to enter?
    > 1
    Enter your values
    > 8
    Order of inputs after computer's turn is:
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    
    Your turn.
    
    How many numbers do you wish to enter?
    > 1
    Enter your values
    > 12
    Order of inputs after computer's turn is:
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    
    Your turn.
    
    How many numbers do you wish to enter?
    > 1
    Enter your values
    > 16
    Order of inputs after computer's turn is:
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    
    Your turn.
    
    How many numbers do you wish to enter?
    > 1
    Enter your values
    > 20
    
    
    CONGRATULATIONS!!!
    YOU WON! 
    

**Try it yourself as exercise:**

  * You can further enhance program by increasing the number of players.
  * You can also use only even/odd numbers.
  * You can replace the numbers with binary number system.
  * You can add levels with variations in the game.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

