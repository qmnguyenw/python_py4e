Python | Multiple indices Replace in String



Sometimes, while working with Python Stings, we can have a problem, in which
we need to perform the replace of characters based on several indices of
String. This kind of problem can have applications in many domains. Lets
discuss certain ways in which this task can be performed.

 **Method #1 : Usingloop + join()**  
This is brute force way in which this task can be performed. In this, we
iterate for each character and substitute with replace character if that is
one.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Multiple indices Replace in String

# Using loop + join()

 

# initializing string

test_str = 'geeksforgeeks is best'

 

# printing original string

print("The original string is : " + test_str)

 

# initializing list 

test_list = [2, 4, 7, 10]

 

# initializing repl char

repl_char = '*'

 

# Multiple indices Replace in String

# Using loop + join()

temp = list(test_str)

for idx in test_list:

 temp[idx] = repl_char

res = ''.join(temp)

 

# printing result 

print("The String after performing replace : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : geeksforgeeks is best
    The String after performing replace : ge*k*fo*ge*ks is best
    

**Method #2 : Using list comprehension +join()**  
The combination of above functions can also be used to perform this task. In
this, we perform similar task as above, just in one liner format using list
comprehension.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Multiple indices Replace in String

# Using list comprehension + join()

 

# initializing string

test_str = 'geeksforgeeks is best'

 

# printing original string

print("The original string is : " + test_str)

 

# initializing list 

test_list = [2, 4, 7, 10]

 

# initializing repl char

repl_char = '*'

 

# Multiple indices Replace in String

# Using list comprehension + join()

temp = list(test_str)

res = [repl_char if idx in test_list else ele for idx,
ele in enumerate(temp)]

res = ''.join(res)

 

# printing result 

print("The String after performing replace : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : geeksforgeeks is best
    The String after performing replace : ge*k*fo*ge*ks is best
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

