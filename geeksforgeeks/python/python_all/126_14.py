Python | Standard deviation of list



Sometimes, while working with Mathematics, we can have a problem in which we
intend to compute the standard deviation of a sample. This has many
applications in competitive programming as well as school level projects.
Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Usingsum() \+ list comprehension**  
This is a brute force shorthand to perform this particular task. We can
approach this problem in sections, computing mean, variance and standard
deviation as square root of variance. The sum() is key to compute mean and
variance. List comprehension is used to extend the common functionality to
each of element of list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Standard deviation of list

# Using sum() + list comprehension

 

# initializing list

test_list = [4, 5, 8, 9, 10]

 

# printing list

print("The original list : " + str(test_list))

 

# Standard deviation of list

# Using sum() + list comprehension

mean = sum(test_list) / len(test_list)

variance = sum([((x - mean) ** 2) for x in
test_list]) / len(test_list)

res = variance ** 0.5

 

# Printing result

print("Standard deviation of sample is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
     
    The original list : [4, 5, 8, 9, 10]
    Standard deviation of sample is : 2.3151673805580453
    

**Method #2 : Usingpstdev()**  
This task can also be performed using inbuilt functionality of pstdev().
This function computes standard deviation of sample internally.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Standard deviation of list

# Using pstdev()

import statistics

 

# initializing list

test_list = [4, 5, 8, 9, 10]

 

# printing list

print("The original list : " + str(test_list))

 

# Standard deviation of list

# Using pstdev()

res = statistics.pstdev(test_list)

 

# Printing result

print("Standard deviation of sample is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
     
    The original list : [4, 5, 8, 9, 10]
    Standard deviation of sample is : 2.3151673805580453
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

