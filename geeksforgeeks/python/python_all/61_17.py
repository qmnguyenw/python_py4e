Python – Split in Nested tuples



Sometimes, while working with Python tuples, we can have a problem in which we
need to perform split of elements in nested tuple, by a certain delimiter.
This kind of problem can have application in different data domains. Let’s
discuss certain ways in which this task can be performed.

>  **Input** : test_list = [(3, (‘Gfg’, ‘best’, 6)), (10, (‘CS’, ‘good’, 9))]  
>  **Output** : [[3, ‘Gfg’, ‘best’, 6], [10, ‘CS’, ‘good’, 9]]
>
>  **Input** : test_list = [(3, (1, 2, 3, 6))]  
>  **Output** : [[3, 1, 2, 3, 6]]

 **Method #1 : Using list comprehension +unpack operator(*)**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of unpacking the elements by delimiter using * operator
and list comprehension to iterate and form pairs.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Split in Nested tuples

# Using list comprehension + unpack operator

 

# initializing list

test_list = [(3, ('Gfg', 'best')), (10, ('CS',
'good')), (7, ('Gfg', 'better'))]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Split in Nested tuples

# Using list comprehension + unpack operator

res = [[a, *b] for a, b in test_list]

 

# printing result 

print("The splitted elements : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [(3, ('Gfg', 'best')), (10, ('CS', 'good')), (7, ('Gfg', 'better'))]
    The splitted elements : [[3, 'Gfg', 'best'], [10, 'CS', 'good'], [7, 'Gfg', 'better']]
    

