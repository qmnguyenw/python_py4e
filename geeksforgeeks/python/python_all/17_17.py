Python program to check if lowercase letters exist in a string



Given a String, the task is to write a Python program to check if the string
has lowercase letters or not.

 **Examples:**

    
    
     **Input:** "Live life to the fullest"
    **Output:** false
    
    **Input:** "LIVE LIFE TO THe FULLEST"
    **Output:** false
    
    **Input:** "LIVE LIFE TO THE FULLEST"
    **Output:** true
    

**Methods 1#:** Using islower()

It **** Returns true if all cased characters in the string are lowercase and
there is at least one cased character, false otherwise.

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# is.lower() method in strings

 

#Take any string

str = "Live life to the Fullest"

 

# Traversing Each character of

# the string to check whether

# it is in lowercase

for char in str:

 k = char.islower() 

 if k == True:

 print('True')

 

 # Break the Loop when you

 # get any lowercase character.

 break

 

# Default condition if the string

# does not have any lowercase character.

if(k != 1):

 print('False')  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    True
    

**Methods 2#:** Using isupper()

It **** Returns true if all cased characters in the string are uppercase and
there is at least one cased character, false otherwise.

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program to demonstrate the

# is.upper() method in strings

#Take a string

str = "GEEKS"

 

# Traversing Each character

# to check whether it is in uppercase

for char in str:

 k = char.isupper() 

 if k == False:

 print('False')

 

 # Break the Loop

 # when you get any

 # uppercase character.

 break

 

# Default condition if the string

# does not have any uppercase character.

if(k == 1):

 print('True')  
  
---  
  
 __

 __

 **Output:**

    
    
    True
    

**Methods 3#:** Using ASCII Value to check whether a given character is in
uppercase or lowercase.

The ord() function returns an integer representing the Unicode character.

 **Example:**

    
    
    print(ord('A'))    # 65
    print(ord('a'))    # 97
    

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program to Demonstrate the strings

# methods to check whether given Character

# is in uppercase or lowercase with the help

# of ASCII values

 

#Input by geeks

x = "GEeK"

 

# counter

counter = 0

 

for char in x:

 if(ord(char) >= 65 and ord(char) <= 90):

 

 counter = counter + 1

 

 # Check for the condition 

 # if the ASCII value is Between 97 and 122

 # if condition is True print the

 # corresponding result

 if(ord(char) >= 97 and ord(char) <= 122):

 print("Lower Character found")

 break

if counter == len(x):

 print(True)  
  
---  
  
 __

 __

 **Output:**

    
    
    Lower Character found
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

