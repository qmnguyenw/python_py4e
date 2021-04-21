Python – Nested List to single value Tuple



Sometimes, while working with Python data, we can have problems in which we
need to convert Python Nested lists to single values tuples. This kind of
problem can have applications in domains such as web development and
competitive programming. Let’s discuss certain ways in which this task can be
performed.

>  **Input** : test_list = [[5, 6], [4, 7, 10, 17]]  
>  **Output** : [(5, ), (6, ), (4, ), (7, ), (10, ), (17, )]
>
>  **Input** : test_list = [[5, 6, 7, 8]]  
>  **Output** : [(5, ), (6, ), (7, ), (8, )]

 **Method #1 : Using list comprehension ( For single nesting )**  
This is one of the way in which this task can be performed. We iterate each
inner list and convert each element as separate tuple. This caters just for a
single nesting.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Nested List to 1 value Tuple

# Using list comprehension

 

# initializing list

test_list = [[5, 6], [4, 7, 10], [12], [9,
11]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Convert Nested List to 1 value Tuple

# Using list comprehension

res = [(ele, ) for sub in test_list for ele in sub]

 

# printing result 

print("The converted container : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [[5, 6], [4, 7, 10], [12], [9, 11]]
    The converted container : [(5, ), (6, ), (4, ), (7, ), (10, ), (12, ), (9, ), (11, )]
    

