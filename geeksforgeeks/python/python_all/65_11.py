Python – Elements Frequency in Mixed Nested Tuple



Sometimes, while working with Python data, we can have a problem in which we
have data in form of nested and non nested form inside in a single tuple, and
we wish to count the element frequency in them. This kind of problem can come
in domains such as web development and Data Science. Let’s discuss certain
ways in which this task can be performed.

>  **Input** : test_tuple = (5, (6, (7, 8, 6)))  
>  **Output** : {5: 1, 6: 2, 7: 1, 8: 1}
>
>  **Input** : test_tuple = (5, 6, 7, 8)  
>  **Output** : {5: 1, 6: 1, 7: 1, 8: 1}

 **Method #1 : Using recursion + loop**  
The solution of this problem involved two steps. In first, we perform
flattening of tuple using recursion and then the counting is performed in
brute force manner using loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Elements Frequency in Mixed Nested Tuple

# Using recursion + loop

 

# helper_fnc

def flatten(test_tuple):

 for tup in test_tuple:

 if isinstance(tup, tuple):

 yield from flatten(tup)

 else:

 yield tup

 

# initializing tuple

test_tuple = (5, 6, (5, 6), 7, (8, 9),
9)

 

# printing original tuple

print("The original tuple : " + str(test_tuple))

 

# Elements Frequency in Mixed Nested Tuple

# Using recursion + loop

res = {}

for ele in flatten(test_tuple):

 if ele not in res:

 res[ele] = 0

 res[ele] += 1

 

# printing result 

print("The elements frequency : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original tuple : (5, 6, (5, 6), 7, (8, 9), 9)
    The elements frequency : {5: 2, 6: 2, 7: 1, 8: 1, 9: 2}
    

