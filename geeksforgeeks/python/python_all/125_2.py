Python | Mean of tuple list



Sometimes, while working with Python tuple list, we can have a problem in
which we need to find the average of tuple values in the list. This problem
has the possible application in many domains including mathematics. Let’s
discuss certain ways in which this task can be performed.

 **Method #1 : Using loops**  
The first approach that can be thought of to solve this problem can be a brute
force approach in which we just loop each tuple to add element and then just
divide it by number of tuples in the list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Mean of tuple list

# Using loops

 

# Initializing list

test_list = [(1, 4, 5), (7, 8), (2, 4,
10)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Average of tuple list

# Using loops

sum = 0

for sub in test_list:

 for i in sub:

 sum = sum + i

res = sum / len(test_list)

 

# printing result

print("The mean of tuple list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(1, 4, 5), (7, 8), (2, 4, 10)]
    The mean of tuple list is : 13.666666666666666
    

**Method #2 : Usingchain() + sum()**  
In order to reduce the line of codes, the chain() functionality can be used
so that all the elements can be extracted and then can be added using sum().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Mean of tuple list

# Using chain() + sum()

from itertools import chain

 

# Initializing list

test_list = [(1, 4, 5), (7, 8), (2, 4,
10)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Average of tuple list

# Using chain() + sum()

temp = list(chain(*test_list)) 

res = sum(temp)/ len(test_list)

 

# printing result

print("The mean of tuple list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(1, 4, 5), (7, 8), (2, 4, 10)]
    The mean of tuple list is : 13.666666666666666
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

