Python | Summation of tuples in list



Sometimes, while working with records, we can have a problem in which we need
to find the cummulative sum of all the values that are present in tuples. This
can have application in cases in which we deal with a lot of records data.
Let’s discuss certain ways in which this problem can be solved.

 **Method #1 : Usingsum() + map()**  
Combination of above functions can be used to solve this particular problem.
In this the task of summation is performed by sum(), and applying the
summation functionality to each element in tuple list is performed by map().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Summation of tuples in list

# using sum() + map()

 

# initialize list of tuple

test_list = [(1, 3), (5, 6, 7), (2, 6)]

 

# printing original tuples list

print("The original list : " + str(test_list))

 

# Summation of tuples in list

# using sum() + map()

res = sum(map(sum, test_list))

 

# printing result

print("The summation of all tuple elements are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(1, 3), (5, 6, 7), (2, 6)]
    The summation of all tuple elements are : 30
    

**Method #2 : Using sum() + izip()**  
The combination of above functions can be used to perform this particular
task. In this, we perform the task of map() using izip(). It helps to club
all the elements for summation by sum(). Works only for single element tuple
and only with Python2.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Summation of tuples in list

# using sum() + izip()

from itertools import izip

 

# initialize list of tuple

test_list = [(1, ), (5, ), (2, )]

 

# printing original tuples list

print("The original list : " + str(test_list))

 

# Summation of tuples in list

# using sum() + map()

res = sum(*izip(*test_list))

 

# printing result

print("The summation of all tuple elements are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(1, ), (5, ), (2, )]
    The summation of all tuple elements are : 8
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

