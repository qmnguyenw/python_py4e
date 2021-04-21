Python | How to Concatenate tuples to nested tuples



Sometimes, while working with tuples, we can have a problem in which we need
to convert individual records into a nested collection yet remaining as
separate element. Usual addition of tuples, generally adds the contents and
hence flattens the resultant container, this is usually undesired. Let’s
discuss certain ways in which this problem is solved.

 **Method #1 : Using+ operator \+ ", " operator during initialization**  
In this method, we perform the usual addition of tuple elements, but while
initializing tuples, we add a comma after the tuple so that they don’t get
flattened while addition.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Concatenating tuples to nested tuples

# using + operator + ", " operator during initialization

 

# initialize tuples

test_tup1 = (3, 4),

test_tup2 = (5, 6),

 

# printing original tuples

print("The original tuple 1 : " + str(test_tup1))

print("The original tuple 2 : " + str(test_tup2))

 

# Concatenating tuples to nested tuples

# using + operator + ", " operator during initialization

res = test_tup1 + test_tup2

 

# printing result

print("Tuples after Concatenating : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple 1 : ((3, 4), )
    The original tuple 2 : ((5, 6), )
    Tuples after Concatenating : ((3, 4), (5, 6))
    

**Method #2 : Using “, ” operator during concatenation**  
This task can be performed by applying “, ” operator during concatenation as
well. It can perform the safe concatenation.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Concatenating tuples to nested tuples

# Using ", " operator during concatenation

 

# initialize tuples

test_tup1 = (3, 4)

test_tup2 = (5, 6)

 

# printing original tuples

print("The original tuple 1 : " + str(test_tup1))

print("The original tuple 2 : " + str(test_tup2))

 

# Concatenating tuples to nested tuples

# Using ", " operator during concatenation

res = ((test_tup1, ) + (test_tup2, ))

 

# printing result

print("Tuples after Concatenating : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple 1 : ((3, 4), )
    The original tuple 2 : ((5, 6), )
    Tuples after Concatenating : ((3, 4), (5, 6))
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

