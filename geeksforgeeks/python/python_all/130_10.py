Python | Indices list of matching element from other list



Sometimes, while working with Python list, we have a problem in which we have
to search for a element in list. But this can be extended to a list and need
to find the exact places where elements occur in other list. Let’s discuss
certain ways in which this task can be performed.

 **Method #1 : Using loop +count()**  
This is the brute method to perform this task. In this we can just count the
occurrence of an element in other list and if we find it, then we add it’s
index to the result list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Indices list of matching element from other list

# Using loop + count()

 

# initializing lists

test_list1 = [5, 7, 8, 9, 10, 11]

test_list2 = [8, 10, 11]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Indices list of matching element from other list

# Using loop + count()

res = []

i = 0

while (i < len(test_list1)):

 if (test_list2.count(test_list1[i]) > 0):

 res.append(i)

 i += 1

 

# printing result 

print("The matching element Indices list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : [5, 7, 8, 9, 10, 11]
    The original list 2 is : [8, 10, 11]
    The matching element Indices list : [2, 4, 5]
    

**Method #2 : Using list comprehension +set() + enumerate()**  
The combination of above functions can be used to perform the task. In these
we just convert the list to set and then check for index and value together
for existence using enumerate() and append the index if found.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Indices list of matching element from other list

# Using list comprehension + set() + enumerate()

 

# initializing lists

test_list1 = [5, 7, 8, 9, 10, 11]

test_list2 = [8, 10, 11]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Indices list of matching element from other list

# Using list comprehension + set() + enumerate()

temp = set(test_list2)

res = [i for i, val in enumerate(test_list1) if val in
temp]

 

# printing result 

print("The matching element Indices list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : [5, 7, 8, 9, 10, 11]
    The original list 2 is : [8, 10, 11]
    The matching element Indices list : [2, 4, 5]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

