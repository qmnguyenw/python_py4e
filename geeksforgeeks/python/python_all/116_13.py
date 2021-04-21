Python | Retain K consecutive elements



Sometimes while working with data, we can have a problem in which we need to
select some of the elements that occur K times consecutively. This problem can
occur in many domains. Let’s discuss certain ways in which this problem can be
solved.

 **Method #1 : Usinggroupby() \+ list comprehension**  
This task can be performed using above functionalities. In this, we group all
the numbers that are occurring K consecutively. We iterate the list using list
comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Retain K consecutive elements

# using groupby() + list comprehension

from itertools import groupby

 

# initialize list 

test_list = [1, 1, 4, 5, 5, 6, 7, 7,
8]

 

# printing original list 

print("The original list : " + str(test_list))

 

# initialize K 

K = 2

 

# Retain K consecutive elements

# using groupby() + list comprehension

res = [i for i, j in groupby(test_list) if len(list(j))
== K]

 

# printing result

print("The K consecutive elements are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [1, 1, 4, 5, 5, 6, 7, 7, 8]
    The K consecutive elements are : [1, 5, 7]
    

**Method #2 : Using list comprehension +slice() + groupby()**  
This task can also be performed using above functions. In this, we just
perform grouping in similar way as above but the way we extract consecutive
elements is by slice().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Retain K consecutive elements

# using groupby() + list comprehension + islice()

from itertools import groupby, islice

 

# initialize list 

test_list = [1, 1, 4, 5, 5, 6, 7, 7,
8]

 

# printing original list 

print("The original list : " + str(test_list))

 

# initialize K 

K = 2

 

# Retain K consecutive elements

# using groupby() + list comprehension + islice()

res = [i for i, j in groupby(test_list) if
len(list(islice(j, 0, K))) == K]

 

# printing result

print("The K consecutive elements are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [1, 1, 4, 5, 5, 6, 7, 7, 8]
    The K consecutive elements are : [1, 5, 7]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

