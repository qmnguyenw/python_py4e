Python – Element Index in Range Tuples



Sometimes, while working with Python data, we can have a problem in which we
need to find the element position in continuous equi ranged tuples in list.
This problem has applications in many domains including day-day programming
and competitive programming. Let’s discuss certain ways in which this task can
be performed.

>  **Input** :  
> test_list = [(0, 10), (11, 20), (21, 30), (31, 40)]  
> K = 37  
>  **Output** : 3
>
>  **Input** :  
> test_list = [(0, 9), (10, 19), (20, 29), (30, 39)]  
> K = 37  
>  **Output** : 3

 **Method #1 : Using loop**  
This is brute force way in which this task can be performed. In this, we
iterate for all the elements in the list and then using comparison operators,
find the position of the desired element.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Element Index in Range Tuples

# Using loop

 

# initializing list

test_list = [(0, 10), (11, 20), (21, 30),
(31, 40), (41, 50)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing Element

K = 37

 

# Element Index in Range Tuples

# Using loop

res = None

for idx, ele in enumerate(test_list):

 if K >= ele[0] and K <= ele[1]:

 res = idx

 

# printing result 

print("The position of element : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [(0, 10), (11, 20), (21, 30), (31, 40), (41, 50)]
    The position of element : 3
    

