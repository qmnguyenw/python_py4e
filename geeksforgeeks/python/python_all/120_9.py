Python | Convert tuple to adjacent pair dictionary



Sometimes, while working with records, we can have a problem in which we have
data and need to convert to key-value dictionary using adjacent elements. This
problem can have application in web development domain. Let’s discuss certain
ways in which this task can be performed.

 **Method #1 : Usingdict() \+ dictionary comprehension + slicing**  
The above functionalities can be used to solve this problem. In this, we just
slice alternate parts of tuple and assign corresponding values using
dictionary comprehension. The result is converted to dictionary using
dict().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert tuple to adjacent pair dictionary

# using dict() + dictionary comprehension + slicing

 

# initialize tuple

test_tup = (1, 5, 7, 10, 13, 5)

 

# printing original tuple

print("The original tuple : " + str(test_tup))

 

# Convert tuple to adjacent pair dictionary

# using dict() + dictionary comprehension + slicing

res = dict(test_tup[idx : idx + 2] for idx in
range(0, len(test_tup), 2))

 

# printing result

print("Dictionary converted tuple : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple : (1, 5, 7, 10, 13, 5)
    Dictionary converted tuple : {1: 5, 13: 5, 7: 10}
    

**Method #2 : Usingdict() + zip() \+ slicing**  
This performs this task in similar way as above method. The difference is that
it uses zip() instead of dictionary comprehension to perform task of pairing
key-value pair.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert tuple to adjacent pair dictionary

# using dict() + zip() + slicing

 

# initialize tuple

test_tup = (1, 5, 7, 10, 13, 5)

 

# printing original tuple

print("The original tuple : " + str(test_tup))

 

# Convert tuple to adjacent pair dictionary

# using dict() + zip() + slicing

res = dict(zip(test_tup[::2], test_tup[1::2]))

 

# printing result

print("Dictionary converted tuple : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple : (1, 5, 7, 10, 13, 5)
    Dictionary converted tuple : {1: 5, 13: 5, 7: 10}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

