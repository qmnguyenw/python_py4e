Python – Concatenation of two String Tuples



Sometimes, while working with records, we can have a problem in which we may
need to perform String concatenation of tuples. This problem can occur in day-
day programming. Let’s discuss certain ways in which this task can be
performed.

 **Method #1 : Usingzip() \+ generator expression**  
The combination of above functions can be used to perform this task. In this,
we perform the task of String concatenation using generator expression and
mapping index of each tuple is done by zip().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Tuple String concatenation

# using zip() + generator expression 

 

# initialize tuples 

test_tup1 = ("Manjeet", "Nikhil", "Akshat") 

test_tup2 = (" Singh", " Meherwal", " Garg") 

 

# printing original tuples 

print("The original tuple 1 : " + str(test_tup1)) 

print("The original tuple 2 : " + str(test_tup2)) 

 

# Tuple String concatenation

# using zip() + generator expression 

res = tuple(ele1 + ele2 for ele1, ele2 in zip(test_tup1,
test_tup2)) 

 

# printing result 

print("The concatenated tuple : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original tuple 1 : ('Manjeet', 'Nikhil', 'Akshat')
    The original tuple 2 : (' Singh', ' Meherwal', ' Garg')
    The concatenated tuple : ('Manjeet Singh', 'Nikhil Meherwal', 'Akshat Garg')
    

**Method #2 : Usingmap() \+ concat**  
The combination of above functionalities can also perform this task. In this,
we perform the task of extending logic of concatenation using concat and
mapping is done by map().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Tuple String concatenation 

# using map() + concat

from operator import concat 

 

# initialize tuples 

test_tup1 = ("Manjeet", "Nikhil", "Akshat") 

test_tup2 = (" Singh", " Meherwal", " Garg")

 

# printing original tuples 

print("The original tuple 1 : " + str(test_tup1)) 

print("The original tuple 2 : " + str(test_tup2)) 

 

# Tuple String concatenation

# using map() + concat

res = tuple(map(concat, test_tup1, test_tup2)) 

 

# printing result 

print("The concatenated tuple : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original tuple 1 : ('Manjeet', 'Nikhil', 'Akshat')
    The original tuple 2 : (' Singh', ' Meherwal', ' Garg')
    The concatenated tuple : ('Manjeet Singh', 'Nikhil Meherwal', 'Akshat Garg')
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

