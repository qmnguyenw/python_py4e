Python – Extract elements with Frequency greater than K



Given a List, extract all elements whose frequency is greater than K.

>  **Input** : test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3  
>  **Output** : [4, 3]  
>  **Explanation** : Both elements occur 4 times.
>
>  **Input** : test_list = [4, 6, 4, 3, 3, 4, 3, 4, 6, 6], K = 2  
>  **Output** : [4, 3, 6]  
>  **Explanation** : Occur 4, 3, and 3 times respectively.

 **Method #1 : Using count() + loop**

In this, we use count() to get the frequency, and loop is used to iterate for
each of elements of List.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract elements with Frequency greater than K

# Using count() + loop

 

# initializing list

test_list = [4, 6, 4, 3, 3, 4, 3, 7,
8, 8]

 

# printing string

print("The original list : " + str(test_list))

 

# initializing K 

K = 2

 

res = [] 

for i in test_list: 

 

 # using count() to get count of elements

 freq = test_list.count(i) 

 

 # checking if not already entered in results

 if freq > K and i not in res: 

 res.append(i)

 

# printing results 

print("The required elements : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [4, 6, 4, 3, 3, 4, 3, 7, 8, 8]
    The required elements : [4, 3]
    

**Method #2 : Using list comprehension + Counter()**

In this, we perform the task of counting using Counter() and the iteration
part is done inside list comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract elements with Frequency greater than K

# Using list comprehension + Counter()

from collections import Counter

 

# initializing list

test_list = [4, 6, 4, 3, 3, 4, 3, 7,
8, 8]

 

# printing string

print("The original list : " + str(test_list))

 

# initializing K 

K = 2

 

# using list comprehension to bind result

res = [ele for ele, cnt in Counter(test_list).items() if cnt
> K]

 

# printing results 

print("The required elements : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [4, 6, 4, 3, 3, 4, 3, 7, 8, 8]
    The required elements : [4, 3]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

