Python – Split a String by Custom Lengths



Given a String, perform split of strings on the basis of custom lengths.

>  **Input** : test_str = ‘geeksforgeeks’, cus_lens = [4, 3, 2, 3, 1]  
> **Output** : [‘geek’, ‘sfo’, ‘rg’, ‘eek’, ‘s’]  
> **Explanation** : Strings separated by custom lengths.  
>  **Input** : test_str = ‘geeksforgeeks’, cus_lens = [10, 3]  
> **Output** : [‘geeksforge’, ‘eks’]  
> **Explanation** : Strings separated by custom lengths.  
>

**Method #1 : Using slicing + loop**

In this, we perform task of slicing to cater custom lengths and loop is used
to iterate for all the lengths.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Multilength String Split

# Using loop + slicing

 

# initializing string

test_str = 'geeksforgeeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing length list

cus_lens = [5, 3, 2, 3]

 

res = []

strt = 0

for size in cus_lens:

 

 # slicing for particular length

 res.append(test_str[strt : strt + size])

 strt += size

 

# printing result 

print("Strings after splitting : " + str(res))   
  
---  
  
__

__

**Output**

  

  

    
    
    The original string is : geeksforgeeks
    Strings after splitting : ['geeks', 'for', 'ge', 'eks']
    

