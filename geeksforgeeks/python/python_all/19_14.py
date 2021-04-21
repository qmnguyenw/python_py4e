Python – Consecutive identical elements count



Given the elements list, get all the elements that have an identical element
as the next element.

>  **Input** : test_list = [4, 5, 5, 5, 5, 6, 6, 7, 8, 2, 2, 10]  
> **Output** : 3  
> **Explanation** : 5, 6 and 2 has identical element as their next element.
>
>  **Input** : test_list = [4, 5, 5, 5, 5, 6, 6, 7, 8, 2, 3, 10]  
> **Output** : 2  
> **Explanation** : 5 and 6 has identical element as their next element.

**Method #1 : Using loop + set()**

In this, we iterate and check for the next element, if equal to current, we
add in result list, then it is converted to set to get distinct elements.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Consecutive identical elements count

# Using loop + set()

 

# initializing list

test_list = [4, 5, 5, 5, 5, 6, 6, 7,
8, 2, 2, 10]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = []

for idx in range(0, len(test_list) - 1):

 

 # getting Consecutive elements 

 if test_list[idx] == test_list[idx + 1]:

 res.append(test_list[idx])

 

# getting count of unique elements 

res = len(list(set(res)))

 

# printing result 

print("Consecutive identical elements count : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [4, 5, 5, 5, 5, 6, 6, 7, 8, 2, 2, 10]
    Consecutive identical elements count : 3
    

**Method #2 : Using list comprehension + set() + len()**

This method is similar to above method, difference being its shorter way to
solve this problem. The len(), and set() are used for task of getting unique
elements count.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Consecutive identical elements count

# Using list comprehension + set() + len()

 

# initializing list

test_list = [4, 5, 5, 5, 5, 6, 6, 7,
8, 2, 2, 10]

 

# printing original list

print("The original list is : " + str(test_list))

 

# getting Consecutive elements

res = [test_list[idx] for idx in range(

 0, len(test_list) - 1) if test_list[idx] ==
test_list[idx + 1]]

 

# getting count of unique elements

res = len(list(set(res)))

 

# printing result

print("Consecutive identical elements count : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [4, 5, 5, 5, 5, 6, 6, 7, 8, 2, 2, 10]
    Consecutive identical elements count : 3
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

