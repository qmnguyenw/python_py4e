Python – Custom Columns Matrix



Sometimes, while working with Python lists, we can have a problem in which we
need to extract certain columns from Matrix and recreate it. This kind of
problem can have applications in data domains as they use Matrix as a
prominent input parameter. Let’s discuss certain ways in which this task can
be performed.

>  **Input** : test_list = [[5, 4, 3, 4], [7, 6, 3, 2], [8, 3, 9, 10]],
> col_list = [2]  
>  **Output** : [[3], [3], [9]]
>
>  **Input** : test_list = [[5, 4], [6, 2], [8, 3]], col_list = [1]  
>  **Output** : [[4], [2], [3]]

 **Method #1 : Using list comprehension**  
This offers one of the ways to solve this problem. In this, we perform
extraction of selective columns using nested list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Custom Columns Matrix

# Using list comprehension

 

# initializing list

test_list = [[5, 4, 3, 4],

 [7, 6, 3, 2], 

 [8, 3, 9, 10]]

 

# printing original list 

print("The original list : " + str(test_list))

 

# initializing Columns list 

col_list = [1, 3]

 

# Custom Columns Matrix

# Using list comprehension

res = [[sub[idx] for idx in col_list] for sub in
test_list]

 

# printing result 

print("Matrix after filtering : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original list : [[5, 4, 3, 4], [7, 6, 3, 2], [8, 3, 9, 10]]
    Matrix after filtering : [[4, 4], [6, 2], [3, 10]]
    

