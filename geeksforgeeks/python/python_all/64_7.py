Python – Check if tuple list has all K



Sometimes, while working with Python records, we can have a problem in which
we need to test if all the elements in tuples of tuple list are K. This
problem can have application in many data domains such as Machine Learning and
Web development. Let’s discuss certain ways in which this task can be
performed.

>  **Input** : test_list = [(4, 4, 4, 4)], K = 4  
>  **Output** : True
>
>  **Input** : test_list = [(7), (5, ), (5, ), (5, )], K = 5  
>  **Output** : False

 **Method #1 : Using loop**  
This is brute force way in which this task can be performed. In this, we use
loop to iterate each value in tuple and test if its K, if we find any element
to be non-K, False is returned.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if tuple list has all K

# Using loop

 

# initializing list

test_list = [(4, 4), (4, 4, 4), (4, 4),
(4, 4, 4, 4), (4, )]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 4

 

# Check if tuple list has all K

# Using loop

res = True

for tup in test_list: 

 for ele in tup:

 if ele != K:

 res = False

 

# printing result 

print("Are all elements K ? : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [(4, 4), (4, 4, 4), (4, 4), (4, 4, 4, 4), (4, )]
    Are all elements K ? : True
    

