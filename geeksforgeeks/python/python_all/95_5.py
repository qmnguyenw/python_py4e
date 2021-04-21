Python – Concatenate Kth element in Tuple List



While working with tuples, we store different data as different tuple
elements. Sometimes, there is a need to print a specific information from the
tuple. For instance, a piece of code would want just names to be printed of
all the student data in concatenated format. Lets discuss certain ways how one
can achieve solutions to this problem.

 **Method #1 : Using list comprehension + join()**  
List comprehension is the simplest way in which this problem can be solved. We
can just iterate over only the specific index value in all the index and store
it in a list and concat it after that using join().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Concatenating Kth element in Tuple List

# using list comprehension 

 

# initializing list of tuples

test_list = [(1, 'Rash', 21), (2, 'Varsha', 20),
(3, 'Kil', 19)]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# initializing K 

K = 1

 

# using list comprehension + join() to concatenate names

res = " ".join([lis[K] for lis in test_list])

 

# printing result

print ("String with only Kth tuple element (i.e names) concatenated : "
+ str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]
    String with only Kth tuple element (i.e names) concatenated : Rash Varsha Kil
    

**Method #2 : Usingmap() + itemgetter() + join()**  
map() coupled with itemgetter() can perform this task in more simpler way.
map() maps all the element we access using itemgetter() and returns the
result. The task of concatenation is performed using join().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Concatenating Kth element in Tuple List

# using map() + itergetter() + join()

from operator import itemgetter

 

# initializing list of tuples

test_list = [(1, 'Rash', 21), (2, 'Varsha', 20),
(3, 'Kil', 19)]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# initializing K 

K = 1

 

# using map() + itergetter() + join() to get names

res = " ".join(list(map(itemgetter(K), test_list)))

 

# printing result

print ("String with only nth tuple element (i.e names) concatenated : "
+ str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]
    String with only Kth tuple element (i.e names) concatenated : Rash Varsha Kil
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

