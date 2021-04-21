Python – Elements with factors count less than K



Given a List of elements, get all elements with factors less than K.

 **Examples:**

>  **Input** : test_list = [60, 12, 100, 17, 18, 19]. K = 4  
> **Output** : [17, 19]  
> **Explanation** : Both elements have 2 factors.
>
>  **Input** : test_list = [60, 12, 100, 360, 18, 900]. K = 4  
> **Output** : []  
> **Explanation** : All have greater than 4 factors.  
>

**Method #1: Using** **list comprehension**

  

  

In this, we use list comprehension to get factors count, and other list
comprehension to iterate for all the elements in list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Elements with factors less than K

# Using list comprehension

 

 

def factors_less_k(ele, K):

 

 # comparing for factors

 return len([idx for idx in range(1, ele + 1) if
ele % idx == 0]) <= K

 

 

# initializing list

test_list = [60, 12, 100, 17, 18]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 4

 

# checking for each element

res = [ele for ele in test_list if factors_less_k(ele, K)]

 

# printing result

print("Filtered elements : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [60, 12, 100, 17, 18]
    Filtered elements : [17]
    

**Method #2 : Using** **filter()** **+** **lambda** **+** **len()** **\+ list
comprehension**

In this, task of filtering is done using filter() and lambda, len(), and list
comprehension is used to perform tasks of getting factors.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Elements with factors less than K

# Using filter() + lambda + len() + list comprehension

 

 

def factors_less_k(ele, K):

 

 # comparing for factors

 return len([idx for idx in range(1, ele + 1) if
ele % idx == 0]) <= K

 

 

# initializing list

test_list = [60, 12, 100, 17, 18]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 4

 

# filtering using filter() + lambda

res = list(filter(lambda ele: factors_less_k(ele, K),
test_list))

 

# printing result

print("Filtered elements : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [60, 12, 100, 17, 18]
    Filtered elements : [17]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

