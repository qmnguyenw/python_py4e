Python | Non-Repeating value Summation in Matrix



Sometimes we need to find the unique values in a list, that is comparatively
easy and its summation and has been discussed earlier. But we can also get a
matrix as input i.e a list of lists, finding unique in them are discussed in
this article. Let’s see certain ways in which this can be achieved.

 **Method #1 : Usingset() + list comprehension + sum()**  
The set function can be used to convert the individual list to a non-repeating
element list and the list comprehension is used to iterate to each of the
lists. The task of performing summation is performed using sum().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Non-Repeating value Summation in Matrix

# set() + list comprehension + sum()

 

# initializing matrix 

test_matrix = [[1, 3, 1], [4, 5, 3], [1,
2, 4]]

 

# printing the original matrix

print ("The original matrix is : " + str(test_matrix))

 

# using set() + list comprehension + sum()

# Non-Repeating value Summation in Matrix

res = sum(list(set(i for j in test_matrix for i
in j)))

 

# printing result

print ("Unique values summation in matrix are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original matrix is : [[1, 3, 1], [4, 5, 3], [1, 2, 4]]
    Unique values summation in matrix are : 15
    

**Method #2 : Usingchain() + set() + sum()**  
The chain function performs the similar task that a list comprehension
performs but in a faster way as it uses iterators for its internal processing
and hence faster. The task of performing summation is performed using sum().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Non-Repeating value Summation in Matrix

# chain() + set() + sum()

from itertools import chain

 

# initializing matrix 

test_matrix = [[1, 3, 1], [4, 5, 3], [1,
2, 4]]

 

# printing the original matrix

print ("The original matrix is : " + str(test_matrix))

 

# using chain() + set() + sum()

# Non-Repeating value Summation in Matrix

res = sum(list(set(chain(*test_matrix))))

 

# printing result

print ("Unique values summation in matrix are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original matrix is : [[1, 3, 1], [4, 5, 3], [1, 2, 4]]
    Unique values summation in matrix are : 15
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

