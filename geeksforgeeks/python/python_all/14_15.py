Python – Find the distance betwewn first and last even elements in a List



Given a List, write a Python program to find the span of even elements in
list, i.e distance between first and last occurrence of even element.

 **Examples:**

>  **Input** : test_list = [1, 3, 7, 4, 7, 2, 9, 1, 10, 11]  
> **Output** : 5  
> **Explanation** : Even elements begin at 4 and end at 10, spanning 5
> indices.  
>
>
> **Input** : test_list = [1, 3, 7, 4, 7, 2, 9, 1, 1, 11]  
> **Output** : 2  
> **Explanation** : Even elements begin at 4 and end at 2, spanning 2 indices.  
>

**Method #1: Using** **list comprehension**

  

  

In this we get all the indices of all even elements using list comprehension
and then perform difference of first and last index of matched elements in
list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Even elements span in list

# Using list comprehension

 

# initializing Matrix

test_list = [1, 3, 7, 4, 7, 2, 9, 1,
10, 11]

 

# printing original list

print("The original list is : " + str(test_list))

 

# getting even indices

indices_list = [idx for idx in range(

 len(test_list)) if test_list[idx] % 2 == 0]

 

# getting difference of first and last occurrence

res = indices_list[-1] - indices_list[0]

 

# printing result

print("Even elements span : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [1, 3, 7, 4, 7, 2, 9, 1, 10, 11]
    Even elements span : 5

 **Method #2 : Using** **filter()** **+** **lambda**

In this, we perform task of getting indices of elements using filter() and
lambda.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Even elements span in list

# Using filter() + lambda

 

# initializing Matrix

test_list = [1, 3, 7, 4, 7, 2, 9, 1,
10, 11]

 

# printing original list

print("The original list is : " + str(test_list))

 

# getting even indices

indices_list = list(

 filter(lambda x: test_list[x] % 2 == 0,
range(len(test_list))))

 

# getting difference of first and last occurrence

res = indices_list[-1] - indices_list[0]

 

# printing result

print("Even elements span : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [1, 3, 7, 4, 7, 2, 9, 1, 10, 11]
    Even elements span : 5

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

