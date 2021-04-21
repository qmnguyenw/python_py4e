Python – Rear column in Multi-sized Matrix



Given a Matrix with variable lengths rows, extract last column.

>  **Input** : test_list = [[3, 4, 5], [7], [8, 4, 6], [10, 3]]  
>  **Output** : [5, 7, 6, 3]  
>  **Explanation** : Last elements of rows filtered.
>
>  **Input** : test_list = [[3, 4, 5], [7], [8, 4, 6]]  
>  **Output** : [5, 7, 6]  
>  **Explanation** : Last elements of rows filtered.

 **Method #1 : Using loop**

This is brute way to solve this, we access last element using “-1”, iterate
for each row.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Rear column in Multisized Matrix

# Using loop

 

# initializing list

test_list = [[3, 4, 5], [7], [8, 4, 6,
1], [10, 3]]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = []

for sub in test_list:

 

 # getting rear element using "-1"

 res.append(sub[-1])

 

# printing results

print("Filtered column : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [[3, 4, 5], [7], [8, 4, 6, 1], [10, 3]]
    Filtered column : [5, 7, 1, 3]
    

**Method #2 : Using list comprehension**

This is another way to solve this, in this, we perform above task in similar
way, just as a shorthand.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Rear column in Multisized Matrix

# Using list comprehension

 

# initializing list

test_list = [[3, 4, 5], [7], [8, 4, 6,
1], [10, 3]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# one-liner to solve this problem

res = [sub[-1] for sub in test_list]

 

# printing results

print("Filtered column : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [[3, 4, 5], [7], [8, 4, 6, 1], [10, 3]]
    Filtered column : [5, 7, 1, 3]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

