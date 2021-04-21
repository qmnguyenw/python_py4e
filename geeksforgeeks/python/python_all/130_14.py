Python | Duplicate element indices in list



While working with Python list, sometimes, we require to check for duplicates
and may also sometimes require to track their indices. This kind of
application can occur in day-day programming. Let’s discuss certain ways in
which this problem can be solved.

 **Method #1 : Using loop +set()**  
This task can be solved using the combination of above functions. In this, we
just insert all the elements in set and then compare each element’s existence
in actual list. If it’s the second occurrence or more, then index is added in
result list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Duplicate element indices in list

# Using set() + loop

 

# initializing list

test_list = [1, 4, 5, 5, 5, 9, 1]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Duplicate element indices in list

# Using set() + loop

oc_set = set()

res = []

for idx, val in enumerate(test_list):

 if val not in oc_set:

 oc_set.add(val) 

 else:

 res.append(idx) 

 

# printing result

print("The list of duplicate elements is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 4, 5, 5, 5, 9, 1]
    The list of duplicate elements is :  [3, 4, 6]
    

**Method #2 : Using list comprehension + list slicing**  
This method is one liner alternative to perform this task. In this we just
check for the non repeating element using list slicing and keep adding index
in case it’s repeated.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Duplicate element indices in list

# Using list comprehension + list slicing

 

# initializing list

test_list = [1, 4, 5, 5, 5, 9, 1]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Duplicate element indices in list

# Using list comprehension + list slicing

res = [idx for idx, val in enumerate(test_list) if val
in test_list[:idx]]

 

# printing result

print("The list of duplicate elements is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 4, 5, 5, 5, 9, 1]
    The list of duplicate elements is :  [3, 4, 6]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

