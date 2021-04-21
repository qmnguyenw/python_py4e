Python – Nth smallest Greater than K



This article offers various approaches to solve the problem of finding Nth
smallest number in python list greater than a specific element K in python
list. This basically provides all the approaches from naive to one-liners so
that they can be used in programming whenever required.

 **Method 1 : Naive Method +sort()**  
Using loop we keep on adding elements that are greater than K and then sort
the list and find the Nth element greater than K.

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# Nth smallest Greater than K

# using naive method + sort()

 

# Initializing list 

test_list = [1, 4, 7, 5, 10]

 

# Initializing k

k = 6

 

# Initializing N 

N = 2

 

# Printing original list 

print ("The original list is : " + str(test_list))

 

# Using naive method + sort()

# Nth smallest Greater than K

res = []

for i in test_list :

 if i > k :

 res.append(i)

res.sort()

 

# Printing result 

print ("The Nth minimum value greater than 6 is : " + str(res[N
- 1]))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 4, 7, 5, 10]
    The Kth minimum value greater than 6 is : 10
    

**Method 2 : lambda + filter() + sort()**  
Similar approach to method above, just to filter the numbers in list greater
than k, filter() instead of loop is used in this approach. Works in a similar
way as above after that.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# Nth smallest Greater than K

# using min() + sort() + lambda

 

# Initializing list 

test_list = [1, 4, 7, 5, 10]

 

# Initializing k

k = 6

 

# Initializing N 

N = 2

 

# Printing original list 

print ("The original list is : " + str(test_list))

 

# Nth smallest Greater than K

# using min() + sort() + lambda

res = list(filter(lambda i: i > k, test_list))

res.sort()

 

# Printing result 

print ("The Nth minimum value greater than 6 is : " + str(res[N
- 1]))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 4, 7, 5, 10]
    The Kth minimum value greater than 6 is : 10
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

