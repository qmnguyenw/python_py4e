Python – Test if List contains elements in Range



A lot of times, while working with data, we have a problem in which we need to
make sure that a container or a list is having elements in just one range.
This has application in Data Domains. Let’s discuss certain ways in which this
task can be performed.

 **Method #1 : Using loop**  
This is brute force method in which this task can be performed. In this, we
just check using if condition if element falls in range, and break if we find
even one occurrence out of range.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Test if List contains elements in Range

# using loop

 

# Initializing loop 

test_list = [4, 5, 6, 7, 3, 9]

 

# printing original list 

print("The original list is : " + str(test_list))

 

# Initialization of range 

i, j = 3, 10

 

# Test if List contains elements in Range

# using loop

res = True

for ele in test_list:

 if ele < i or ele >= j :

 res = False

 break

 

# printing result 

print ("Does list contain all elements in range : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [4, 5, 6, 7, 3, 9]
    Does list contain all elements in range : True
    

**Method #2 : Usingall()**  
This is alternative and shorter way to perform this task. In this we use check
operation as a parameter to all() and returns True when all elements in range.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Test if List contains elements in Range

# using all()

 

# Initializing loop 

test_list = [4, 5, 6, 7, 3, 9]

 

# printing original list 

print("The original list is : " + str(test_list))

 

# Initialization of range 

i, j = 3, 10

 

# Test if List contains elements in Range

# using all()

res = all(ele >= i and ele < j for ele in test_list) 

 

# printing result 

print ("Does list contain all elements in range : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [4, 5, 6, 7, 3, 9]
    Does list contain all elements in range : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

