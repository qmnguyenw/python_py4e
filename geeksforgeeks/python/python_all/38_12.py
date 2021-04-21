Python – Remove index ranges from String



Given a string and ranges list, remove all the characters that occur in
ranges.

> **Input** : test_str = ‘geeksforgeeks is best for geeks’, range_list = [(3,
> 6), (7, 10)]  
>  **Output** : geeks is best for geeks  
>  **Explanation** : The required ranges removed.
>
>  **Input** : test_str = ‘geeksforgeeks is best for geeks’, range_list = [(3,
> 6)]  
>  **Output** : georgeeks is best for geeks  
>  **Explanation** : The required ranges removed.

 **Method #1 : Using loop**

In this, we check for each range, remake string, considering the index doesn’t
lie in range checking using conditional statements.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove index ranges from String 

# Using loop

 

# initializing strings

test_str1 = 'geeksforgeeks is best for geeks'

 

# printing original string

print("The original string 1 is : " + str(test_str1))

 

# initializing ranges list 

range_list = [(3, 6), (7, 10), (14, 17)]

 

res = ""

 

for idx, chr in enumerate(test_str1):

 for strt_idx, end_idx in range_list:

 

 # checking for ranges and appending 

 if strt_idx <= idx + 1 <= end_idx: 

 break

 else:

 res += chr

 

# printing result 

print("The reconstructed string : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string 1 is : geeksforgeeks is best for geeks
    The reconstructed string : geeksbest for geeks
    

**Method #2 : Using any() + list comprehension + join()**

In this, we perform task of checking for indices for strings using any() and
list comprehension is used to reconstruct string accordingly.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove index ranges from String 

# Using any() + list comprehension + join()

 

# initializing strings

test_str1 = 'geeksforgeeks is best for geeks'

 

# printing original string

print("The original string 1 is : " + str(test_str1))

 

# initializing ranges list 

range_list = [(3, 6), (7, 10), (14, 17)]

 

# using any() to check for strings in index ranges

res = ''.join(chr for idx, chr in enumerate(test_str1,
1) if not any(strt_idx <= idx <= end_idx 

 for strt_idx, end_idx in range_list))

 

# printing result 

print("The reconstructed string : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string 1 is : geeksforgeeks is best for geeks
    The reconstructed string : geeksbest for geeks
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

