Python – Kth digit Sum



Given a Numeric list, extract the sum of the Kth digit.

>  **Input** : test_list = [5467, 34232, 45456, 22222, 3455], K = 2  
> **Output** : 19  
> **Explanation** : 6 + 2 + 4 + 2 + 5 = 19.
>
>  **Input** : test_list = [5467, 34232, 45456, 22222, 3455], K = 0  
> **Output** : 17  
> **Explanation** : 5 + 3 + 4 + 2 + 3 = 17.

**Method #1 : Using** **str()** **\+ loop**

In this, we convert the element to string and then compute the summation of
only Kth digit by extracting it using loop.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Kth digit Sum

# Using loop + sum()

 

# initializing list

test_list = [5467, 34232, 45456, 22222, 3455]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 2

 

res = 0

for ele in test_list:

 

 # adding Kth digit

 res += int(str(ele)[K])

 

# printing result

print("Kth digit sum : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [5467, 34232, 45456, 22222, 3455]
    Kth digit sum : 19

 **Method #2 : Using** **sum()** **+** **list comprehension** **\+ str()**

In this, we perform the task of getting sum using sum(), and list
comprehension is used to get one-liner approach to the problem.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Kth digit Sum 

# Using sum() + list comprehension + str()

 

# initializing list

test_list = [5467, 34232, 45456, 22222, 3455]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 2

 

# sum() getting summation

res = sum([int(str(ele)[K]) for ele in test_list])

 

# printing result 

print("Kth digit sum : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [5467, 34232, 45456, 22222, 3455]
    Kth digit sum : 19

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

