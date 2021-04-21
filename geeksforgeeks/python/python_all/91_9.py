Python | Nested Records Modulo



Sometimes, while working with records, we can have a problem in which we
require to perform index wise remainder of tuple elements. This can get
complicated with tuple elements to be tuple and inner elements again be tuple.
Let’s discuss certain ways in which this problem can be solved.

 **Method #1 : Usingzip() \+ nested generator expression**  
The combination of above functions can be used to perform the task. In this,
we combine the elements across tuples using zip(). The iterations and modulo
logic is provided by generator expression.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Nested Records Modulo

# using zip() + nested generator expression

 

# initialize tuples

test_tup1 = ((1, 3), (4, 5), (2, 9), (1,
10))

test_tup2 = ((6, 7), (3, 9), (1, 1), (7,
3))

 

# printing original tuples

print("The original tuple 1 : " + str(test_tup1))

print("The original tuple 2 : " + str(test_tup2))

 

# Nested Records Modulo

# using zip() + nested generator expression

res = tuple(tuple(a % b for a, b in zip(tup1,
tup2))\

 for tup1, tup2 in zip(test_tup1, test_tup2))

 

# printing result

print("The resultant tuple after modulo : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple 1 : ((1, 3), (4, 5), (2, 9), (1, 10))
    The original tuple 2 : ((6, 7), (3, 9), (1, 1), (7, 3))
    The resultant tuple after modulo : ((1, 3), (1, 5), (0, 0), (1, 1))
    

**Method #2 : Usingisinstance() + zip() \+ loop + list comprehension**  
The combination of above functions can be used to perform this particular
task. In this, we check for the nesting type and perform recursion. This
method can give flexibility of more than 1 level nesting.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Nested Records Modulo

# using isinstance() + zip() + loop + list comprehension

 

# function to perform task 

def tup_mod(tup1, tup2):

 if isinstance(tup1, (list, tuple)) and isinstance(tup2,
(list, tuple)):

 return tuple(tup_mod(x, y) for x, y in zip(tup1, tup2))

 return tup1 % tup2

 

# initialize tuples

test_tup1 = ((1, 3), (4, 5), (2, 9), (1,
10))

test_tup2 = ((6, 7), (3, 9), (1, 1), (7,
3))

 

# printing original tuples

print("The original tuple 1 : " + str(test_tup1))

print("The original tuple 2 : " + str(test_tup2))

 

# Nested Records Modulo

# using isinstance() + zip() + loop + list comprehension

res = tuple(tup_mod(x, y) for x, y in zip(test_tup1,
test_tup2))

 

# printing result

print("The resultant tuple after modulo : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple 1 : ((1, 3), (4, 5), (2, 9), (1, 10))
    The original tuple 2 : ((6, 7), (3, 9), (1, 1), (7, 3))
    The resultant tuple after modulo : ((1, 3), (1, 5), (0, 0), (1, 1))
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

