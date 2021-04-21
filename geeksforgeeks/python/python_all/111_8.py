Python – Rear element extraction from list of tuples records



While working with tuples, we store different data as different tuple
elements. Sometimes, there is a need to print specific information from the
tuple like rear index. For instance, a piece of code would want just names to
be printed of all the student data. Let’s discuss certain ways how one can
achieve solutions to this problem.

 **Method #1 : Using list comprehension**  
List comprehension is the simplest way in which this problem can be solved. We
can just iterate over only the rear index value in all the index and store it
in a list and print it after that.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Rear element extraction from Records

# using list comprehension 

 

# initializing list of tuples

test_list = [(1, 'Rash', 21), (2, 'Varsha', 20),
(3, 'Kil', 19)]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# using list comprehension to get names

# Rear element extraction from Records

res = [lis[-1] for lis in test_list]

 

# printing result

print ("List with only rear tuple element : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]
    List with only rear tuple element : [21, 20, 19]
    

**Method #2 : Usingmap() + itemgetter()**  
map() coupled with itemgetter() can perform this task in more simpler way.
map() maps all the element we access using itemgetter() and returns the
result.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Rear element extraction from Records

# using map() + itergetter()

from operator import itemgetter

 

# initializing list of tuples

test_list = [(1, 'Rash', 21), (2, 'Varsha', 20),
(3, 'Kil', 19)]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# using map() + itergetter() to get names

# Rear element extraction from Records

res = list(map(itemgetter(-1), test_list))

 

# printing result

print ("List with only rear tuple element : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]
    List with only rear tuple element : [21, 20, 19]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

