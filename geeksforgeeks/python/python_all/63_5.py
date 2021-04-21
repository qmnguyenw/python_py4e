Python – Flatten tuple of List to tuple



Sometimes, while working with Python Tuples, we can have a problem in which we
need to perform the flattening of tuples, which have lists as its constituent
elements. This kind of problem is common in data domains such as Machine
Learning. Let’s discuss certain ways in which this task can be performed.

>  **Input** : test_tuple = ([5], [6], [3], [8])  
>  **Output** : (5, 6, 3, 8)
>
>  **Input** : test_tuple = ([5, 7, 8])  
>  **Output** : (5, 7, 8)

 **Method #1 : Usingsum() + tuple()**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of flattening using sum(), passing empty list as its
argument.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Flatten tuple of List to tuple

# Using sum() + tuple()

 

# initializing tuple

test_tuple = ([5, 6], [6, 7, 8, 9], [3])

 

# printing original tuple

print("The original tuple : " + str(test_tuple))

 

# Flatten tuple of List to tuple

# Using sum() + tuple()

res = tuple(sum(test_tuple, []))

 

# printing result 

print("The flattened tuple : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original tuple : ([5, 6], [6, 7, 8, 9], [3])
    The flattened tuple : (5, 6, 6, 7, 8, 9, 3)
    

