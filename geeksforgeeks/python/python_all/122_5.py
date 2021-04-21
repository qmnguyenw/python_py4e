Python | Repeating tuples N times



Sometimes, while working with data, we might have a problem in which we need
to replicate, i.e construct duplicates of tuples. This is important
application in many domains of computer programming. Let’s discuss certain
ways in which this task can be performed.

 **Method #1 : Using* operator**  
The multiplication operator can be used to construct the duplicates of a
container. This also can be extended to tuples even though tuples are
immutable.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Repeating tuples N times

# using * operator

 

# initialize tuple 

test_tup = (1, 3)

 

# printing original tuple 

print("The original tuple : " + str(test_tup))

 

# initialize N 

N = 4

 

# Repeating tuples N times

# using * operator

res = ((test_tup, ) * N)

 

# printing result

print("The duplicated tuple elements are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple : (1, 3)
    The duplicated tuple elements are : ((1, 3), (1, 3), (1, 3), (1, 3))
    

**Method #2 : Using repeat()**  
The internal function of itertools library, repeat() can be used to achieve
the solution to the above problem.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Repeating tuples N times

# using repeat()

from itertools import repeat

 

# initialize tuple 

test_tup = (1, 3)

 

# printing original tuple 

print("The original tuple : " + str(test_tup))

 

# initialize N 

N = 4

 

# Repeating tuples N times

# using repeat()

res = tuple(repeat(test_tup, N))

 

# printing result

print("The duplicated tuple elements are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple : (1, 3)
    The duplicated tuple elements are : ((1, 3), (1, 3), (1, 3), (1, 3))
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

