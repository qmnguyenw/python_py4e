Python – Similar Consecutive elements frequency



Sometimes, while working with Python, we can have a problem in which we have
to find the occurrences of elements that are present consecutively. This
problem have usage in school programming and data engineering. Let’s discuss
certain ways in which this task can be performed.

 **Method #1 : Using loop**  
This is brute force method by which this problem can be solved. In this, we
iterate loop and count till we get other number.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Similar Consecutive elements frequency

# using loop

 

# initializing list 

test_list = [2, 2, 3, 3, 3, 3, 4, 4,
4]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# Similar Consecutive elements frequency

# using loop

res = []

count = 1

for ele in range(0, len(test_list) -1):

 if test_list[ele] != test_list[ele + 1]:

 res.append((test_list[ele], count))

 count = 1

 else :

 count = count + 1

res.append((test_list[len(test_list) -1], count))

 

# printing result 

print ("The consecutive element frequency is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [2, 2, 3, 3, 3, 3, 4, 4, 4]
    The consecutive element frequency is : [(2, 2), (3, 4), (4, 3)]
    

**Method #2 : Usinggroupby() + len() \+ list comprehension**  
The combination of above methods can be used to perform this task. In this, we
group the consecutive elements and extract the count using len(). List
comprehension is used to bind both the logics together.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Similar Consecutive elements frequency

# using groupby() + len() + list comprehension

from itertools import groupby

 

# initializing list 

test_list = [2, 2, 3, 3, 3, 3, 4, 4,
4]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# Similar Consecutive elements frequency

# using groupby() + len() + list comprehension

res = [(k, len(list(j))) for k, j in groupby(test_list)]

 

# printing result 

print ("The consecutive element frequency is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [2, 2, 3, 3, 3, 3, 4, 4, 4]
    The consecutive element frequency is : [(2, 2), (3, 4), (4, 3)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

