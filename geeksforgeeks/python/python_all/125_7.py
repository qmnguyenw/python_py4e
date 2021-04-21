Python | Retain records of specific length



Sometimes, while working with records, we might desire to filter records in
such a way in which we need to discard records that do not contains exact
number of elements required to constitute a record. Let’s discuss certain ways
in which this task can be performed.

 **Method #1 : Using list comprehension +len()**  
In this method, we just iterate through the list and discard the tuples that
do not match the matching length required to constitute the record. The
computation of length is done by len().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Retain records of specific length

# Using list comprehension + len()

 

# Initializing list

test_list = [(4, 5, 6), (5, 6), (2, 3,
5), (5, 6, 8), (5, 9)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing desired length 

N = 3

 

# Retain records of specific length

# Using list comprehension + len()

res = [sub for sub in test_list if len(sub) == 3]

 

# printing result

print("The tuple list after removing uneven records: " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(4, 5, 6), (5, 6), (2, 3, 5), (5, 6, 8), (5, 9)]
    The tuple list after removing uneven records: [(4, 5, 6), (2, 3, 5), (5, 6, 8)]
    

**Method #2 : Usingfilter() \+ lambda + len()**  
The combination of above functions can also be used to perform this particular
task. In this, we just use filter() and use lambda function to separate
uneven length records.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Retain records of specific length

# Using filter() + lambda + len()

 

# Initializing list

test_list = [(4, 5, 6), (5, 6), (2, 3,
5), (5, 6, 8), (5, 9)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing desired length 

N = 3

 

# Retain records of specific length

# Using filter() + lambda + len()

res = list(filter(lambda ele: len(ele) == N,
test_list))

 

# printing result

print("The tuple list after removing uneven records: " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(4, 5, 6), (5, 6), (2, 3, 5), (5, 6, 8), (5, 9)]
    The tuple list after removing uneven records: [(4, 5, 6), (2, 3, 5), (5, 6, 8)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

