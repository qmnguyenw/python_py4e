Python – Records with Value at K index



Sometimes, while working with records, we might have a problem in which we
need to find all the tuples of elements for a particular value at a particular
Kth position of tuple. This seems to be a peculiar problem but while working
with many keys in records, we encounter this problem. Let’s discuss certain
ways in which this problem can be solved.

 **Method #1 : Using loop**  
This is the brute force method by which this problem can be solved. In this we
keep a check and append to list if we find specific record at Kth position in
tuple.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Records with Value at K index

# Using loop

 

# initialize list 

test_list = [(3, 1, 5), (1, 3, 6), (2, 5,
7), (5, 2, 8), (6, 3, 0)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initialize ele 

ele = 3

 

# initialize K 

K = 1

 

# Records with Value at K index

# Using loop

# using y for K = 1 

res = []

for x, y, z in test_list:

 if y == ele:

 res.append((x, y, z))

 

# printing result

print("The tuples of element at Kth position : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(3, 1, 5), (1, 3, 6), (2, 5, 7), (5, 2, 8), (6, 3, 0)]
    The tuples of element at Kth position : [(1, 3, 6), (6, 3, 0)]
    

**Method #2 : Usingenumerate() \+ list comprehension**  
The combination of above functions can be used to solve this problem. In this,
we enumerate for the indices using enumerate(), rest is performed as in above
method but in compact way.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Records with Value at K index

# Using enumerate() + list comprehension

 

# initialize list 

test_list = [(3, 1, 5), (1, 3, 6), (2, 5,
7), (5, 2, 8), (6, 3, 0)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initialize ele 

ele = 3

 

# initialize K 

K = 1

 

# Records with Value at K index

# Using enumerate() + list comprehension

res = [b for a, b in enumerate(test_list) if b[K] ==
ele]

 

# printing result

print("The tuples of element at Kth position : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(3, 1, 5), (1, 3, 6), (2, 5, 7), (5, 2, 8), (6, 3, 0)]
    The tuples of element at Kth position : [(1, 3, 6), (6, 3, 0)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

