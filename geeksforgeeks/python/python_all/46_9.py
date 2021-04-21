Find sum and average of List in Python



Given a List. The task is to find the sum and average of the list. Average of
the list is defined as the sum of the elements divided by the number of the
elements.

 **Examples:**

    
    
     **Input:** [4, 5, 1, 2, 9, 7, 10, 8]
    **Output:**
    sum =  46
    average =  5.75
    
    **Input:** [15, 9, 55, 41, 35, 20, 62, 49]
    **Output:**
    sum =  286
    average =  35.75
    

**Method 1: Naive method**

In this method, we will iterate over the list of and will add each element to
a variable count which stores the sum of the ith element and then dividing the
sum with the total number of variables to find the average.

 **Example:**

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to find the sum

# and average of the list

 

L = [4, 5, 1, 2, 9, 7, 10, 8]

 

 

# variable to store the sum of 

# the list

count = 0

 

# Finding the sum

for i in L:

 count += i

 

# divide the total elements by

# number of elements

avg = count/len(L)

 

print("sum = ", count)

print("average = ", avg)  
  
---  
  
 __

 __

 **Output:**

    
    
    sum =  46
    average =  5.75
    

**Method 2: Using sum() method**

sum() method returns the sum of the list passed as its argument. Then we will
divide the sum by the len() method to find the average.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to find the sum

# and average of the list

 

L = [4, 5, 1, 2, 9, 7, 10, 8]

 

 

# using sum() method

count = sum(L)

 

# finding average

avg = count/len(L)

 

print("sum = ", count)

print("average = ", avg)  
  
---  
  
 __

 __

 **Output:**

    
    
    sum =  46
    average =  5.75
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

