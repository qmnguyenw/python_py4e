Python | Frequency grouping of list elements



Sometimes, while working with lists, we can have a problem in which we need to
group element along with it’s frequency in form of list of tuple. Let’s
discuss certain ways in which this task can be performed.

 **Method #1 : Using loop**  
This is a brute force method to perform this particular task. In this, we
iterate each element, check in other list for it’s presence, if yes, then
increase it’s count and put to tuple.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Frequency grouping of list elements

# using loop

 

# initialize list 

test_list = [1, 3, 3, 1, 4, 4]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Frequency grouping of list elements

# using loop

res = []

temp = dict()

for ele in test_list:

 if ele in temp:

 temp[ele] = temp[ele] + 1

 else : 

 temp[ele] = 1

for key in temp:

 res.append((key, temp[key]))

 

# printing result

print("Frequency of list elements : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [1, 3, 3, 1, 4, 4]
    Frequency of list elements : [(1, 2), (3, 2), (4, 2)]
    

**Method #2 : UsingCounter() + items()**  
The combination of two functions can be used to perform this task. They
perform this task using inbuild constructs and are a shorthand to perform this
task.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Frequency grouping of list elements

# using Counter() + items()

from collections import Counter

 

# initialize list 

test_list = [1, 3, 3, 1, 4, 4]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Frequency grouping of list elements

# using Counter() + items()

res = list(Counter(test_list).items())

 

# printing result

print("Frequency of list elements : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [1, 3, 3, 1, 4, 4]
    Frequency of list elements : [(1, 2), (3, 2), (4, 2)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

