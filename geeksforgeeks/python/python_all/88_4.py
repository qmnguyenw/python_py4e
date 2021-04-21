Python – Double each consecutive duplicate



Sometimes, while working with data, we can have a problem in which we need to
perform double of element on each consecutive occurrence of a duplicate. This
is very specific problem, but solution to this can prove to be very handy.
Lets discuss certain ways in which this task can be performed.

 **Method #1 : Using loop**  
This is brute force way to perform this task. In this, we iterate each element
and when we find duplicate we store in dictionary and perform its double
subsequently.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Double each consecutive duplicate

# using loop

 

# Initializing list

test_list = [1, 2, 4, 2, 4, 1, 2]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Double each consecutive duplicate

# using loop

temp = {}

res = []

for ele in test_list:

 temp[ele] = temp1 = temp.get(ele, 0) + ele

 res.append(temp1)

 

# printing result 

print ("The list after manipulation is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 2, 4, 2, 4, 1, 2]
    The list after manipulation is : [1, 2, 4, 4, 8, 2, 6]
    

**Method #2 : Usingdefaultdict() \+ loop**  
This method performs this task in similar way as above. The only difference is
a step is reduced by using defaultdict() as it pre initializes the list.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Double each consecutive duplicate

# using loop + defaultdict()

from collections import defaultdict

 

# Initializing list

test_list = [1, 2, 4, 2, 4, 1, 2]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Double each consecutive duplicate

# using loop + defaultdict()

temp = defaultdict(int)

res = []

for ele in test_list:

 temp[ele] += ele

 res.append(temp[ele])

 

# printing result 

print ("The list after manipulation is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 2, 4, 2, 4, 1, 2]
    The list after manipulation is : [1, 2, 4, 4, 8, 2, 6]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

