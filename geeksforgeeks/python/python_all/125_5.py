Python | Check element for range occurrence



Sometimes, while working with data, we can have a simple problem in which we
have ranges in form of tuple, and we need to check if a specific number lies
between any of ranges suggested by tuple. This has it’s application in
competitive programming. Let’s discuss certain ways in which this task can be
performed.

 **Method #1 : Using loop +enumerate()**  
This task can be performed using combination of above functions. In this, we
just need to iterate through each element of list and return the index of
tuple pair between which the element exists using enumerate().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check element for range occurrence

# Using loop + enumerate()

 

# Initializing list

test_list = [(45, 90), (100, 147), (150, 200)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing element

N = 124

 

# Check element for range occurrence

# Using loop + enumerate()

res = None

for idx in (idx for idx, (sec, fir) in enumerate(test_list)
if sec <= N <= fir):

 res = idx

 

# printing result

print("The index of tuple between which element occurs : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(45, 90), (100, 147), (150, 200)]
    The index of tuple between which element occurs : 1
    

**Method #2 : Usingnext() + enumerate() \+ generator expression**  
This task can also be performed using combination of above functions. In this,
we just iterate through using next(). Rest everything is performed similar
to the above function.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check element for range occurrence

# Using next() + enumerate() + generator expression

 

# Initializing list

test_list = [(45, 90), (100, 147), (150, 200)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing element

N = 124

 

# Check element for range occurrence

# Using next() + enumerate() + generator expression

res = next((idx for idx, (sec, fir) in enumerate(test_list)
if sec <= N <= fir), None)

 

# printing result

print("The index of tuple between which element occurs : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(45, 90), (100, 147), (150, 200)]
    The index of tuple between which element occurs : 1
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

