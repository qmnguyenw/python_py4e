Python – Get maximum of Nth column from tuple list



Sometimes, while working with Python list, we can have a task in which we need
to work with tuple list and get the maximum of it’s Nth index. This problem
has application in web development domain while working with data
informations. Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Using list comprehension +max()**  
This task can be performed using the combination of above functionalities. In
this, maximum of index occurs using max() and list comprehension drives the
iteration and access of Nth index element of each tuple in list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Nth column Maximum in tuple list

# using list comprehension + max()

 

# initialize list

test_list = [(5, 6, 7), (1, 3, 5), (8, 9,
19)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initialize N

N = 2

 

# Nth column Maximum in tuple list

# using list comprehension + max()

res = max([sub[N] for sub in test_list])

 

# printing result

print("Maximum of Nth Column of Tuple List : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(5, 6, 7), (1, 3, 5), (8, 9, 19)]
    Maximum of Nth Column of Tuple List : 19
    

**Method #2 : Usingimap() + max() + itemgetter()**  
The combination of above functions can also achieve this task. This approach
is generator based and recommended in case we have a very large list. In this,
max() is used to perform maximum, itemgetter to get Nth index and imap()
performs the task of mapping elements to extract max. Works only in Python2.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# Nth column Maximum in tuple list

# using imap() + max() + itemgetter()

from operator import itemgetter

from itertools import imap

 

# initialize list

test_list = [(5, 6, 7), (1, 3, 5), (8, 9,
19)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initialize N

N = 2

 

# Nth column Maximum in tuple list

# using imap() + max() + itemgetter()

idx = itemgetter(N)

res = max(imap(idx, test_list))

 

# printing result

print("Maximum of Nth Column of Tuple List : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(5, 6, 7), (1, 3, 5), (8, 9, 19)]
    Maximum of Nth Column of Tuple List : 19
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

