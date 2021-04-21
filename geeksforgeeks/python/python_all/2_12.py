Python – Create nested list containing values as the count of list items



Given a list, the task is to write a Python program to create a nested list
where the values are the count of list items.

 **Examples:**

    
    
     **Input:** [1, 2, 3]
    **Output:** [[1], [2, 2], [3, 3, 3]]
    
    **Input:** [4, 5]
    **Output:** [[1, 1, 1, 1], [2, 2, 2, 2, 2]]

 **Method 1: Using nested** **list comprehension**

The list will contain the count of the list items for each element e in the
list we will create a list in the list with size e, in each list we will
append the element e for e times.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

l= [1, 2, 3, 4, 5]

l = [[i+1 for j in range(l[i])] for i in
range(len(l))]

print(l)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    [[1], [2, 2], [3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5, 5]]

 **Method 2:**

The list will contain the count of the list items iterate the for loop for L
times i.e. length of the list. Now at each element append a list, The appended
list will be of the size count.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

l= [1, 2, 3, 4, 5]

 

for i in range(len(l)):

 l[i] = [i+1 for j in range(i+1)]

 

print(l)  
  
---  
  
 __

 __

 **Output:**

    
    
    [[1], [2, 2], [3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5, 5]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

