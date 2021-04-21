Python program to count the number of spaces in string



Given a string, the task is to write a Python program to count the number of
spaces in the string.

 **Examples:**

    
    
     **Input:** "my name is geeks for geeks"
    **Output:** number of spaces = 5
    
    **Input:** "geeksforgeeks"
    **Output:** number of spaces=0

 **Approach:**

  * Input string from the user’s
  * Initialize count variable with zero
  * Run a for loop I from 0 till the length of string
  * Inside for loop, check if s[i] == blank, then increment count by 1
  * Outside for loop, print count

 **Example 1:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# create funtion that

# return space count

def check_space(string):

 

 # counter

 count = 0

 

 # loop for search each index

 for i in range(0, len(string)):

 

 # Check each char

 # is blank or not

 if string[i] == " ":

 count += 1

 

 return count

 

# driver node

string = "Welcome to geeksforgeeks"

 

# call the function and display

print("number of spaces ",check_space(string))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    number of spaces  2

 **Example 2:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# create funtion that

# return space count

def check_space(string):

 

 # counter

 count = 0

 

 # loop for search each index

 for i in string:

 

 # Check each char

 # is blank or not

 if i == " ":

 count += 1

 

 return count

 

# driver node

string = "Welcome to geeksforgeeks, Geeks!"

 

# call the function and display

print("number of spaces ",check_space(string))

   
  
---  
  
__

__

**Output:**

    
    
    number of spaces  3

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

