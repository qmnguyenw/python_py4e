Python | Record Point with Minimum difference



Sometimes, while working with data, we might have a problem in which we need
to find minimum differene between available pairs in list. This can be
application to many problems in mathematics domain. Let’s discuss certain ways
in which this task can be performed.

 **Method #1 : Usingmin() \+ list comprehension**  
The combination of this functions can be used to perform this task. In this,
we compute the absolute difference of all pairs and then return the min of it
using min().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Record Point with Minimum difference

# Using list comprehension + min()

 

# initialize list

test_list = [(3, 5), (1, 7), (10, 3), (1,
2)]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Record Point with Minimum difference

# Using list comprehension + min()

temp = [abs(b - a) for a, b in test_list]

res = min(temp)

 

# printing result

print("Minimum difference among pairs : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(3, 5), (1, 7), (10, 3), (1, 2)]
    Minimum difference among pairs : 1
    

**Method #2 : Usingmin() \+ lambda**  
This is similar to above method. In this the task performed by list
comprehension is solved using lambda function, providing the difference
computation logic. Returns the min. difference pair.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Record Point with Minimum difference 

# Using lambda + min()

 

# initialize list

test_list = [(3, 5), (1, 7), (10, 3), (1,
2)]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Record Point with Minimum difference 

# Using lambda + min()

res = min(test_list, key = lambda sub: abs(sub[1] -
sub[0]))

 

# printing result

print("Minimum difference among pairs : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(3, 5), (1, 7), (10, 3), (1, 2)]
    Minimum difference among pairs : (1, 2)
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

