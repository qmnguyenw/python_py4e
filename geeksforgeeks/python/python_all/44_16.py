Python – Extract ith element of K key’s value



Given a dictonary, extract ith element of K key’s value list.

>  **Input** : test_dict = {‘Gfg’ : [6, 7, 3, 1], ‘is’ : [9, 1, 4], ‘best’ :
> [10, 7, 4]}, K = ‘Gfg’, i = 1  
>  **Output** : 7  
>  **Explanation** : 1st index of ‘Gfg”s value is 7.
>
>  **Input** : test_dict = {‘Gfg’ : [6, 7, 3, 1], ‘is’ : [9, 1, 4], ‘best’ :
> [10, 7, 4]}, K = ‘best’, i = 0  
>  **Output** : 10  
>  **Explanation** : 0th index of ‘best”s value is 10.

 **Method : Using + get()**

This is one of the ways in which this task can be performed. In this, we
extract the key’s value using get() and then value is extracted after checking
for K being less than list length.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract ith element of K key's value

# Using get()

 

# initializing dictionary

test_dict = {'Gfg' : [6, 7, 3, 1], 

 'is' : [9, 1, 4],

 'best' : [10, 7, 4]} 

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing K 

K = 'Gfg'

 

# initializing i 

i = 2

 

# using get() to get the required value 

temp = test_dict.get(K)

res = None

# checking for non empty dict and length constraints

if temp and len(temp) >= i: 

 res = temp[i] 

 

# printing result 

print("The extracted value : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': [6, 7, 3, 1], 'is': [9, 1, 4], 'best': [10, 7, 4]}
    The extracted value : 3
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

