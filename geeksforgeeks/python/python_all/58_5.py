Python – Squash consecutive values of K



Sometimes, while working with Python lists, we can have a problem in which we
need to perform removal of duplicate consecutive values of particular element.
This kind of problem can have application in many domains such as competitive
programming and web development. Let’s discuss certain ways in which this task
can be performed.

>  **Input** : test_list = [4, 5, 5, 4, 3, 3, 5, 5, 5, 6, 5], K = 3  
>  **Output** : [4, 5, 5, 4, 3, 5, 5, 5, 6, 5]
>
>  **Input** : test_list = [1, 1, 1, 1], K = 1  
>  **Output** : [1]

 **Method #1 : Usingzip() \+ yield**  
The combination of above functions provide one of the ways to solve this
problem. In this, we perform the task of checking consecution duplications
using zipping current and next element list, and yield is used to render the
element basis of condition.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Squash consecutive values of K

# Using zip() + yield

 

# helper function

def hlper_fnc(test_list, K):

 for sub1, sub2 in zip(test_list, test_list[1:]):

 if sub1 == sub2 == K:

 continue

 else:

 yield sub1

 yield sub2 

 

# initializing list

test_list = [4, 5, 5, 4, 3, 3, 5, 5,
5, 6, 5] 

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 5

 

# Squash consecutive values of K

# Using zip() + yield

res = list(hlper_fnc(test_list, K))

 

# printing result 

print("List after filteration : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original list is : [4, 5, 5, 4, 3, 3, 5, 5, 5, 6, 5]
    List after filteration : [4, 5, 4, 3, 3, 5, 6, 5]
    

