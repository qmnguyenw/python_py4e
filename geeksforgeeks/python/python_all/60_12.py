Python – How to Check if two lists are reverse equal



Sometimes, while working with Python lists, we can have a problem in which we
need to check if two lists are reverse of each other. This kind of problem can
have application in many domains such as day-day programming and school
programming. Let’s discuss certain ways in which this task can be performed.

>  **Input** : test_list1 = [5, 6, 7], test_list2 = [7, 6, 5]  
>  **Output** : True
>
>  **Input** : test_list1 = [5, 6], test_list2 = [7, 6]  
>  **Output** : False

 **Method #1 : Usingreversed() and "==" operator**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of reversing using reversed() and testing for equality
using “==” operator.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if two lists are reverse equal

# Using reversed() + == operator

 

# initializing lists

test_list1 = [5, 6, 7, 8]

test_list2 = [8, 7, 6, 5]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# Check if two lists are reverse equal

# Using reversed() + == operator

res = test_list1 == list(reversed(test_list2))

 

# printing result 

print("Are both list reverse of each other ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original list 1 : [5, 6, 7, 8]
    The original list 2 : [8, 7, 6, 5]
    Are both list reverse of each other ? : True
    

