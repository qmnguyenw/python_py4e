Python – How to Multiply all items in Tuple



Sometimes, while programming, we have a problem in which we might need to
perform product among tuple elements. This is an essential utility as we come
across product operation many times and tuples are immutable and hence
required to be dealt with. Let’s discuss certain ways in which this task can
be performed.

 **Method #1 : Usinglist() \+ loop**  
The above functions can be combined to perform this task. We can employ loop
to accumulate the result of product logic. The list() function is used to
perform interconversions.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Tuple Elements Multiplication

# Using list() + loop

 

# getting Product 

def prod(val) : 

 res = 1

 for ele in val: 

 res *= ele 

 return res 

 

# initializing tup 

test_tup = (7, 8, 9, 1, 10, 7) 

 

# printing original tuple 

print("The original tuple is : " + str(test_tup)) 

 

# Tuple Elements Multiplication 

# Using list() + loop

res = prod(list(test_tup)) 

 

# printing result 

print("The product of tuple elements are : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original tuple is : (7, 8, 9, 1, 10, 7)
    The product of tuple elements are : 35280
    

**Method #2 : Usingmap() + loop + list()**  
The combination of above functions can be used to perform this task. In this,
we first convert the tuple to list, flatten it’s each list element using
map(), perform product of each using loop and again employ loop for overall
product of resultant list.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate working of

# Tuple Elements Multiplication

# Using map() + list() + loop

 

# getting Product 

def prod(val) : 

 res = 1

 for ele in val: 

 res *= ele 

 return res 

 

# initializing tup 

test_tup = ([7, 8], [9, 1], [10, 7]) 

 

# printing original tuple 

print("The original tuple is : " + str(test_tup)) 

 

# Tuple Elements Multiplication

# Using map() + list() + loop 

res = prod(list(map(prod, list(test_tup)))) 

 

# printing result 

print("The product of tuple elements are : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original tuple is : (7, 8, 9, 1, 10, 7)
    The product of tuple elements are : 35280
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

