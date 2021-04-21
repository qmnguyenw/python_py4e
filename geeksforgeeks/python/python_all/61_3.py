Python – Absolute Tuple Summation



Sometimes, while working with Python tuples, we can have a problem in which we
need to perform the summation of absolute values of intermediate tuple
elements. This kind of problem can have application in many domains such as
web development. Let’s discuss certain ways in which this task can be
performed.

>  **Input** : test_list = [(-7, -8), (-5, -6)]  
>  **Output** : [15, 11]
>
>  **Input** : test_list = [(-1, -2, -4)]  
>  **Output** : [7]

 **Method #1 : Usingsum() + list comprehension + abs()**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of computing sum using sum(), abs() for absolute values,
and list comprehension to iterate through the list and inside each tuple,
generator expression is used to iterate.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Absolute Tuple Summation

# Using sum() + list comprehension + abs()

 

# initializing list

test_list = [(7, -8), (-5, -6), (-7, 2),
(6, 8)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Absolute Tuple Summation

# Using sum() + list comprehension + abs()

res = [sum([abs(ele) for ele in sub]) for sub in
test_list]

 

# printing result 

print("The absolute sum list: " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [(7, -8), (-5, -6), (-7, 2), (6, 8)]
    The absolute sum list: [15, 11, 9, 14]
    

