Python program to check if given value occurs atleast k times



Given a list and some value (let’s say it N), write a Python program to check
if the given value occurs atleast k-times in that list.

We can use list comprehension to deal with this problem. We can add each
occurrence of given value and check if it is greater than or equal to k. If
the value returned is True, then set the flag to 1, else 0.

Below is the Python implementation –

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to check if given

# value occurs atleast k times

 

test_list = [1, 3, 5, 5, 4, 5] 

 

# printing original list 

print ("The original list is : " + str(test_list)) 

 

# value to be checked 

val = 5

 

# initializing k 

k = 3

 

# using sum() + list comprehension 

# checking occurrences

res = 0

res = sum([1 for i in test_list if i == val]) >=
k

 

if res == 1 : res = True

else : res = False

 

# printing result 

print ("%d occur atleast %d times ? :" %(val, k) + str(res))   
  
---  
  
__

__

**Output:**

    
    
    The original list is : [1, 3, 5, 5, 4, 5]
    5 occur atleast 3 times ? :True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

