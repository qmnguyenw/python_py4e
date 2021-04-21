Python – Maximum Sum Record



Sometimes, while working with data, we might have a problem in which we need
to find maximum sum between available pairs in list. This can be application
to many problems in mathematics domain. Let’s discuss certain ways in which
this task can be performed.

 **Method #1 : Usingmax() \+ list comprehension**  
The combination of this functions can be used to perform this task. In this,
we compute the sum of all pairs and then return the max of it using max().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Maximum Sum Record

# Using list comprehension + max()

 

# initialize list

test_list = [(3, 5), (1, 7), (10, 3), (1,
2)]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Maximum Sum Record

# Using list comprehension + max()

temp = [b + a for a, b in test_list]

res = max(temp)

 

# printing result

print("Maximum sum among pairs : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(3, 5), (1, 7), (10, 3), (1, 2)]
    Maximum sum among pairs : 13
    

**Method #2 : Usingmax() \+ lambda**  
This is similar to above method. In this the task performed by list
comprehension is solved using lambda function, providing the sum computation
logic. Returns the max. sum pair.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Maximum Sum Record

# Using lambda + max()

 

# initialize list

test_list = [(3, 5), (1, 7), (10, 3), (1,
2)]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Maximum Sum Record

# Using lambda + max()

res = max(test_list, key = lambda sub: sub[1] +
sub[0])

 

# printing result

print("Maximum sum among pairs : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(3, 5), (1, 7), (10, 3), (1, 2)]
    Maximum sum among pairs : 13
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

