Python – Kth Valid String



Sometimes while dealing with data science, we need to handle a large amount of
data and hence we may require shorthands to perform certain tasks. We handle
the Null values at preprocessing stage and hence sometimes require to check
for the Kth valid element. Let’s discuss certain ways in which we can find the
Kth Non-Empty String.

 **Method #1 : Usingnext() \+ list comprehension**  
The next function returns the iterator and hence its more efficient that
conventional list comprehension and the logic part is handled using list
comprehension which checks for the last None value.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Kth Valid String

# using next() + list comprehension

 

# initializing list

test_list = ["", "", "Akshat", "Nikhil"]

 

# printing original list 

print("The original list : " + str(test_list))

 

# initializing K 

K = 2

 

# using next() + list comprehension

# Kth Valid String

test_list = iter(test_list)

for idx in range(0, K):

 res = next(sub for sub in test_list if sub)

 

# printing result

print("The Kth non empty string is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['', '', 'Akshat', 'Nikhil']
    The Kth non empty string is : Nikhil
    

**Method #2 : Usingfilter()**  
The filter function can be used to find the Non empty strings and the Kth
index is returned to get the first string among those. Works only with Python
2.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# Kth Valid String

# using filter()

 

# initializing list

test_list = ["", "", "Akshat", "Nikhil"]

 

# printing original list 

print("The original list : " + str(test_list))

 

# initializing K 

K = 2

 

# using filter()

# Kth Valid String

res = filter(None, test_list)[K - 1]

 

# printing result

print("The Kth non empty string is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['', '', 'Akshat', 'Nikhil']
    The Kth non empty string is : Nikhil
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

