Python – Maximum element in Cropped List



Sometimes, while working with Python, we can have a problem in which we need
to get maximum of list. But sometimes, we need to get this for between custom
indices. This can be need of any domain be it normal programming or web
development. Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Using loop +max()**  
This is brute force method in which we performed this task. In this, we just
add to new list the elements in specified range. Then max() is used to compute
maximum.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Maximum element in Cropped List

# using loop + max()

 

# initializing list 

test_list = [2, 3, 5, 7, 9, 10, 8, 6]

 

# printing original list

print ("The original list is : " + str(test_list))

 

i, j = 2, 5

 

# Maximum element in Cropped List

# using loop + max()

res = []

for idx, ele in enumerate(test_list):

 if idx >= i and idx < j:

 res.append(ele)

res = max(res)

 

# printing result 

print ("The maximum element in range is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [2, 3, 5, 7, 9, 10, 8, 6]
    The maximum element in range is : 9
    

**Method #2 : Using list slicing +max()**  
The combination of above functions can be used to perform this task. In this,
we just perform slicing using list slicing and max() performs the task of
extracting max.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Maximum element in Cropped List

# using list slicing + max()

 

# initializing list 

test_list = [2, 3, 5, 7, 9, 10, 8, 6]

 

# printing original list

print ("The original list is : " + str(test_list))

 

i, j = 2, 5

 

# Maximum element in Cropped List

# using list slicing + max()

res = test_list[i : j]

res = max(res)

 

# printing result 

print ("The maximum element in range is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [2, 3, 5, 7, 9, 10, 8, 6]
    The maximum element in range is : 9
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

