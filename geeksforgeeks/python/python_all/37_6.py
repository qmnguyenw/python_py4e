Python – Find Kth Even Element



Given a List, extract Kth occurrence of Even Element.

>  **Input** : test_list = [4, 6, 2, 3, 8, 9, 10, 11], K = 3  
>  **Output** : 8  
>  **Explanation** : K = 3, i.e 0 based index, 4, 6, 2 and 4th is 8.
>
>  **Input** : test_list = [4, 6, 2, 3, 8, 9, 10, 11], K = 2  
>  **Output** : 2  
>  **Explanation** : K = 2, i.e 0 based index, 4, 6, and 3rd is 2.

 **Method #1 : Using list comprehension**

In this, we extract list of even elements using % operator and use list index
access to get Kth even element.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Kth Even Element

# Using list comprehension

 

# initializing list

test_list = [4, 6, 2, 3, 8, 9, 10, 11]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 4

 

# list comprehension to perform iteration and % 2 check 

res = [ele for ele in test_list if ele % 2 ==
0][K]

 

# printing result 

print("The Kth Even Number : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [4, 6, 2, 3, 8, 9, 10, 11]
    The Kth Even Number : 10
    

**Method #2 : Using filter() + lambda**

In this, task of finding even elements is done using filter() + lambda
function.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Kth Even Element

# Using filter() + lambda

 

# initializing list

test_list = [4, 6, 2, 3, 8, 9, 10, 11]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 4

 

# list comprehension to perform iteration and % 2 check 

res = list(filter(lambda ele : ele % 2 == 0,
test_list))[K]

 

# printing result 

print("The Kth Even Number : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [4, 6, 2, 3, 8, 9, 10, 11]
    The Kth Even Number : 10
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

