Python – Cross list exponentiation



Sometimes we come across the situations in which we require to apply a
particular function to each element of two lists at similar indices. These are
quite similar and come up as an application for certain utilities. Let’s
discuss certain ways in which the exponentiation, i.e remainder of two lists
can be performed.

 **Method #1 : Usingzip() \+ list comprehension**  
The zip operation can be used to link one list with the other and the
computation part can be handled by the list comprehension and hence providing
a shorthand to this particular problem.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Cross list exponentiation

# using zip() + list comprehension

 

# initializing lists 

test_list1 = [3, 5, 2, 6, 4]

test_list2 = [7, 3, 4, 1, 5]

 

# printing original lists 

print ("The original list 1 is : " + str(test_list1))

print ("The original list 2 is : " + str(test_list2))

 

# Cross list exponentiation

# using zip() + list comprehension

res = [i ** j for i, j in zip(test_list1, test_list2)]

 

# printing result

print ("The cross exponentiation list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : [3, 5, 2, 6, 4]
    The original list 2 is : [7, 3, 4, 1, 5]
    The cross exponentiation list is : [2187, 125, 16, 6, 1024]
    

**Method #2 : Usingmap()**  
Using map function is the most elegant way in which we can possibly perform
the twining of a function with both the lists. Different operations other than
exponentiation can also be applied over it.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Cross list exponentiation

# using map()

from operator import pow

 

# initializing lists 

test_list1 = [3, 5, 2, 6, 4]

test_list2 = [7, 3, 4, 1, 5]

 

# printing original lists 

print ("The original list 1 is : " + str(test_list1))

print ("The original list 2 is : " + str(test_list2))

 

# Cross list exponentiation

# using map()

res = list(map(pow, test_list1, test_list2))

 

# printing result

print ("The cross exponentiation list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : [3, 5, 2, 6, 4]
    The original list 2 is : [7, 3, 4, 1, 5]
    The cross exponentiation list is : [2187, 125, 16, 6, 1024]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

