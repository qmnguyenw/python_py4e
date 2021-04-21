Python | Search elements in a Matrix



Python supports a list as its list element and hence a matrix can be formed.
Sometimes we might have a utility in which we require to perform a search in
that list of list i.e matrix and its a very common in all the domains of
coding. Let’s discuss certain ways in which this can be performed.

 **Method #1 : Usingany() \+ list comprehension**  
The any function can be used to perform the task of if condition and the check
for each element in the nested list can be computed using the list
comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Search in Matrix

# using any() + list comprehension

 

# initializing list

test_list = [[4, 5, 6],

 [10, 2, 13],

 [1, 11, 18]]

 

# printing original list 

print("The original list : " + str(test_list))

 

# using any() + list comprehension

# to Search in Matrix

res = any(13 in sub for sub in test_list)

 

# printing result

print("Is 13 present in Matrix ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [[4, 5, 6], [10, 2, 13], [1, 11, 18]]
    Is 13 present in Matrix ? : True
    

**Method #2 : Using set.issubset() + itertools.chain()**  
The issubset method can be used to check for the membership in sublist and
chain function can be used to perform this task for the each element in the
Matrix, in a faster way as it works on iterators.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Search in Matrix

# using set.issubset() + itertools.chain()

from itertools import chain

 

# initializing list

test_list = [[4, 5, 6],

 [10, 2, 13],

 [1, 11, 18]]

 

# printing original list 

print("The original list : " + str(test_list))

 

# using set.issubset() + itertools.chain()

# to Search in Matrix

res = {13}.issubset(chain.from_iterable(test_list))

 

# printing result

print("Is 13 present in Matrix ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [[4, 5, 6], [10, 2, 13], [1, 11, 18]]
    Is 13 present in Matrix ? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

