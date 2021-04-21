Python – Find Product of Index Value and find the Summation



Given a List of elements, write a Python program to perform the product of
index and value and compute the summation.

 **Examples:**

>  **Input** : test_list = [5, 3, 4, 9, 1, 2]  
> **Output** : 76  
> **Explanation** : 5 + (3*2) 6 + 12 + 36 + 5 + 12 = 76  
>
>
> **Input** : test_list = [5, 3, 4]  
> **Output** : 23  
> **Explanation** : 5 + (3*2) 6 + 12 = 23

**Method #1: Using loop +** **enumerate()**

  

  

In this, we iterate for each element along with its index using enumerate()
and compute the product. Sum counter is maintained to update the intermediate
sum of the product computed.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Index Value Product Sum

# Using loop + enumerate()

 

# initializing list

test_list = [5, 3, 4, 9, 1, 2]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = 0

for idx, ele in enumerate(test_list):

 

 # updating summation of required product

 res += (idx + 1) * ele

 

# printing result

print("The computed sum : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [5, 3, 4, 9, 1, 2]
    The computed sum : 76

 **Method #2 : Using** **sum()** **+** **list comprehension** **+**
**enumerate()**

One liner way to solve this problem, in this, we perform task of getting
products iteration as list comprehension and summation at end is done using
sum().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Index Value Product Sum

# Using loop + enumerate()

 

# initializing list

test_list = [5, 3, 4, 9, 1, 2]

 

# printing original list

print("The original list is : " + str(test_list))

 

# one liner to solve problem using list comprehension

res = sum([(idx + 1) * ele for idx, ele in
enumerate(test_list)])

 

# printing result

print("The computed sum : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [5, 3, 4, 9, 1, 2]
    The computed sum : 76

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

