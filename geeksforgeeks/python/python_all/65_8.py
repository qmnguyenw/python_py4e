Python – Similar index pairs in Tuple lists



Sometimes, while working with Python tuples, we can have a problem in which we
need to perform similar index pairing. This kind of problem is peculiar, but
can occur across certain domains. Let’s discuss certain way in which this task
can be performed.

>  **Input** :  
> test_list1 = [(5, ), (1, ), (8, ), (10, )]  
> test_list2 = [(8, ), (1, ), (11, ), (9, )]  
>  **Output** : [[(5, 8)], [(1, 1)], [(8, 11)], [(10, 9)]]
>
>  **Input** :  
> test_list1 = [(5, 6, 7, 6)]  
> test_list2 = [(8, 6, 7, 9)]  
>  **Output** : [[(5, 8), (6, 6), (7, 7), (6, 9)]]

 **Method : Using list comprehension +zip()**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of zipping similar index elements using zip() and list
comprehension is used to compile all the pairs.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Similar index pairs in Tuple lists

# Using list comprehension + zip()

 

# initializing lists

test_list1 = [(5, 6), (1, 2), (8, 9), (10,
33)]

test_list2 = [(8, 7), (1, 3), (11, 23), (9,
4)]

 

# printing original list

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Similar index pairs in Tuple lists

# Using list comprehension + zip()

res = [list(zip(a, b)) for a, b in zip(test_list1,
test_list2)]

 

# printing result 

print("The paired tuples : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list 1 is : [(5, 6), (1, 2), (8, 9), (10, 33)]
    The original list 2 is : [(8, 7), (1, 3), (11, 23), (9, 4)]
    The paired tuples : [[(5, 8), (6, 7)], [(1, 1), (2, 3)], [(8, 11), (9, 23)], [(10, 9), (33, 4)]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

