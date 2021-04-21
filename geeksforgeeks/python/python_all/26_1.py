Python – Calculate the percentage of positive elements of the list



Given a list, compute the percentage of positive elements in the list.

>  **Input** : test_list = [4, 6, -2, 3, -8, -9, -1, 8, 9, 1]  
> **Output** : 60.0  
> **Explanation** : 6/10 elements are positive.
>
>  **Input** : test_list = [-4, 6, -2, 3, -8, -9, -1, 8, 9, 1]  
> **Output** : 50.0  
> **Explanation** : 5/10 elements are positive.

**Method #1 : Using** **len()** **+** **list comprehension**

In this, we construct positive elements list using list comprehension and then
compute the length of lists using len(), both lengths are divided and
multiplied by 100 to get percentage count.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Positive values percentage 

# Using len() + list comprehension

 

# initializing list

test_list = [4, 6, -2, 3, -8, 0, -1,
8, 9, 1]

 

# printing original list

print("The original list is : " + str(test_list))

 

# getting filtered list using comprehension and 

# division to get fraction

res = (len([ele for ele in test_list if ele > 0])
/ len(test_list)) * 100

 

# printing result 

print("Positive elements percentage : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [4, 6, -2, 3, -8, 0, -1, 8, 9, 1]
    Positive elements percentage : 60.0

 **Method #2 : Using** **filter()** **+** **lambda** **\+ len()**

In this, we perform tasks of getting positive elements using filter() and
lambda, rest all tasks are performed similar to the above methods.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Positive values percentage

# Using filter() + lambda + len()

 

# initializing list

test_list = [4, 6, -2, 3, -8, 0, -1,
8, 9, 1]

 

# printing original list

print("The original list is : " + str(test_list))

 

# getting filtered list using filter(), lambda and

# division to get fraction

res = (len(list(filter(lambda ele: ele > 0,
test_list))) / len(test_list)) * 100

 

# printing result

print("Positive elements percentage : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [4, 6, -2, 3, -8, 0, -1, 8, 9, 1]
    Positive elements percentage : 60.0

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

