Python – All pair combinations of 2 tuples



Sometimes, while working with Python tuples data, we can have a problem in
which we need to extract all possible combination of 2 argument tuples. This
kind of application can come in Data Science or gaming domains. Let’s discuss
certain ways in which this task can be performed.

>  **Input** : test_tuple1 = (7, 2), test_tuple2 = (7, 8)  
>  **Output** : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8,
> 2)]
>
>  **Input** : test_tuple1 = (9, 2), test_tuple2 = (7, 8)  
>  **Output** : [(9, 7), (9, 8), (2, 7), (2, 8), (7, 9), (7, 2), (8, 9), (8,
> 2)]

 **Method #1 : Using list comprehension**  
This is one of the ways in which this task can be performed. In this, we
perform task of forming one index combination in one pass, in other pass
change the index, and add to the initial result list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# All pair combinations of 2 tuples

# Using list comprehension

 

# initializing tuples

test_tuple1 = (4, 5)

test_tuple2 = (7, 8)

 

# printing original tuples

print("The original tuple 1 : " + str(test_tuple1))

print("The original tuple 2 : " + str(test_tuple2))

 

# All pair combinations of 2 tuples

# Using list comprehension

res = [(a, b) for a in test_tuple1 for b in test_tuple2]

res = res + [(a, b) for a in test_tuple2 for b in
test_tuple1]

 

# printing result 

print("The filtered tuple : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original tuple 1 : (4, 5)
    The original tuple 2 : (7, 8)
    The filtered tuple : [(4, 7), (4, 8), (5, 7), (5, 8), (7, 4), (7, 5), (8, 4), (8, 5)]
    

