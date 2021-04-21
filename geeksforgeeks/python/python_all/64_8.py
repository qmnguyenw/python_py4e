Python – Check if Tuple contains only K elements



Sometimes, while working with Python tuples, we can have a problem in which we
need to test if any tuple contains elements from set K elements. This kind of
problem is quite common and have application in many domains such as web
development and day-day programming. Let’s discuss certain ways in which this
task can be done.

>  **Input** : test_tuple = (1, 2, 3, 2, 1, 2), K = [1, 2, 3, 4]  
>  **Output** : True
>
>  **Input** : test_tuple = (1, 2, 3), K = [1, 2]  
>  **Output** : False

 **Method #1 : Usingall()**  
This is one of the ways in which this task can be performed. In this, we check
for the presence of all the elements in tuple are just from certain set of
numbers using inbuilt function all().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if Tuple contains only K elements

# Using all()

 

# initializing tuple

test_tuple = (3, 5, 6, 5, 3, 6)

 

# printing original tuple

print("The original tuple : " + str(test_tuple))

 

# initializing K elements

K = [3, 6, 5]

 

# Check if Tuple contains only K elements

# Using all()

res = all(ele in K for ele in test_tuple)

 

# printing result 

print("Does tuples contains just from K elements : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original tuple : (3, 5, 6, 5, 3, 6)
    Does tuples contains just from K elements : True
    

