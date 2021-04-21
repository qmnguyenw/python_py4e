Python – Check if list contain particular digits



Given a List and some digits, the task is to write a python program to check
if the list contains only certain digits.

    
    
     **Input :** test_list = [435, 133, 113, 451, 134], digs = [1, 4, 5, 3]
    **Output :** True
    **Explanation :** All elements are made out of 1, 4, 5 or 3 only.
    
    **Input :** test_list = [435, 133, 113, 451, 134], digs = [1, 4, 5]
    **Output :** False
    **Explanation :** 3 as a digit is required in allowed digits.

 **Method #1 : Using** **loop** **+** **str()** **+** **join()**

In this, we iterate for each element in the list and check for each element to
have all the digits by joining all digits, converting to string and checking
for each in all digit of elements converted to a string.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if list contain particular digits

# Using loop + str() + join()

 

# initializing lists

test_list = [435, 133, 113, 451, 134]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing digits

digs = [1, 4, 5, 3]

 

digt_str = ''.join([str(ele) for ele in digs])

all_ele = ''.join([str(ele) for ele in test_list])

 

res = True

for ele in all_ele:

 

 # checking for all digits in element string

 for el in ele:

 if el not in digt_str:

 res = False

 break

 

# printing result

print("Are all elements made from required digits? : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [435, 133, 113, 451, 134]
    Are all elements made from required digits? : True

 **Method #2 : Using** **any()** **+** **list comprehension**

  

  

In this, we flag off if any digit not from digit string using any() and not
operation. One liner alternative extended using iteration in a list
comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if list contain particular digits

# Using any() + list comprehension

 

# initializing lists

test_list = [435, 133, 113, 451, 134]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing digits

digs = [1, 4, 5, 3]

 

digt_str = ''.join([str(ele) for ele in digs])

all_ele = ''.join([str(ele) for ele in test_list])

 

# any() checks if any element is not part of digit

res = not any(ele not in digt_str for ele in all_ele)

 

# printing result

print("Are all elements made from required digits? : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [435, 133, 113, 451, 134]
    Are all elements made from required digits? : True

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

