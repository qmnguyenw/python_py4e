Python – Find minimum k records from tuple list



Sometimes, while working with data, we can have a problem in which we have
records and we require to find the lowest K scores from it. This kind of
application is popular in web development domain. Let’s discuss certain ways
in which this problem can be solved.

 **Method #1 : Using sorted() \+ lambda**  
The combination of above functionality can be used to perform this particular
task. In this, we just employ sorted function, and print the lowest K elements
using list slicing.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Minimum K records

# Using sorted() + lambda

 

# Initializing list 

test_list = [('Manjeet', 10), ('Akshat', 4),
('Akash', 2), ('Nikhil', 8)]

 

# Initializing K

K = 2

 

# printing original list

print("The original list is : " + str(test_list))

 

# Minimum K records

# Using sorted() + lambda

res = sorted(test_list, key = lambda x: x[1])[:K]

 

# printing result

print("The lowest K records are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)]
    The lowest K records are : [('Akash', 2), ('Akshat', 4)]
    

**Method #2 : Usingsorted() + itemgetter()**  
The combination of above functions can also be used to perform this particular
task. In this, the task performed by lambda function is performed by
itemgetter() is used to get the index in tuple which has to be included in
calculations.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Minimum K records

# Using sorted() + itemgetter()

from operator import itemgetter

 

# Initializing list 

test_list = [('Manjeet', 10), ('Akshat', 4),
('Akash', 2), ('Nikhil', 8)]

 

# Initializing K

K = 2

 

# printing original list

print("The original list is : " + str(test_list))

 

# Minimum K records

# Using sorted() + itemgetter()

res = sorted(test_list, key = itemgetter(1))[:K]

 

# printing result

print("The lowest K records are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)]
    The lowest K records are : [('Akash', 2), ('Akshat', 4)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

