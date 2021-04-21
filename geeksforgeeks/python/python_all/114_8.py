Python – Summation of float string list



Sometimes, while working with Python list, we can have a problem in which we
need to find summation in list. But sometimes, we don’t have a natural number
but a floating-point number in string format. This problem can occur while
working with data, both in web development and Data Science domain. Let’s
discuss the ways in which this problem can be solved.

 **Method #1 : Usingsum() + float() \+ generator**  
This problem can be solved using the sum function in which we first convert
the strings into float and then pass this logic in functions in respective sum
function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Summation of float string list

# using sum() + float() + generator

 

# initialize lists

test_list = ['4.5', '7.8', '9.8', '10.3']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Summation of float string list

# using sum() + float() + generator

res_sum = sum(float(sub) for sub in test_list)

 

# printing result

print("The summation of float string list : " + str(res_sum))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['4.5', '7.8', '9.8', '10.3']
    The summation of float string list : 32.400000000000006
    

**Method #2 : Using loop**  
This is a brute force method to perform this task. In this, we iterate for the
list and convert and sum the list float elements during iteration.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Summation of float string list

# Using loop

 

# initialize lists

test_list = ['4.5', '7.8', '9.8', '10.3']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Summation of float string list

# Using loop

res_sum = 0

for ele in test_list: 

 res_sum += float(ele)

 

# printing result

print("The summation of float string list : " + str(res_sum))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['4.5', '7.8', '9.8', '10.3']
    The summation of float string list : 32.400000000000006
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

