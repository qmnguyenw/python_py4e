Python | Add substring at specific index



In Python, String is immutable datatype, what this means is, that there are
lot many restrictions when one handles its manipulation. The problem of adding
something at a position at string is not possible, without the list
reconstruction. Let’s discuss certain ways in which this task can be
performed.

 **Method #1 : Using list slicing**

This task can be performed using the list slicing. In this, we just slice the
list into two parts, breaking at the target position and then rejoining it
after inserting target substring at middle.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Add substring at specific index

# using list slicing

 

# initializing string

test_string = 'geeksgeeks'

 

# initializing add_string

add_string = "for"

 

# printing original string 

print("The original string : " + test_string)

 

# printing add string 

print("The add string : " + add_string)

 

# initializing N 

N = 5

 

# using list slicing

# Add substring at specific index 

res = test_string[ : N] + add_string + test_string[N : ]

 

# print result

print("The string after performing addition : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : geeksgeeks
    The add string : for
    The string after performing addition : geeksforgeeks
    

  

  

**Method #2 : Usingjoin() + list() + insert()**

Another possible hack that can be performed in for the following problem is
that converting the string to list and then adding the string at particular
position and then performing the join.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Add substring at specific index

# using join() + list() + insert()

 

# initializing string

test_string = 'geeksgeeks'

 

# initializing add_string

add_string = "for"

 

# printing original string 

print("The original string : " + test_string)

 

# printing add string 

print("The add string : " + add_string)

 

# initializing N 

N = 5

 

# using join() + list() + insert()

# Add substring at specific index 

res = list(test_string)

res.insert(N, add_string)

res = ''.join(res)

 

# print result

print("The string after performing addition : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : geeksgeeks
    The add string : for
    The string after performing addition : geeksforgeeks
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

