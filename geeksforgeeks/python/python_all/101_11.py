Python – Union of Tuples



Sometimes, while working with tuples, we can have a problem in which we need
union of two records. This type of application can come in Data Science
domain. Let’s discuss certain ways in which this problem can be solved.

 **Method #1 : Using set() + “+” operator**  
This task can be performed using union functionality offered by + operator
over sets. The conversion to set is done by set().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Union of Tuples

# Using set() + "+" operator

 

# initialize tuples

test_tup1 = (3, 4, 5, 6)

test_tup2 = (5, 7, 4, 10)

 

# printing original tuples

print("The original tuple 1 : " + str(test_tup1))

print("The original tuple 2 : " + str(test_tup2))

 

# Union of Tuples

# Using set() + "+" operator

res = tuple(set(test_tup1 + test_tup2))

 

# printing result

print("The union elements from tuples are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple 1 : (3, 4, 5, 6)
    The original tuple 2 : (5, 7, 4, 10)
    The union elements from tuples are : (3, 4, 5, 6, 7, 10)
    
    

  
**Method #2 : Using union() + set()**  
This is method similar to above method, the difference is that instead of +
operator, we use inbuilt function to perform the task of filtering dissimilar
elements.  

__

__  
__

__

__  
__  
__

# Python3 code to demonstrate working of

# Union of Tuples

# Using union() + set()

 

# initialize tuples

test_tup1 = (3, 4, 5, 6)

test_tup2 = (5, 7, 4, 10)

 

# printing original tuples

print("The original tuple 1 : " + str(test_tup1))

print("The original tuple 2 : " + str(test_tup2))

 

# Union of Tuples

# Using union() + set()

res = tuple(set(test_tup1).union(set(test_tup2)))

 

# printing result

print("The union elements from tuples are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple 1 : (3, 4, 5, 6)
    The original tuple 2 : (5, 7, 4, 10)
    The union elements from tuples are : (3, 4, 5, 6, 7, 10)
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

