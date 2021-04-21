Python | Harmonic Mean of List



While working with Python, we can have a problem in which we need to find
harmonic mean of a list cumulative. This problem is common in Data Science
domain. Let’s discuss certain ways in which this problem can be solved.

 **Method #1 : Using loop + formula**  
The simpler manner to approach this problem is to employ the formula for
finding harmonic mean and perform using loop shorthands. This is the most
basic approach to solve this problem.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Harmonic Mean of List

# using loop + formula

 

# initialize list

test_list = [6, 7, 3, 9, 10, 15]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Harmonic Mean of List

# using loop + formula

sum = 0

for ele in test_list:

 sum += 1 / ele 

res = len(test_list)/sum

 

# printing result

print("The harmonic mean of list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [6, 7, 3, 9, 10, 15]
    The harmonic mean of list is : 6.517241379310345
    

**Method #2 : Usingstatistics.harmonic_mean()**  
This task can also be performed using inbuilt function of harmonic_mean().
This is new in Python versions >= 3.8.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Harmonic Mean of List

# using statistics.harmonic_mean()

import statistics 

 

# initialize list

test_list = [6, 7, 3, 9, 10, 15]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Harmonic Mean of List

# using statistics.harmonic_mean()

res = statistics.harmonic_mean(test_list)

 

# printing result

print("The harmomin mean of list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [6, 7, 3, 9, 10, 15]
    The harmonic mean of list is : 6.517241379310345
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

