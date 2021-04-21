Python – Tuple Matrix Columns Summation



Sometimes, while working with Tuple Matrix, we can have a problem in which we
need to perform summation of each column of tuple matrix, at the element
level. This kind of problem can have application in Data Science domains.
Let’s discuss certain ways in which this task can be performed.

>  **Input** : test_list = [[(4, 5), (1, 2)], [(2, 4), (4, 6)]]  
>  **Output** : [(6, 9), (5, 8)]
>
>  **Input** : test_list = [[(4, 5), (1, 2), (6, 7)]]  
>  **Output** : [(4, 5), (1, 2), (6, 7)]

 **Method #1 : Using list comprehension +zip() + sum()**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of sum using sum() and zip() is used to perform column
wise pairing of all elements.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Tuple Matrix Columns Summation

# Using list comprehension + zip() + sum()

 

# initializing lists

test_list = [[(4, 5), (3, 2)], [(2, 2), (4,
6)], [(3, 2), (4, 5)]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Tuple Matrix Columns Summation

# Using list comprehension + zip() + sum()

res = [tuple(sum(ele) for ele in zip(*i)) for i
in zip(*test_list)]

 

# printing result 

print("Tuple matrix columns summation : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original list is : [[(4, 5), (3, 2)], [(2, 2), (4, 6)], [(3, 2), (4, 5)]]
    Tuple matrix columns summation : [(9, 9), (11, 13)]
    

