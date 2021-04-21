Python – Remove Elements in K distance with N



Given a list, remove all elements which are within K distance with N.

>  **Input** : test_list = [4, 5, 9, 1, 10, 6, 13 ], K = 3, N = 5  
> **Output** : [9, 1, 10, 13]  
> **Explanation** : 4 is removed as 5 – 4 = 1 < 3, hence its within distance.
>
>  **Input** : test_list = [1, 10, 6, 13 ], K = 3, N = 5  
> **Output** : [1, 10, 13]  
> **Explanation** : 4 is removed as 5 – 4 = 1 < 3, hence its within distance.

 **Method #1 : Using** **list comprehension**

In this, we extract only those elements which are at safe distance by
magnitude K to N using comparisons using list comprehension.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove Elements in K distance with N

# Using list comprehension

 

# initializing list

test_list = [4, 5, 9, 1, 10, 6, 13 ]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 3

 

# initializing N 

N = 5

 

# checking for elements in safe zone with respect to N

res = [ele for ele in test_list if ele < N - K or ele
> N + K]

 

# printing result 

print("Filtered elements : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [4, 5, 9, 1, 10, 6, 13]
    Filtered elements : [9, 1, 10, 13]
    

**Method #2 : Using** **filter()** **+** **lambda**

In this, task of filtering is done using filter() and lambda function.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove Elements in K distance with N

# Using filter() + lambda

 

# initializing list

test_list = [4, 5, 9, 1, 10, 6, 13 ]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 3

 

# initializing N 

N = 5

 

# checking for elements in safe zone with respect to N

res = list(filter(lambda ele : ele < N - K or ele > N
+ K, test_list))

 

# printing result 

print("Filtered elements : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [4, 5, 9, 1, 10, 6, 13]
    Filtered elements : [9, 1, 10, 13]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

