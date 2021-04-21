Python | String Split including spaces



The problems and at the same time applications of list splitting is quite
common while working with python strings. The spaces are usually tend to
ignore in the use cases. But sometimes, we might not need to omit the spaces
but include them in our programming output. Let’s discuss certain ways in
which this problem can be solved.

 **Method #1 : Usingsplit() \+ list comprehension**

This kind of operation can be performed using the split function and list
comprehension. The main difference in not omitting the space is that we
specifically add the spaces that we might have omitted in the process, after
each element.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# String Split including spaces

# using list comprehension + split()

 

# initializing string

test_string = "GfG is Best"

 

# printing original string

print("The original string : " + str(test_string))

 

# using list comprehension + split()

# String Split including spaces

res = [i for j in test_string.split() for i in (j, '
')][:-1]

 

# print result

print("The list without omitting spaces : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : GfG is Best
    The list without omitting spaces : ['GfG', ' ', 'is', ' ', 'Best']
    

  

  

**Method #2 : Usingzip() + chain() + cycle()**

This particular task can also be performed using the combination of above 3
functions. The zip function can be used to bind the logic, chain and cycle
function perform the task of inserting the space at appropriate position.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# String Split including spaces

# using zip() + chain() + cycle()

from itertools import chain, cycle

 

# initializing string

test_string = "GfG is Best"

 

# printing original string

print("The original string : " + str(test_string))

 

# using zip() + chain() + cycle()

# String Split including spaces

res = list(chain(*zip(test_string.split(), cycle('
'))))[:-1]

 

# print result

print("The list without omitting spaces : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : GfG is Best
    The list without omitting spaces : ['GfG', ' ', 'is', ' ', 'Best']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

