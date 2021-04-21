Python – Breaking Up String Variables



 **Prerequisite:** itertools

Given a String, the task is to write a Python program to break up the string
and create individual elements.

>  **Input :** GeeksForGeeks  
>  **Output :** [ ‘G’, ‘e’, ‘e’, ‘k’, ‘s’, ‘F’, ‘o’, ‘r’, ‘G’, ‘e’, ‘e’, ‘k’,
> ‘s’ ]  
>
>
> **Input:** Computer  
>  **Output:** [ ‘C’, ‘o’, ‘m’, ‘p’, ‘u’, ‘t’, ‘e’, ‘r’]

Below are some ways to do the above task.

  

  

 **Method #1:** Using join() function

The join() method provides a flexible way to create strings from iterable
objects. It joins each element of an iterable (such as list, string, and
tuple) by a string separator (the string on which the join() method is called)
and returns the concatenated string.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

a= "GeeksForGeeks"

 

split_string = list(''.join(a))

 

print(split_string)  
  
---  
  
 __

 __

 **Output:**

> [‘G’, ‘e’, ‘e’, ‘k’, ‘s’, ‘F’, ‘o’, ‘r’, ‘G’, ‘e’, ‘e’, ‘k’, ‘s’]

 **Method #2:** Using for loop

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

a= "GeeksForGeeks"

 

res = [i for ele in a for i in ele]

 

print(res)  
  
---  
  
 __

 __

 **Output:**

> [‘G’, ‘e’, ‘e’, ‘k’, ‘s’, ‘F’, ‘o’, ‘r’, ‘G’, ‘e’, ‘e’, ‘k’, ‘s’]

 **Method #3:** Using chain.from_iterable()

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from itertools import chain

 

 

a = "GeeksForGeeks"

 

# using chain.from_iterable()

# to convert list of string and characters

# to list of characters

res = list(chain.from_iterable(a))

 

# printing result

print(str(res))  
  
---  
  
 __

 __

 **Output:**

> [‘G’, ‘e’, ‘e’, ‘k’, ‘s’, ‘F’, ‘o’, ‘r’, ‘G’, ‘e’, ‘e’, ‘k’, ‘s’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

