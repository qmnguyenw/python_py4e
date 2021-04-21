Python – Replace String by Kth Dictionary value



Given list of Strings, replace the value mapped by Kth value of mapped list.

>  **Input** : test_list = [“Gfg”, “is”, “Best”], subs_dict = {“Gfg” : [5, 6,
> 7], “is” : [7, 4, 2]}, K = 0  
>  **Output** : [5, 7, “Best”]  
>  **Explanation** : “Gfg” and “is” is replaced by 5, 7 as 0th index in
> dictionary value list.
>
>  **Input** : test_list = [“Gfg”, “is”, “Best”], subs_dict = {“Gfg” : [5, 6,
> 7], “Best” : [7, 4, 2]}, K = 0  
>  **Output** : [5, “is”, 7]  
>  **Explanation** : “Gfg” and “Best” is replaced by 5, 7 as 0th index in
> dictionary value list.

 **Method #1 : Using list comprehension**

This is one of the ways in which this task can be performed. In this, we
perform the task iteration and conditional replacement inside one-liner in
list comprehension.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace String by Kth Dictionary value 

# Using list comprehension

 

# initializing list

test_list = ["Gfg", "is", "Best"]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing subs. Dictionary

subs_dict = {

 "Gfg" : [5, 6, 7], 

 "is" : [7, 4, 2], 

}

 

# initializing K 

K = 2

 

# using list comprehension to solve

# problem using one liner

res = [ele if ele not in subs_dict else subs_dict[ele][K]

 for ele in test_list]

 

# printing result 

print("The list after substitution : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : ['Gfg', 'is', 'Best']
    The list after substitution : [7, 2, 'Best']
    

**Method #2 : Using get() + list comprehension**

The combination of above functions can be used to solve this problem. In this,
we iterate using list comprehension and check for key existence and
substitution using get().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace String by Kth Dictionary value 

# Using get() + list comprehension

 

# initializing list

test_list = ["Gfg", "is", "Best"]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing subs. Dictionary

subs_dict = {

 "Gfg" : [5, 6, 7], 

 "is" : [7, 4, 2], 

}

 

# initializing K 

K = 2

 

# using list comprehension to solve problem using one liner

# get() to perform presence checks and assign default value

res = [subs_dict.get(ele, ele) for ele in test_list]

res = [ele[K] if isinstance(ele, list) else ele for ele
in res] 

 

# printing result 

print("The list after substitution : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : ['Gfg', 'is', 'Best']
    The list after substitution : [7, 2, 'Best']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

