Python | Summation of Kth Column of Tuple List



Sometimes, while working with Python list, we can have a task in which we need
to work with tuple list and get the possible accumulation of it’s Kth index.
This problem has application in web development domain while working with data
informations. Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Using list comprehension +sum()**  
This task can be performed using the combination of above functionalities. In
this, summation of index occurs using sum() and list comprehension drives
the iteration and access of Nth index element of each tuple in list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Summation of Kth Column of Tuple List

# using list comprehension + sum()

 

# initialize list

test_list = [(5, 6, 7), (1, 3, 5), (8, 9,
19)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initialize K

K = 2

 

# Summation of Kth Column of Tuple List

# using list comprehension + sum()

res = sum([sub[K] for sub in test_list])

 

# printing result

print("Summation of Kth Column of Tuple List : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(5, 6, 7), (1, 3, 5), (8, 9, 19)]
    Summation of Kth Column of Tuple List : 31
    

**Method #2 : Usingimap() + sum() + itemgetter()**  
The combination of above functions can also achieve this task. This approach
is generator based and recommended in case we have a very large list. In this,
sum() is used to perform summation, itemgetter to get Kth index and imap()
performs the task of mapping elements to perform summation. Works only in
Python2.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# Summation of Kth Column of Tuple List

# using imap() + sum() + itemgetter()

from operator import itemgetter

from itertools import imap

 

# initialize list

test_list = [(5, 6, 7), (1, 3, 5), (8, 9,
19)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initialize K

K = 2

 

# Summation of Kth Column of Tuple List

# using imap() + sum() + itemgetter()

idx = itemgetter(K)

res = sum(imap(idx, test_list))

 

# printing result

print("Summation of Kth Column of Tuple List : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(5, 6, 7), (1, 3, 5), (8, 9, 19)]
    Summation of Kth Column of Tuple List : 31
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

