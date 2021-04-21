Python | Chunk Tuples to N



Sometimes, while working with data, we can have a problem in which we may need
to perform chunking of tuples each of size N. This is popular in applications
in which we need to supply data in chunks. Let’s discuss certain ways in which
this task can be performed.

 **Method #1 : Using list comprehenion**  
This is brute and shorthand method to perform this task. In this, we split the
N elements at a time and construct a new tuple for them.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Chunk Tuples to N

# using list comprehension

 

# initialize tuple

test_tup = (10, 4, 5, 6, 7, 6, 8, 3,
4)

 

# printing original tuple

print("The original tuple : " + str(test_tup))

 

# initialize N 

N = 3

 

# Chunk Tuples to N

# using list comprehension

res = [test_tup[i : i + N] for i in range(0,
len(test_tup), N)]

 

# printing result

print("The tuples after chunking are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple : (10, 4, 5, 6, 7, 6, 8, 3, 4)
    The tuples after chunking are : [(10, 4, 5), (6, 7, 6), (8, 3, 4)]
    

**Method #2 : Usingzip() + iter()**  
The combination of above functions can also be used to solve this problem. In
this, we use zip() to combine chunks and iter() converts to suitable format.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Chunk Tuples to N

# using zip() + iter()

 

# initialize tuple

test_tup = (10, 4, 5, 6, 7, 6, 8, 3,
4)

 

# printing original tuple

print("The original tuple : " + str(test_tup))

 

# initialize N 

N = 3

 

# Chunk Tuples to N

# using zip() + iter()

temp = [iter(test_tup)] * N

res = list(zip(*temp))

 

# printing result

print("The tuples after chunking are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple : (10, 4, 5, 6, 7, 6, 8, 3, 4)
    The tuples after chunking are : [(10, 4, 5), (6, 7, 6), (8, 3, 4)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

