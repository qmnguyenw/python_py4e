Python – Concatenate Dynamic Frequency



Given List of elements, perform concatenation with frequency dynamically, i.e
each element concatenated with its frequency till its index.

>  **Input** : test_list = [‘z’, ‘z’, ‘e’, ‘f’, ‘f’]  
>  **Output** : [‘1z’, ‘2z’, ‘1e’, ‘1f’, ‘2f’]  
>  **Explanation** : As occurrence increase, concat number is increased.
>
>  **Input** : test_list = [‘g’, ‘f’, ‘g’]  
>  **Output** : [‘1g’, ‘1f’, ‘2g’]  
>  **Explanation** : As occurrence increase, concat number is increased.

 **Method : Using defaultdict() + “+” operator + str()**

In this, the dynamic frequency computation is done using defaultdict() and
str() is used to convert elements to string for valid concatenation using “+”
operator.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Concatenate Dynamic Frequency

# Using defaultdict() + "+" operator + str()

from collections import defaultdict

 

# initializing list

test_list = ['z', 'z', 'e', 'f', 'f', 'e',
'f', 'z', 'c']

 

# printing original list

print("The original list is : " + str(test_list))

 

memo = defaultdict(int)

res = []

for ele in test_list:

 memo[ele] += 1

 

 # adding Frequency with element

 res.append(str(memo[ele]) + str(ele))

 

# printing result 

print("Dynamic Frequency list : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['z', 'z', 'e', 'f', 'f', 'e', 'f', 'z', 'c']
    Dynamic Frequency list : ['1z', '2z', '1e', '1f', '2f', '2e', '3f', '3z', '1c']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

