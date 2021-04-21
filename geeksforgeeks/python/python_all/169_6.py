Python | Boolean list initialization



Many a times in programming, we require to initialize a list with some initial
values. In Dynamic programming, this is used more often and mostly the
requirement is to initialize with a boolean 0 or 1. Let’s discuss certain ways
in which this can be achieved.

 **Method #1 : Using list comprehension**  
This can easily be done with naive method, hence, can also be converted in
compact version using list comprehension. This is the most basic way to
perform this task.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to perform boolean list initializing 

# using list comprehension 

 

# using list comprehension 

# to perform boolean list initializing

res = [True for i in range(6)]

 

# printing result

print ("The True initialized list is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The True initialized list is : [True, True, True, True, True, True]
    

  
**Method #2 : Using * operator**  
This can be done using ***** operator with comparatively more readable and
compact way. We multiply the single list _N_ no. of times to get the desired
result.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to perform boolean list initializing 

# using * operator

 

# using * operator 

# to perform boolean list initializing

res = [True] * 6

 

# printing result

print ("The True initialized list is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    The True initialized list is : [True, True, True, True, True, True]
    

