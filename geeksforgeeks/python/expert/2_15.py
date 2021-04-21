How to detect if a specific key pressed using Python?



In this article, we will learn how can we detect if a specific key is pressed
by the user or not. Detecting a key is very important for a coder, as the
whole execution of the program is just dependent on a single/pattern key
press.  
You may experience in your day-to-day life that the whole ATM transaction can
be either accepted or denied when you press the enter key just after your PIN.
In the same way, you will see many live examples in your day-to-day life.  
The whole Module is divided into 3 segments, The 1st segment deal with simple
integers, 2nd Alphanumerical characters and In 3rd we will use a python module
to detect a key.

 **Method 1:** Using pynput.

In this method, we will use pynput python module to detecting any key press.
“pynput.keyboard” contains classes for controlling and monitoring the
keyboard. It Calls pynput.keyboard.Listener. stop from anywhere, or return
False from a callback to stop the listener. This library allows you to control
and monitor input devices.

 **Approach:**

  * Import key, Listener from pynput.keyboard
  * Create a with Statement: The with statement is used to wrap the execution of a block with methods defined by a context manager.
  * Define functions

For installation run this code into your terminal.

  

  

    
    
    pip install pynput

 **Example 1:** Here you will see which key is being pressed.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from pynput.keyboard import Key, Listener

 

def show(key):

 

 print('\nYou Entered {0}'.format( key))

 

 if key == Key.delete:

 # Stop listener

 return False

 

# Collect all event until released

with Listener(on_press = show) as listener: 

 listener.join()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201130182151/Ubuntu64bit20201130005900-660x247.png)

 **Example 2:** Here you can detect a specific key is being been pressed or
not.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from pynput.keyboard import Key, Listener

 

def show(key):

 

 if key == Key.tab:

 print("good")

 

 if key != Key.tab:

 print("try again")

 

 # by pressing 'delete' button 

 # you can terminate the loop 

 if key == Key.delete: 

 return False

 

# Collect all event until released

with Listener(on_press = show) as listener:

 listener.join()  
  
---  
  
 __

 __

Output:

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201130182224/Ubuntu64bit20201130010251-660x265.png)

  

  

 **Method 2:**

Here we are taking an input from a user and detecting that the user has
entered the specified Alphanumerical(characters representing the numbers 0 –
9, the letters A – Z (both uppercase and lowercase), and some common symbols
such as @ # * and &.) or not.

 **Approach:**

  * Take user input
  * Create a loop
  * Use condition
  * Print output

 **Code:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

for _ in range(3):

 

 user_input = input(" Please enter your lucky word or type 'END' to
terminate loop: ")

 

 if user_input == "geek":

 print("You are really a geek")

 break

 

 elif user_input == "END":

 break

 

 else:

 print("Try Again")  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201130181637/Ubuntu64bit20201130004439-660x198.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

