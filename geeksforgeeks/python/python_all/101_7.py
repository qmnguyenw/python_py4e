Python | K Character Split String



The problems and at the same time applications of list splitting is quite
common while working with python strings. Some characters are usually tend to
ignore in the use cases. But sometimes, we might not need to omit those
characters but include them in our programming output. Let’s discuss certain
ways in which this problem can be solved.

 **Method #1 : Usingsplit() \+ list comprehension**  
This kind of operation can be performed using the split function and list
comprehension. The main difference in not omitting the character is that we
specifically add the characters that we might have omitted in the process,
after each element.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# K Character Split String

# using list comprehension + split()

 

# initializing string

test_string = "GfG_is_Best"

 

# printing original string

print("The original string : " + str(test_string))

 

# initializing K 

K = '_'

 

# using list comprehension + split()

# K Character Split String

res = [i for j in test_string.split(K) for i in (j,
K)][:-1]

 

# print result

print("The list without omitting Character : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : GfG_is_Best
    The list without omitting Character : ['GfG', '_', 'is', '_', 'Best']
    

**Method #2 : Usingzip() + chain() + cycle()**  
This particular task can also be performed using the combination of above 3
functions. The zip function can be used to bind the logic, chain and cycle
function perform the task of inserting the character at appropriate position.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# K Character Split String

# using zip() + chain() + cycle()

from itertools import chain, cycle

 

# initializing string

test_string = "GfG_is_Best"

 

# printing original string

print("The original string : " + str(test_string))

 

# initializing K 

K = "_"

 

# using zip() + chain() + cycle()

# K Character Split String

res = list(chain(*zip(test_string.split(K),
cycle(K))))[:-1]

 

# print result

print("The list without omitting character : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : GfG_is_Best
    The list without omitting Character : ['GfG', '_', 'is', '_', 'Best']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

