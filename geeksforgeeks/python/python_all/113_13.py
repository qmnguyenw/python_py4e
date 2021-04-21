Python – Remove front column from Matrix



Sometimes, while working with Matrix data, we can have stray element that
attached at front end of each row of matrix. This can be undesired at times
and wished to be removed. Let’s discuss certain ways in which this task can be
performed.

 **Method #1 : Using loop + del + list slicing**  
The combination of above functionalities can be used to perform this task. In
this, we run a loop for each row in matrix and remove the front element using
del.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove front column from Matrix

# Using loop + del + list slicing

 

# initialize list

test_list = [[1, 3, 4], [2, 4, 6], [3, 8,
1]]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Remove front column from Matrix

# Using loop + del + list slicing

for ele in test_list: del ele[0] 

 

# printing result

print("Matrix after removal of front column : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [[1, 3, 4], [2, 4, 6], [3, 8, 1]]
    Matrix after removal of front column : [[3, 4], [4, 6], [8, 1]]
    

**Method #2 : Using list comprehension + list slicing**  
The combination of above functions can also be used to perform this task. In
this, we just iterate for each row and delete front element using list
slicing.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove front column from Matrix

# Using list comprehension + list slicing

 

# initialize list

test_list = [[1, 3, 4], [2, 4, 6], [3, 8,
1]]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Remove front column from Matrix

# Using list comprehension + list slicing

res = [ele[1:] for ele in test_list]

 

# printing result

print("Matrix after removal of front column : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [[1, 3, 4], [2, 4, 6], [3, 8, 1]]
    Matrix after removal of front column : [[3, 4], [4, 6], [8, 1]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

