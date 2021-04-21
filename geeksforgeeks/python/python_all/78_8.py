Python – Consecutive Alphabetic Occurrence



Sometimes, while working with Strings, we can have a problem in which we need
to check whether we can find occurrence of characters consecutive and
according to English alphabets. This kind of problem can occur in school
programming and day-day programming. Lets discuss certain ways in which this
task can be performed.

 **Method #1 : Using loop +ascii_letters + zip()**  
The combination of above methods can be used to perform this task. In this, we
extract the English alphabets using ascii_letters and check for consecution
using zip().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Consecutive Alphabetic Occurrence

# Using loop + ascii_letters + zip()

from string import ascii_letters

 

# initializing string

test_str = 'geeksforgeeks is best fgr geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# Consecutive Alphabetic Occurrence

# Using loop + ascii_letters + zip()

res = []

for i, j in zip(ascii_letters, ascii_letters[1:]) :

 if i + j in test_str:

 res.append((i, j))

 

# printing result 

print("The Consecutive matching letter pairs : " + str(res))   
  
---  
  
__

__

**Output :**

> The original string is : geeksforgeeks is best fgr geeks  
> The Consecutive matching letter pairs : [(‘f’, ‘g’), (‘s’, ‘t’)]

  

  

**Method #2 : Using list comprehension +ascii_letters + zip()**  
The combination of above methods can be used to perform this task. In this, we
perform similar way as above just in one-liner shortened way using list
comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Consecutive Alphabetic Occurrence

# Using list comprehension + ascii_letters + zip()

from string import ascii_letters

 

# initializing string

test_str = 'geeksforgeeks is best fgr geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# Consecutive Alphabetic Occurrence

# Using list comprehension + ascii_letters + zip()

res = [(i, j) for i, j in zip(ascii_letters, 

 ascii_letters[1:]) if i + j in test_str]

 

# printing result 

print("The Consecutive matching letter pairs : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : geeksforgeeks is best fgr geeks
    The Consecutive matching letter pairs : [('f', 'g'), ('s', 't')]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

