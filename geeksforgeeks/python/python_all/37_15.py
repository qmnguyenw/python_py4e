Python – Skew Nested Tuple Summation



Given a Tuple, nesting at 2nd position, return summation of 1st elements.

>  **Input** : test_tup = (5, (6, (1, (9, None))))  
>  **Output** : 21  
>  **Explanation** : 9 + 6 + 5 + 1 = 21.
>
>  **Input** : test_tup = (5, (6, (1, None)))  
>  **Output** : 12  
>  **Explanation** : 1 + 6 + 5 = 12.

 **Method #1 : Using infinite loop**

In this, we perform get into skew structure while summation using infinite
loop and break when we reach None value.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Skew Nested Tuple Summation

# Using infinite loop

 

# initializing tuple

test_tup = (5, (6, (1, (9, (10, None)))))

 

# printing original tuple

print("The original tuple is : " + str(test_tup))

 

res = 0

while test_tup:

 res += test_tup[0]

 

 # assigning inner tuple as original

 test_tup = test_tup[1]

 

# printing result 

print("Summation of 1st positions : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original tuple is : (5, (6, (1, (9, (10, None)))))
    Summation of 1st positions : 31
    
    

**Method #2 : Using recursion**

In this, we perform summation and recur for the 2nd element of tuple, return
on None.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Skew Nested Tuple Summation

# Using recursion

 

# helper function to perform task

def tup_sum(test_tup):

 

 # return on None 

 if not test_tup:

 return 0

 else:

 return test_tup[0] + tup_sum(test_tup[1])

 

# initializing tuple

test_tup = (5, (6, (1, (9, (10, None)))))

 

# printing original tuple

print("The original tuple is : " + str(test_tup))

 

# calling fnc.

res = tup_sum(test_tup)

 

# printing result 

print("Summation of 1st positions : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original tuple is : (5, (6, (1, (9, (10, None)))))
    Summation of 1st positions : 31
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

