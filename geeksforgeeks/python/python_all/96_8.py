Python | Multiplication till Null value



The prefix array is quite famous in the programming world. This article would
discuss a variation of this scheme. This deals with the cumulative list
product till a False value, and again starts cumulation of product from
occurrence of True value. Let’s discuss certain way in which this can be
performed.

 **Method #1 : Using Naive Method**  
In the naive method, we just construct the new list comprising of the the
product of prev. value of list until False and restarts the procedure once a
True value is encountered.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Multiplication till Null value

# using naive method 

 

# initializing list of lists

test_list = [1, 3, 4, False, 4, 5, False,
7, 8]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# Multiplication till Null value

# using naive method

for i in range(1, len(test_list)):

 if test_list[i]: 

 test_list[i] *= test_list[i - 1]

 else:

 test_list[i] = 1

 

# printing result

print ("The computed modified new list : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 3, 4, False, 4, 5, False, 7, 8]
    The computed modified new list : [1, 3, 12, 1, 4, 20, 1, 7, 56]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

