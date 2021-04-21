Python | Check if any element in list satisfies a condition



Sometimes, while working with Python lists, we can have a problem to filter a
list. One of the criteria of performing this filter operation can be checking
if any element exists in list that satisfies a condition. Let’s discuss
certain ways in which this problem can be solved.

 **Method #1 : Using list comprehension**  
This problem can be easily solved using loops. But this method provides a one
liner to solve this problem. List comprehension just checks for any element
that satisfies a condition.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if any element in list satisfies a condition

# Using list comprehension

 

# initializing list

test_list = [4, 5, 8, 9, 10, 17]

 

# printing list

print("The original list : " + str(test_list))

 

# Check if any element in list satisfies a condition

# Using list comprehension

res = True in (ele > 10 for ele in test_list)

 

# Printing result

print("Does any element satisfy specified condition ? : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
     
    The original list : [4, 5, 8, 9, 10, 17]
    Does any element satisfy specified condition ? : True
    

**Method #2 : Usingany()**  
This the most generic method to solve this particular problem. In this we just
use the inbuilt function extended by Python library to solve this task. It
checks for any element satisfying a condition and returns a True in case it
finds any one element.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if any element in list satisfies a condition

# Using any()

 

# initializing list

test_list = [4, 5, 8, 9, 10, 17]

 

# printing list

print("The original list : " + str(test_list))

 

# Check if any element in list satisfies a condition

# Using any()

res = any(ele > 10 for ele in test_list)

 

# Printing result

print("Does any element satisfy specified condition ? : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
     
    The original list : [4, 5, 8, 9, 10, 17]
    Does any element satisfy specified condition ? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

