Python – Remove first occurrence of K in Tuple



Sometimes, while working with Python tuples, we can have a problem in which we
need to perform the removal of first occurrence of an element in tuple. This
type of problem can have application in many domains such as school
programming. Let’s discuss certain ways in which this task can be performed.

>  **Input** : test_tuple = (5, 6, 5, 4, 7, 8, 4), K = 5  
>  **Output** : (6, 5, 4, 7, 8, 4)
>
>  **Input** : test_tuple = (5, 6, 8, 4, 7, 8, 4), K = 8  
>  **Output** : (5, 6, 4, 7, 8, 4)

 **Method #1 : Usingindex() + loop + list slicing**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of extracting the first occurrence of K using index() and
list slicing is used to reorder the tuple after element removal.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove first occurrence of K in Tuple

# Using index() + loop + list slicing

 

# initializing tuples

test_tuple = (5, 6, 4, 4, 7, 8, 4)

 

# printing original tuple

print("The original tuple : " + str(test_tuple))

 

# initializing K 

K = 4

 

# Remove first occurrence of K in Tuple

# Using index() + loop + list slicing

try:

 idx = test_tuple.index(K)

 res = test_tuple[:idx] + test_tuple[idx + 1:]

except ValueError: 

 res = test_tuple

 

# printing result 

print("Tuple after element removal : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original tuple : (5, 6, 4, 4, 7, 8, 4)
    Tuple after element removal : (5, 6, 4, 7, 8, 4)
    

