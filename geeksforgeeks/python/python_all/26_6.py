Python – Extract Rear K digits from Numbers



Given an Integer list, extract rear K digits from it.

>  **Input** : test_list = [5645, 23567, 34543, 87652, 2342], K = 2  
> **Output** : [45, 67, 43, 52, 42]  
> **Explanation** : Last 2 digits extracted.
>
>  **Input** : test_list = [5645, 23567, 34543, 87652, 2342], K = 4  
> **Output** : [5645, 3567, 4543, 7652, 2342]  
> **Explanation** : Last 4 digits extracted.  
>

**Method #1 : Using** **list comprehension** **\+ % operator**

In this technique, we modulo each number with 10^K to get the desired last K
digits of each number.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Rear K digits from Numbers

# Using list comprehension + % operator 

 

# initializing list

test_list = [5645, 23567, 34543, 87652, 2342]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 3

 

# Getting remainder for each element

res = [ele % (10 ** K) for ele in test_list]

 

# printing result 

print("Rear K digits of elements ? : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [5645, 23567, 34543, 87652, 2342]
    Rear K digits of elements ? : [645, 567, 543, 652, 342]
    

**Method #2 : Using** **str()** **\+ slicing**

In this, we perform task of getting rear elements using list slicing, and
str() is used to convert each element to string.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Rear K digits from Numbers

# Using str() + slicing 

 

# initializing list

test_list = [5645, 23567, 34543, 87652, 2342]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 3

 

# getting integer using int() after slicing string

res = [int(str(idx)[-K:]) for idx in test_list]

 

# printing result 

print("Rear K digits of elements ? : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [5645, 23567, 34543, 87652, 2342]
    Rear K digits of elements ? : [645, 567, 543, 652, 342]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

