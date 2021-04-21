Python – Test if K occurs N consecutive times



Sometimes, while working with Python list, we can have a problem in which we
need to check if a particular number occurs N consecutive times. This can have
application in many domains including day-day programming. Lets discuss
certain ways in which this task can be performed.

 **Method #1 : Using list comprehension**  
This is a way in which this task can be performed. In this, we iterate the
list and check for occurrence in list using multiplication operator in a one
liner.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Test if K occurs N consecutive times

# using list comprehension

 

# Initializing list

test_list = [1, 3, 4, 4, 4, 3, 3, 2,
2, 1]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing K 

K = 4

 

# Initializing N 

N = 3

 

# Test if K occurs N consecutive times

# using list comprehension

res = [K] * N in (test_list[i : i + N] for i in
range(len(test_list) - N))

 

# printing result 

print ("Does K occur N consecutive times ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 3, 4, 4, 4, 3, 3, 2, 2, 1]
    Does K occur N consecutive times ? : True
    

**Method #2 : Usinglambda + join()**  
This is yet another way to perform this task. In this, we perform the task of
checking for consecution using lambda and join() is used to get the elements
groups that are consecutive.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Test if K occurs N consecutive times

# using lambda + join()

 

# Initializing list

test_list = [1, 3, 4, 4, 4, 3, 3, 2,
2, 1]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing K 

K = 4

 

# Initializing N 

N = 3

 

# Test if K occurs N consecutive times

# using lambda + join()

res = bool(lambda ele: str(K) * N in
''.join(str(num) for num in test_list))

 

# printing result 

print ("Does K occur N consecutive times ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 3, 4, 4, 4, 3, 3, 2, 2, 1]
    Does K occur N consecutive times ? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

