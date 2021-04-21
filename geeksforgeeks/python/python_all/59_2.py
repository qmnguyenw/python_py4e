Python – Remove space between tuple elements



Sometimes, while working with Tuples, we can have a problem in which we need
to print tuples, with no space betweem the comma and next element, which by
convention, is present. This problem can have use in day-day and school
programming. Let’s discuss certain ways in which this task can be performed.

>  **Input** : test_tuple = (7, 6, 8)  
>  **Output** : (7, 6, 8)
>
>  **Input** : test_tuple = (6, 8)  
>  **Output** : (6, 8)

 **Method #1 : Usingstr() + replace()**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of removing the additional space, by replacing with empty
space.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove space between tuple elements

# Using replace() + str()

 

# initializing tuples

test_tuple = (4, 5, 7, 6, 8)

 

# printing original tuple

print("The original tuple : " + str(test_tuple))

 

# Remove space between tuple elements

# Using replace() + str()

res = str(test_tuple).replace(' ', '')

 

# printing result 

print("The tuple after space removal : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original tuple : (4, 5, 7, 6, 8)
    The tuple after space removal : (4, 5, 7, 6, 8)
    

