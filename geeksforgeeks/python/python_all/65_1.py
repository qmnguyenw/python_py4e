Python – Add custom dimension in Matrix



Sometimes, while working with Python Matrix, we can have a problem in which we
need to add another dimension of custom values, this kind of problem can have
problem in all kinds of domains such as day-day programming and competitive
programming. Let’s discuss certain ways in which this task can be performed.

>  **Input** :  
> test_list = [(5, 6, 7, 8)]  
> vals = [10]  
>  **Output** : [(5, 6, 7, 8, 10)]
>
>  **Input** :  
> test_list = [(5, ), (6, ), (7, ), (8, )]  
> vals = [10, 9, 8, 7]  
>  **Output** : [(5, 10), (6, 9), (7, 8), (8, 7)]

 **Method #1 : Usingzip() \+ list comprehension + “+” operator**  
The combination of above functions can be used to solve this problem. In this,
we use + operator to add an element and zip() is used to extend this logic to
every row of Matrix.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Add custom dimension in Matrix

# Using zip() + list comprehension + "+" operator

 

# initializing list

test_list = [(5, 6), (1, 2), (7, 8), (9,
12)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing Column values 

vals = [4, 5, 7, 3]

 

# Add custom dimension in Matrix

# Using zip() + list comprehension + "+" operator

res = [i + (j, ) for i, j in zip(test_list, vals)]

 

# printing result 

print("The result after adding dimension : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [(5, 6), (1, 2), (7, 8), (9, 12)]
    The result after adding dimension : [(5, 6, 4), (1, 2, 5), (7, 8, 7), (9, 12, 3)]
    

