Python – String Matrix Concatenation



Sometimes, while working with Matrix we can have a problem in which we have
Strings and we need a universal concatanation of all the String present in it.
Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Using list comprehension +join()**  
We can solve this problem using the list comprehension as a potential
shorthand to the conventional loops that we may use to perform this particular
task. We just join the elements extracted and put them into a as a single
string.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# String Matrix Concatenation

# Using list comprehension

 

# initializing list

test_list = [["geeksforgeeks", " is", " best"], [" I",
" Love"], [" Gfg"]]

 

# printing original list

print("The original list : " + str(test_list))

 

# using list comprehension

# count of all the elements in list

res = "".join([ele for sub in test_list for ele in sub])

 

# print result

print("The Matrix Concatenation is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [['geeksforgeeks', ' is', ' best'], [' I', ' Love'], [' Gfg']]
    The Matrix Concatenation is : geeksforgeeks is best I Love Gfg
    

**Method #2 : Usingchain() + join()**  
This particular problem can also be solved using the chain function instead of
list comprehension in which we use the conventional join function to join.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# String Matrix Concatenation 

# Using chain() + join()

from itertools import chain

 

# initializing list

test_list = [["geeksforgeeks", " is", " best"], [" I",
" Love"], [" Gfg"]]

 

# printing original list

print("The original list : " + str(test_list))

 

# using chain() + join()

# String Matrix Concatenation

res = "".join(list(chain(*test_list)))

 

# print result

print("The Matrix Concatenation is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [['geeksforgeeks', ' is', ' best'], [' I', ' Love'], [' Gfg']]
    The Matrix Concatenation is : geeksforgeeks is best I Love Gfg
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

