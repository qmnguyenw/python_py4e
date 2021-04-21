Python program to generate a list of alphabets in lexical order



 **Prerequisite:**chr()

The following methods explain how a python list with alphabets in
lexical(alphabetic) order can be generated dynamically using chr() method.

 **Approach:**

The core of the concept in both methods is almost same, they only differ in
implementation:

  1. Validate size of alphabet list(size=26).
  2. If size>26, change to 26.
  3. If size≤0, no meaning left to the function and to make it meaningful set size to 26.
  4. Use chr() to produce the list using any of following methods.

 **Method 1:** _Using_ _loop_

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# function to get the list of alphabets

def generateAlphabetListDynamically(size = 26):

 size = 26 if (size > 26 or size <= 0) else size

 

 # Empty list 

 alphabetList = []

 

 # Looping from 0 to required size 

 for i in range(size):

 alphabetList.append(chr(65 + i))

 

 # return the generated list

 return alphabetList

 

 

alphabetList = generateAlphabetListDynamically()

print('The alphabets in the list are:', *alphabetList)  
  
---  
  
 __

 __

 **Output:**

> The alphabets in the list are: A B C D E F G H I J K L M N O P Q R S T U V W
> X Y Z

 **Method 2:** using list comprehension

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

def generateAlphabetListDynamically(size=26):

 size = 26 if (size > 26 or size <= 0) else size

 

 # Here we are looping from 0 to upto specified size

 # 65 is added because it is ascii equivalent of 'A'

 alphabetList = [chr(i+65) for i in range(size)]

 

 # returning the list

 return alphabetList

 

 

# Calling the function to get the alphabets

alphabetList = generateAlphabetListDynamically()

print('The alphabets in the list are:', *alphabetList)  
  
---  
  
 __

 __

 **Output:**

> The alphabets in the list are: A B C D E F G H I J K L M N O P Q R S T U V W
> X Y Z

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

