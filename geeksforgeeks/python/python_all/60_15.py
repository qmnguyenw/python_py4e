Python – K length Concatenate Single Valued Tuple



Sometimes, while working with Python Tuples, we can have a problem in which we
need to perform concatenation of single values tuples, to make them into
groups of bigger size. This kind of problem can occur in web development and
day-day programming. Let’s discuss certain ways in which this task can be
performed.

>  **Input** : test_list = [(3, ), (6, ), (8, ), (2, ), (9, ), (4, ), (7, ),
> (1, )], K = 4  
>  **Output** : [(3, 6, 8, 2), (9, 4, 7, 1)]
>
>  **Input** : test_list = [(3, ), (6, ), (8, ), (2, ), (9, ), (4, ), (7, ),
> (1, )], K = 2  
>  **Output** : [(3, 6), (8, 2), (9, 4), (7, 1)]

 **Method #1 : Usingzip() \+ list comprehension**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of forming groups using zip() and construction of values
using list comprehension. The size of K can only be limited to 2.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# K length Concatenate Single Valued Tuple

# Using zip() + list comprehension

 

# initializing lists

test_list = [(3, ), (6, ), (8, ), (2, ), (9, ),
(4, )]

 

# printing original list

print("The original list is : " + str(test_list))

 

# K length Concatenate Single Valued Tuple

# Using zip() + list comprehension

res = [a + b for a, b in zip(test_list[::2],
test_list[1::2])]

 

# printing result 

print("Concatenated tuples : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original list is : [(3, ), (6, ), (8, ), (2, ), (9, ), (4, )]
    Concatenated tuples : [(3, 6), (8, 2), (9, 4)]
    

