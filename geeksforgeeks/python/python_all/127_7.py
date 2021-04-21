Python | Nth Column vertical string in Matrix



Sometimes, while working with Python Matrix, we can have a problem in which we
need to access the Matrix in vertical form and extract strings from same, that
too as a string, not merely as a list of characters. This task has it’s
application in gaming in which we need to extract string during crosswords.
Let’s discuss a way in which this task can be performed.

 **Method : Using list comprehension +join()**  
We achieve the task in this method in 2 steps. In 1st step the Nth column
elements are extracted using list comprehension. In 2nd step, these elements
are joined together to perform the characters to string conversion.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Nth Column vertical string in Matrix

# Using join() + list comprehension

 

# initializing list 

test_list = [('a', 'g', 'v'), ('e', 'f', 8),
('b', 'g', 0)]

 

# printing list 

print("The original list : " + str(test_list))

 

# initializing Nth column

N = 1

 

# Nth Column vertical string in Matrix

# Using join() + list comprehension

temp = [sub[N] for sub in test_list]

res = "".join(temp)

 

# Printing result

print("Constructed vertical string : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
     
    The original list : [('a', 'g', 'v'), ('e', 'f', 8), ('b', 'g', 0)]
    Constructed vertical string : gfg
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

