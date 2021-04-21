Python program to test for Non-neighbours in List



Given teo elements, write a Python program to check that they don’t occur as
their neighbours in list

 **Examples:**

>  **Input** : test_list = [3, 7, 2, 1, 4, 5, 7, 9], i, j = 7, 4  
> **Output** : True  
> **Explanation** : 7 doesn’t occur are 4’s neighbour.
>
>  **Input** : test_list = [3, 7, 2, 1, 4, 5, 7, 9], i, j = 5, 4  
> **Output** : False  
> **Explanation** : 5 occurs are 4’s neighbour.  
>

**Method #1 : Using loop**

  

  

In this, we check for next and previous elements to not be i or j while
iteration of list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test for Non-neighbours in List

# Using loop

 

# initializing list

test_list = [3, 7, 2, 1, 4, 5, 7, 9]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing i, j

i, j = 7, 4

 

res = True

for idx in range(1, len(test_list) - 1):

 if test_list[idx] == i:

 

 # check for surrounding element to be j if i

 if test_list[idx - 1] == j or test_list[idx + 1]
== j:

 res = False

 break

 

# printing result

print("Are i, j Non-neighbours' : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [3, 7, 2, 1, 4, 5, 7, 9]
    Are i, j Non-neighbours' : True

 **Method #2 : Using** **all()**

This is one liner approach to solve this problem. In this, we perform task of
checking for all elements for neighbours using all() in generator expression
in all().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test for Non-neighbours in List

# Using all()

 

# initializing list

test_list = [3, 7, 2, 1, 4, 5, 7, 9]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing i, j

i, j = 7, 4

 

# checking for preceding and succeeding element 

# not to be j if curr is i

res = all(test_list[idx - 1] != j and test_list[idx +
1] !=

 j for idx in range(1, len(test_list) - 1) if
test_list[idx] == i)

 

# printing result

print("Are i, j Non-neighbours' : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [3, 7, 2, 1, 4, 5, 7, 9]
    Are i, j Non-neighbours' : True

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

