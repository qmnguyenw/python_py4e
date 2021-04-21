Python – Find the index of Minimum element in list



Sometimes, while working with Python lists, we can have a problem in which we
intend to find the position of minimum element of list. This task is easy and
discussed many times. But sometimes, we can have multiple minimum elements and
hence multiple minimum positions. Let’s discuss ways to achieve this task.

 **Method #1 : Usingmin() + enumerate() \+ list comprehension**  
In this method, the combination of above functions is used to perform this
particular task. This is performed in two steps. In 1st, we acquire the
minimum element and then access the list using list comprehension and
corresponding element using enumerate and extract every element position equal
to minimum element processed in step 1.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Minimum element indices in list

# Using list comprehension + min() + enumerate()

 

# initializing list

test_list = [2, 5, 6, 2, 3, 2]

 

# printing list

print("The original list : " + str(test_list))

 

# Minimum element indices in list

# Using list comprehension + min() + enumerate()

temp = min(test_list)

res = [i for i, j in enumerate(test_list) if j ==
temp]

 

# Printing result

print("The Positions of minimum element : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [2, 5, 6, 2, 3, 2]
    The Positions of minimum element : [0, 3, 5]
    

**Method #2 : Using loop + min()**  
This is brute method to perform this task. In this, we compute the minimum
element and then iterate the list to equate to min element and store indices.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Minimum element indices in list

# Using loop + min()

 

# initializing list

test_list = [2, 5, 6, 2, 3, 2]

 

# printing list

print("The original list : " + str(test_list))

 

# Minimum element indices in list

# Using loop + min()

temp = min(test_list)

res = []

for idx in range(0, len(test_list)):

 if temp == test_list[idx]:

 res.append(idx)

 

# Printing result

print("The Positions of minimum element : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [2, 5, 6, 2, 3, 2]
    The Positions of minimum element : [0, 3, 5]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

