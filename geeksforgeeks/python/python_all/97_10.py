Python | Tuple Column element frequency



In python we need to handle various forms of data and one among them is list
of tuples in which we may have to perform any kind of operation. This
particular article discusses the ways of finding the frequency of the Kth
element in list of tuple. Let’s discuss certain ways in which this can be
performed.

 **Method #1 : Usingmap() + count()**  
The map function can be used to accumulate the indices of all the tuples in a
list and the task of counting the frequency can be done using the generic
count function of python library.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Tuple Column element frequency

# using map() + count()

 

# initializing list of tuples

test_list = [(1, 'Geeks'), (2, 'for'), (3,
'Geeks')]

 

# printing the original list

print ("The original list is : " + str(test_list))

 

# initializing K 

K = 1

 

# using map() + count()

# Tuple Column element frequency

res = list(map(lambda i : i[K], test_list)).count('Geeks')

 

# printing result

print ("The frequency of element at Kth index is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(1, 'Geeks'), (2, 'for'), (3, 'Geeks')]
    The frequency of element at Kth index is : 2
    

**Method #2 : UsingCounter() \+ list comprehension**  
List comprehension performs the task of getting the Kth element of the tuples
and the counting part is handled by Counter function of collection library.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Tuple Column element frequency

# using Counter() + list comprehension

from collections import Counter

 

# initializing list of tuples

test_list = [(1, 'Geeks'), (2, 'for'), (3,
'Geeks')]

 

# printing the original list

print ("The original list is : " + str(test_list))

 

# initializing K 

K = 1

 

# using Counter() + list comprehension

# Tuple Column element frequency

res = Counter(i[K] for i in test_list)

 

# printing result

print ("The frequency of element at Kth index is : " +
str(res['Geeks']))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(1, 'Geeks'), (2, 'for'), (3, 'Geeks')]
    The frequency of element at Kth index is : 2
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

