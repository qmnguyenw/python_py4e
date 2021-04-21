Python – Group similar elements into Matrix



Sometimes, while working with Python Matrix, we can have a problem in which we
need to perform grouping of all the elements with are same. This kind of
problem can have application in data domains. Let’s discuss certain ways in
which this task can be performed.

>  **Input** : test_list = [1, 3, 4, 4, 2, 3]  
>  **Output** : [[1], [2], [3, 3], [4, 4]]
>
>  **Input** : test_list = [1, 3, 4, 2]  
>  **Output** : [[1], [2], [3], [4]]

 **Method #1 : Using list comprehension +groupby()**  
The combination of above functions provide possible solution to this problem.
In this, we perform task of grouping using groupby() and list comprehension
assists in iteration.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Group similar elements into Matrix

# Using list comprehension + groupby()

from itertools import groupby

 

# initializing list

test_list = [1, 3, 5, 1, 3, 2, 5, 4,
2]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Group similar elements into Matrix

# Using list comprehension + groupby()

res = [list(val) for key, val in
groupby(sorted(test_list))] 

 

# printing result 

print("Matrix after grouping : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original list : [1, 3, 5, 1, 3, 2, 5, 4, 2]
    Matrix after grouping : [[1, 1], [2, 2], [3, 3], [4], [5, 5]]
    

