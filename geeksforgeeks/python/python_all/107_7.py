Python – Cumulative Records Product



Sometimes, while working with data in form of records, we can have a problem
in which we need to find the product element of all the records received. This
is a very common application that can occur in Data Science domain. Let’s
discuss certain ways in which this task can be performed.

 **Method #1 : Using loop + generator expression**  
This is the most basic method to achieve solution to this task. In this, we
iterate over whole nested lists using generator expression and get the product
element using explicit product function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Cummulative Records Product

# using loop + generator expression

 

# getting Product

def prod(val) :

 res = 1

 for ele in val:

 res *= ele

 return res 

 

# initialize list 

test_list = [(2, 4), (6, 7), (5, 1), (6,
10), (8, 7)]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Cummulative Records Product

# using loop + generator expression

res = prod(int(j) for i in test_list for j in i)

 

# printing result

print("The Cummulative product of list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(2, 4), (6, 7), (5, 1), (6, 10), (8, 7)]
    The Cummulative product of list is : 5644800
    

**Method #2 : Using loop + map() + chain.from_iterable()**  
The combination of above methods can also be used to perform this task. In
this, the extension of finding product is done by combination of map() and
from_iterable().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Cummulative Records Product

# using product + map() + chain.from_iterable()

from itertools import chain

 

# getting Product

def prod(val) :

 res = 1

 for ele in val:

 res *= ele

 return res 

 

# initialize list 

test_list = [(2, 4), (6, 7), (5, 1), (6,
10), (8, 7)]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Cummulative Records Product

# using product + map() + chain.from_iterable()

res = prod(map(int, chain.from_iterable(test_list)))

 

# printing result

print("The cummulative product of list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(2, 4), (6, 7), (5, 1), (6, 10), (8, 7)]
    The Cummulative product of list is : 5644800
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

