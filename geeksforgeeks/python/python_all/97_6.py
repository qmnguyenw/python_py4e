Python – Sum of tuple elements



Sometimes, while programming, we have a problem in which we might need to
perform summation among tuple elements. This is an essential utility as we
come across summation operation many times and tuples are immutable and hence
required to be dealt with. Let’s discuss certain ways in which this task can
be performed.

 **Method #1 : Usinglist() + sum()**  
The above functions can be combined to perform this task. We can employ sum()
to accumulate the result of summation logic. The list() function is used to
perform interconversions.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Tuple summation

# Using list() + sum()

 

# initializing tup 

test_tup = (7, 8, 9, 1, 10, 7) 

 

# printing original tuple

print("The original tuple is : " + str(test_tup)) 

 

# Tuple elements inversions

# Using list() + sum()

res = sum(list(test_tup))

 

# printing result 

print("The summation of tuple elements are : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original tuple is : (7, 8, 9, 1, 10, 7)
    The summation of tuple elements are : 42
    

**Method #2 : Usingmap() + sum() + list()**  
The combination of above functions can be used to perform this task. In this,
we first convert the tuple to list, flatten it’s each list element using
map(), perform summation of each using sum() and again employ sum() for
overall summation of resultant list.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate working of

# Tuple elements inversions

# Using map() + list() + sum()

 

# initializing tup 

test_tup = ([7, 8], [9, 1], [10, 7]) 

 

# printing original tuple

print("The original tuple is : " + str(test_tup)) 

 

# Tuple elements inversions

# Using map() + list() + sum()

res = sum(list(map(sum, list(test_tup))))

 

# printing result 

print("The summation of tuple elements are : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original tuple is : (7, 8, 9, 1, 10, 7)
    The summation of tuple elements are : 42
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

