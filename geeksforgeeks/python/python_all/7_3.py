Python Program to Construct dictionary using random values



Given List, our task is to write a Python program to construct dictionary with
values randomly selected from range.

 **Examples:**

    
    
     **Input :** test_list = ["Gfg", "is", "Best"], i, j = 2, 9
    **Output :** {'Gfg': 3, 'is': 9, 'Best': 4}
    **Explanation :** Random values assigned between 2 and 9.
    
    **Input :** test_list = ["Gfg", "is", "Best"], i, j = 2, 10
    **Output :** {'Gfg': 3, 'is': 9, 'Best': 10}
    **Explanation :** Random values assigned between 2 and 10.

 **Method #1 : Using** **randint()** **+** **loop**

In this, we iterate through each element in list and assign random number
selected using randint() to construct key value pair dictionary.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Construct dictionary using random values

# Using randint() + loop

from random import randint

 

# initializing list

test_list = ["Gfg", "is", "Best"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing range

i, j = 2, 9

 

res = dict()

for ele in test_list:

 

 # assiging random elements

 res[ele] = randint(i, j)

 

# printing result

print("Random range initialized dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output:**

  

  

> The original list is : [‘Gfg’, ‘is’, ‘Best’]
>
> Random range initialized dictionary : {‘Gfg’: 5, ‘is’: 7, ‘Best’: 8}

 **Method #2 : Using** **dictionary comprehension** **+** **randint()**

In this, we perform task in similar manner as above method, only difference
being dictionary comprehension is used to assign dictionary in shorthand
manner.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Construct dictionary using random values

# Using randint() + loop

from random import randint

 

# initializing list

test_list = ["Gfg", "is", "Best"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing range

i, j = 2, 9

 

# assiging random elements

# dictionary comprehension used as shorthand

res = {ele : randint(i, j) for ele in test_list}

 

# printing result

print("Random range initialized dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘Gfg’, ‘is’, ‘Best’]
>
> Random range initialized dictionary : {‘Gfg’: 4, ‘is’: 2, ‘Best’: 6}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

