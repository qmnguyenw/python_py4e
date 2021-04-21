Python | Convert numeric words to numbers



Sometimes, while working with python Strings, we can have a problem in which
we need to convert the strings that are in form of named numbers to actual
numbers. This has application in Mathematical domains and Data Science
domains. Lets discuss certain ways in which this task can be performed.

 **Method #1 : Usingloop + join() + split()**  
One of the ways to solve this problem is to use a map, where one can map the
numeric with words and then split the strings and rejoin using mapping to
numbers.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert numeric words to numbers

# Using join() + split()

 

help_dict = {

 'one': '1',

 'two': '2',

 'three': '3',

 'four': '4',

 'five': '5',

 'six': '6',

 'seven': '7',

 'eight': '8',

 'nine': '9',

 'zero' : '0'

}

 

# initializing string

test_str = "zero four zero one"

 

# printing original string

print("The original string is : " + test_str)

 

# Convert numeric words to numbers

# Using join() + split()

res = ''.join(help_dict[ele] for ele in test_str.split())

 

# printing result 

print("The string after performing replace : " + res)   
  
---  
  
__

__

**Output :**

    
    
    The original string is : zero four zero one
    The string after performing replace : 0401
    

**Method #2 : Usingword2number library**  
This problem can also be solved using PyPI library word2number. It has
inbuilt functions that converts words to numbers.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert numeric words to numbers

# Using word2number

from word2number import w2n

 

# initializing string

test_str = "zero four zero one"

 

# printing original string

print("The original string is : " + test_str)

 

# Convert numeric words to numbers

# Using word2number

res = w2n.word_to_num(test_str)

 

# printing result 

print("The string after performing replace : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : zero four zero one
    The string after performing replace : 0401
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

