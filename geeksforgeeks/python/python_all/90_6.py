Python | Maximum distance between elements



Sometimes, while working with lists, we can have a problem in which we need to
find maximum distance between reoccurring elements. This kind of problem can
have application in competitive programming and web development domain. Let’s
discuss certain way in which this task can be performed.

 **Method : Using loop + max() + defaultdict() + enumerate()**  
The combination of above functions can be used to perform this particular
task. In this, we first initialize the temp dict with list using
defaultdict(). The iteration is using enumerate() and max() performs the
maximum distance between all similar numbers in list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Maximum distance between elements

# using max() + enumerate() + loop + defaultdict()

from collections import defaultdict

 

# Initializing list

test_list = [4, 5, 6, 4, 6, 3]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Maximum distance between elements

# using max() + enumerate() + loop + defaultdict()

temp = defaultdict(list)

for idx, ele in enumerate(test_list):

 temp[ele].append(idx)

res = max(temp[ele][-1]-temp[ele][0] for ele in
temp)

 

# printing result 

print ("Maximum distance between same element is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [4, 5, 6, 4, 6, 3]
    Maximum distance between same element is : 3
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

