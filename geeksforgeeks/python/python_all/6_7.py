Python Program to convert String to Uppercase under the Given Condition



Given a String list, the task is to write a Python program to convert
uppercase strings if length is greater than K.

 **Examples:**

>  **Input :** test_list = [“Gfg”, “is”, “best”, “for”, “geeks”], K = 3
>
>  **Output :** [‘Gfg’, ‘is’, ‘BEST’, ‘for’, ‘GEEKS’]
>
>  **Explanation :** Best has 4 chars, hence BEST is uppercased.
>
>  
>
>
>  
>
>
>  **Input :** test_list = [“Gfg”, “is”, “best”, “for”, “geeks”], K = 4
>
>  **Output :** [‘Gfg’, ‘is’, ‘best’, ‘for’, ‘GEEKS’]
>
>  **Explanation :** geeks has 5 chars [greater than 4], hence GEEKS is
> uppercased.

 **Method #1 : Using** **upper()** **+** **loop**

In this, we perform task of uppercasing using upper(), and conditional
statements for greater is checked using loop.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Conditional Uppercase by size

# Using upper() + loop

 

# initializing list

test_list = ["Gfg", "is", "best", "for", "geeks"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 3

 

res = []

for ele in test_list:

 

 # check for size

 if len(ele) > K:

 res.append(ele.upper())

 else:

 res.append(ele)

 

# printing result

print("Modified Strings : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : ['Gfg', 'is', 'best', 'for', 'geeks']
    Modified Strings : ['Gfg', 'is', 'BEST', 'for', 'GEEKS']

 **Method #2 : Using** **list comprehension**

In this, task of iteration is performed inside list comprehension to act as
shorthand to similar method as above.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Conditional Uppercase by size

# Using list comprehension

 

# initializing list

test_list = ["Gfg", "is", "best", "for", "geeks"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 3

 

# list comprehension for one liner solution

res = [ele.upper() if len(ele) > K else ele for ele in
test_list]

 

# printing result

print("Modified Strings : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : ['Gfg', 'is', 'best', 'for', 'geeks']
    Modified Strings : ['Gfg', 'is', 'BEST', 'for', 'GEEKS']

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

