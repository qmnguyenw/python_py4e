Python program to repeat M characters of a string N times



In this article, the task is to write a Python program to repeat M characters
of string N times.

 **Method 1:**

  1. Define a function that will take a word, m, n values as arguments.
  2. If M is greater than the length of the word. Set m value equal to the length of the word
  3. Now store the characters needed to be repeated into a string named repeat_string using slicing.
  4. Initialize an empty string named as a result
  5. Concatenate the repeat_string to result for n times.
  6. Now print the string.

 **Below is the implementation:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

def repeat(word, m, n):

 

 # if number of characters greater than length of word.

 # set number of characters = length of word

 if(m > len(word)):

 m = len(word)

 

 repeat_word = word[:m]

 result = ""

 

 for i in range(n):

 result = result+repeat_word

 print(result)

 

# driver code

repeat("geeks", 2, 3)  
  
---  
  
 __

 __

 **Output:**

    
    
    gegege

 **Method 2:**

  

  

  1. Define a function which will take a word, m, n values as arguments.
  2. if M is greater than length of word. set m value equal to length of word
  3. Now store the characters needed to be repeated into a string named repeat_string using slicing.
  4. Multiply the repeat_string with n.
  5. Now print the string.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

def repeat(word, m, n):

 

 # if number of characters greater than length of word.

 # set number of characters = length of word

 if(m > len(word)):

 m = len(word)

 

 repeat_word = word[:m]

 print(repeat_word*n)

 

# driver code

repeat("geeks", 2, 3)  
  
---  
  
 __

 __

 **Output:**

    
    
    gegege

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

