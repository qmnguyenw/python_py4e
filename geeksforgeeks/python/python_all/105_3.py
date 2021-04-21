Python – Filter Range Length Tuples



Sometimes, while working with records, we might desire to filter records in
such a way in which we need to discard records that do not contains exact
number of elements required to constitute a record and lie in a range. Let’s
discuss certain ways in which this task can be performed.

 **Method #1 : Using list comprehension +len()**  
In this method, we just iterate through the list and discard the tuples that
do not match the matching range length required to constitute the record. The
computation of length is done by len().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter Range Length Tuples

# Using list comprehension + len()

 

# Initializing list

test_list = [(4, ), (5, 6), (2, 3, 5), (5,
6, 8, 2), (5, 9)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing desired lengths 

i, j = 2, 3

 

# Filter Range Length Tuples

# Using list comprehension + len()

res = [sub for sub in test_list if len(sub) >= i and
len(sub) <= j]

 

# printing result

print("The tuple list after filtering range records : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(4, ), (5, 6), (2, 3, 5), (5, 6, 8, 2), (5, 9)]
    The tuple list after filtering range records : [(5, 6), (2, 3, 5), (5, 9)]
    

**Method #2 : Usingfilter() + lambda + len()**  
The combination of above functions can also be used to perform this particular
task. In this, we just use filter() and use lambda function to filter range
length records.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter Range Length Tuples

# Using filter() + lambda + len()

 

# Initializing list

test_list = [(4, ), (5, 6), (2, 3, 5), (5,
6, 8, 2), (5, 9)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing desired lengths 

i, j = 2, 3

 

# Filter Range Length Tuples

# Using filter() + lambda + len()

res = list(filter(lambda ele: len(ele) >= i and
len(ele) <= j, test_list))

 

# printing result

print("The tuple list after filtering range records : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(4, ), (5, 6), (2, 3, 5), (5, 6, 8, 2), (5, 9)]
    The tuple list after filtering range records : [(5, 6), (2, 3, 5), (5, 9)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

