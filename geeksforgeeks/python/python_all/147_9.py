Python | Assign ids to each unique value in a list



Sometimes, while working in web development domain or in competitive
programming, we require to assign a unique id to each of the different value
to track for it’s occurrence for count or any other required use case. Let’s
discuss certain ways in which this task can be performed.

 **Method #1 : Usingdefaultdict \+ lambda + list comprehension**

The combination of above functions can be used to accomplish this particular
task. The defaultdict function performs the main task of assigning Ids using
lambda function, it assigns the current number of keys to every new key. The
list comprehension is used in later stage to form the list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# assigning ids to values

# using list comprehension + defaultdict + lambda

from collections import defaultdict

 

# initializing list

test_list = [5, 6, 7, 6, 5, 1]

 

# printing original list

print("The original list : " + str(test_list))

 

# using list comprehension + defaultdict + lambda

# assigning ids to values

temp = defaultdict(lambda: len(temp))

res = [temp[ele] for ele in test_list]

 

# print result

print("The ids of assigned values is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [5, 6, 7, 6, 5, 1]
    The ids of assigned values is : [0, 1, 2, 1, 0, 3]
    

  

  

**Method #2 : UsingOrderedDict.fromkeys() + enumerate() \+ list
comprehension**

This method performs the task similar to the above method. In this
orderedDict.fromkeys function performs the function to remove the duplicates
and enumerate function helps us get the indices of values to map them
together.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# assigning ids to values using 

# list comprehension + OrderedDict.fromkeys() + enumerate()

from collections import OrderedDict

 

# initializing list

test_list = [5, 6, 7, 6, 5, 1]

 

# printing original list

print("The original list : " + str(test_list))

 

# using list comprehension + OrderedDict.fromkeys() + enumerate()

# assigning ids to values

res = [{val : key for key, val in enumerate(

 OrderedDict.fromkeys(test_list))}

 [ele] for ele in test_list]

 

# print result

print("The ids of assigned values is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [5, 6, 7, 6, 5, 1]
    The ids of assigned values is : [0, 1, 2, 1, 0, 3]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

