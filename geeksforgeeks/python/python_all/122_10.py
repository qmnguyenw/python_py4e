Python | Find Maximum difference between tuple pairs



Sometimes, while working with data, we might have a problem in which we need
to find maximum differene between available pairs in list. This can be
application to many problems in mathematics domain. Let’s discuss certain ways
in which this task can be performed.

 **Method #1 : Usingmax() \+ list comprehension**  
The combination of this functions can be used to perform this task. In this,
we compute the absolute difference of all pairs and then return the max of it
using max().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Maximum difference tuple pair 

# Using list comprehension + max()

 

# initialize list

test_list = [(3, 5), (1, 7), (10, 3), (1,
2)]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Maximum difference tuple pair 

# Using list comprehension + max()

temp = [abs(b - a) for a, b in test_list]

res = max(temp)

 

# printing result

print("Maximum difference among pairs : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(3, 5), (1, 7), (10, 3), (1, 2)]
    Maximum difference among pairs : 7
    

**Method #2 : Usingmax() \+ lambda**  
This is similar to above method. In this the task performed by list
comprehension is solved using lambda function, providing the difference
computation logic. Returns the max. difference pair.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Maximum difference tuple pair 

# Using lambda + max()

 

# initialize list

test_list = [(3, 5), (1, 7), (10, 3), (1,
2)]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Maximum difference tuple pair 

# Using lambda + max()

res = max(test_list, key = lambda sub: abs(sub[1] -
sub[0]))

 

# printing result

print("Maximum difference among pairs : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(3, 5), (1, 7), (10, 3), (1, 2)]
    Maximum difference among pairs : (10, 3)
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

