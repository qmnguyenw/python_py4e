Python – Nearest K Sort



Given a List of elements, perform sort on basis of its distance from K.

>  **Input** : test_list = [6, 7, 4, 11, 17, 8, 3], K = 10  
> **Output** : [11, 8, 7, 6, 4, 17, 3]  
> **Explanation** : 11-10 = 1; < 10 – 8 = 2 .. Ordered by increasing
> difference.
>
>  **Input** : test_list = [6, 7, 4, 11], K = 10  
> **Output** : [11, 7, 6, 4]  
> **Explanation** : 11-10 = 1; < 10 – 7 = 3 .. Ordered by increasing
> difference.

**Method #1 : Using sort() + abs()**

In this, we perform sorting using _sort()_ and _abs()_ is used to get the
difference, used for logic formation to perform sort operation upon.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Nearest K Sort

# Using sort() + abs()

 

# getting absolute difference

def get_diff(ele):

 

 # returning absolute difference

 return abs(ele - K)

 

 

# initializing list

test_list = [6, 7, 4, 11, 17, 8, 3]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 10

 

# performing inplace sort using sort()

test_list.sort(key=get_diff)

 

# printing result

print("Sorted List : " + str(test_list))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [6, 7, 4, 11, 17, 8, 3]
    Sorted List : [11, 8, 7, 6, 4, 17, 3]
    
    

**Method #2 : Using sorted() + lambda + abs()**

Similar to above method, here, _sorted()_ is used to perform sort operation
and rather than calling external function, _lambda_ is used to provide sorting
logic.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Nearest K Sort

# Using sorted() + abs() + lambda

 

# initializing list

test_list = [6, 7, 4, 11, 17, 8, 3]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 10

 

# sorted() used to perform sorting, lambda function to get logic

res = sorted(test_list, key=lambda ele: abs(ele - K))

 

# printing result

print("Sorted List : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [6, 7, 4, 11, 17, 8, 3]
    Sorted List : [11, 8, 7, 6, 4, 17, 3]
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

