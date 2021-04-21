Python – Alternate Minimum element in list



Some of the list operations are quite general and having shorthands without
needing to formulate a multiline code is always required. Wanting to construct
the list consisting of all the alternate elements of the original list is a
problem that one developer faces in day-day applications and sometimes require
to find minimum of these alternate elements. Lets discuss certain ways in
which this can be performed.

 **Method #1 : Using list comprehension +min()**  
Shorthand to the naive method, list comprehension provides a faster way to
perform this particular task. In this method, all the indices which are not
multiple of 2, hence odd are inserted in the new list. Then the minimum is
extrated using min().

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# Alternate elements Minimimum

# using list comprehension + min()

 

# initializing list 

test_list = [1, 4, 6, 7, 9, 3, 5]

 

# printing original list 

print ("The original list : " + str(test_list))

 

# using list comprehension + min()

# Alternate elements Minimimum

res = min([test_list[i] for i in range(len(test_list))
if i % 2 != 0])

 

# printing result 

print ("The alternate element list minimum is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [1, 4, 6, 7, 9, 3, 5]
    The alternate element list minimum is : 3
    

**Method #2 : Usingenumerate() + min()**  
This is just a variation to the list comprehension method but does the similar
internal working as list comprehension but uses different variables to keep
track of index along with its value. Then the minimum is extrated using min().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# Alternate elements Minimimum

# using enumerate() + min()

 

# initializing list 

test_list = [1, 4, 6, 7, 9, 3, 5]

 

# printing original list 

print ("The original list : " + str(test_list))

 

# using enumerate() + min()

# Alternate elements Minimimum

res = min([i for j, i in enumerate(test_list) if j %
2 != 0])

 

# printing result 

print ("The alternate element list minimum is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [1, 4, 6, 7, 9, 3, 5]
    The alternate element list minimum is : 3
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

