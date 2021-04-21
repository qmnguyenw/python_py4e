Python – Rear elements Average in List



Sometimes, while working with data, we can have a problem in which we need to
perform the mean of all the rear element that come after K. This can be an
application in Mathematics and Data Science domain. Lets discuss certain ways
in which this task can be performed.

 **Method #1 : Usingsum() \+ list comprehension**  
The combination of above functionalities can be used to perform this task. In
this, we first let the initial K element be as they are and perform sum of
rest of element and divide by number of element left.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Rear elements Average in List

# using list comprehension + sum()

 

# Initializing list

test_list = [5, 6, 4, 7, 8, 1, 10]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing K 

K = 3

 

# Rear elements Average in List

# using list comprehension + sum()

res = test_list[ : K] + [sum(test_list[K:]) /
len(test_list[K: ])]

 

# printing result 

print ("Average List after K elements : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [5, 6, 4, 7, 8, 1, 10]
    Average List after K elements : [5, 6, 4, 6.5]
    

**Method #2 : Usingmean() \+ list comprehension**  
This is yet another way in which this task can be performed. In this, we
perform the task of finding mean using mean(), rest of task is same as above
method.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Rear elements Average in List

# using list comprehension + mean()

from statistics import mean

 

# Initializing list

test_list = [5, 6, 4, 7, 8, 1, 10]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing K 

K = 3

 

# Rear elements Average in List

# using list comprehension + mean()

res = [*test_list[:K], mean(test_list[K:])]

 

# printing result 

print ("Average List after K elements : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [5, 6, 4, 7, 8, 1, 10]
    Average List after K elements : [5, 6, 4, 6.5]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

