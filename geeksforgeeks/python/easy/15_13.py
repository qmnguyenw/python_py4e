Simple Keyboard Racing with Python



Let’s make a simple keyboard racing game using Python. In the game, the
participant clicks a pair of keys in quick succession and the program shows
the total time taken by the racer to cover the distance.

 **Rules:**  
As soon as you see ‘GO!’ on screen, start pressing the keys ‘z’ and ‘x’. A ‘*’
sign is shown for every metre covered. Pressing ‘z’ and ‘x’ once will be
counted as 1 metre; targets is to cover 10 metres.

 **Modules Used:**

    
    
    **msvcrt** : Used to get keystroke as input for race
    **time** : Used to calculate time taken to complete the race
    

Note that **MSVCRT** module can only function on a terminal window, not on a
GUI program/IDE.

Below is the code:

  

  

 __

 __  
 __

 __

 __  
 __  
 __

import msvcrt

import time

 

high_score = 17.78

name = "GeeksforGeeks"

while True:

 distance = int(0)


print('\n--------------------------------------------------------------')

 print('\n\nWelcome to the 100m sprint, tap z and x rapidly to
move!')

 print('* = 10m')

 print('\nCurrent record:' + str(high_score) + ' by: ' +
name)

 print('\nPress enter to start')

 input()

 print('Ready...')

 time.sleep(1)

 print('GO!')

 

 start_time = time.time()

 while distance < 10:

 

 k1 = msvcrt.getch().decode('ASCII')

 if k1 == 'z':

 k2 = msvcrt.getch().decode('ASCII')

 if k2 == 'x':

 distance += 1

 if distance == 5:

 print("* You're halfway there!")

 elif distance % 1 == 0:

 print('*')

 

 fin_time = time.time() - start_time

 fin_time = round(fin_time, 2)

 

 print('Congratulations on successfully completing the race!')

 print('You took', fin_time, 'seconds to reach the finish line')

 

 if fin_time < high_score:

 print("Well done you've got a new high score ")

 name = input("Please enter your name : ")

 high_score = fin_time  
  
---  
  
 __

 __

 **Output:**  

![](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-891.png)

Game Initiate

![](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-892.png)

Game in Progress

![](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-893.png)

Game Finished: New High Score

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

