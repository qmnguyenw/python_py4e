Python – Convert List to Single valued Lists in Tuple



Conversion of data types is the most common problem across CS domain nowdays.
One such problem can be converting List elements to single values lists in
tuples. This can have application in data preprocessing domain. Let’s discuss
certain ways in which this task can be performed.

>  **Input** : test_list = [1, 3, 5, 6, 7, 9]  
>  **Output** : ([1], [3], [5], [6], [7], [9])
>
>  **Input** : test_list = [1]  
>  **Output** : ([1])

 **Method #1 : Using list comprehension + tuple()**  
This is one of the ways in which this task can be performed. In this, we
construct and iterate the list using list comprehension and finally convert
the result list to tuple using tuple().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert List to Single valued Lists in Tuple

# Using list comprehension + tuple()

 

# initializing lists

test_list = [6, 8, 4, 9, 10, 2]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Convert List to Single valued Lists in Tuple

# Using list comprehension + tuple()

res = tuple([ele] for ele in test_list)

 

# printing result 

print("Tuple after conversion : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [6, 8, 4, 9, 10, 2]
    Tuple after conversion : ([6], [8], [4], [9], [10], [2])
    

