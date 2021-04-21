Python program to Uppercase selective indices



Given a String perform uppercase to particular indices.

>  **Input** : test_str = ‘geeksgeeksisbestforgeeks’, idx_list = [5, 7, 3, 2,
> 6, 9]  
> **Output** : geEKsGEEkSisbestforgeeks  
> **Explanation** : Particular indices are uppercased.
>
>  **Input** : test_str = ‘geeksgeeksisbestforgeeks’, idx_list = [5, 7, 3]  
> **Output** : geeKsGeEksisbestforgeeks  
> **Explanation** : Particular indices are uppercased.  
>

**Method #1 : Using loop +** **upper()**

In this, we perform task of converting to uppercase using upper(), and convert
to uppercase checking indices from list.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Uppercase selective indices

# Using loop + upper()

 

# initializing string

test_str = 'geeksgeeksisbestforgeeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing indices list 

idx_list = [5, 7, 3, 2, 6, 9]

 

res = ''

for idx in range(0, len(test_str)):

 

 # checking for index list for uppercase 

 if idx in idx_list:

 res += test_str[idx].upper()

 else:

 res += test_str[idx]

 

# printing result 

print("Transformed String : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeksgeeksisbestforgeeks
    Transformed String : geEKsGEEkSisbestforgeeks
    

**Method #2 : Using** **list comprehension** **+** **upper()** **+**
**join()**

Similar method as above, difference being list comprehension is used to offer
one liner, and join() is used to convert back to string.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Uppercase selective indices

# Using list comprehension + upper() + join()

 

# initializing string

test_str = 'geeksgeeksisbestforgeeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing indices list

idx_list = [5, 7, 3, 2, 6, 9]

 

# one-liner way to solve this problem

res = ''.join([test_str[idx].upper() if idx in idx_list else
test_str[idx]

 for idx in range(0, len(test_str))])

 

# printing result

print("Transformed String : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original string is : geeksgeeksisbestforgeeks
    Transformed String : geEKsGEEkSisbestforgeeks
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

