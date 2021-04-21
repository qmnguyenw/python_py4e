Python – Incremental Size Chunks from Strings



Given a String, split it into incremental sizes consecutive list.

>  **Input** : test_str = ‘geekforgeeks is best’  
>  **Output** : [‘g’, ‘ee’, ‘kfo’, ‘rgee’, ‘ks is’, ‘ best’]  
>  **Explanation** : Characters size increasing in list.
>
>  **Input** : test_str = ‘geekforgeeks’  
>  **Output** : [‘g’, ‘ee’, ‘kfo’, ‘rgee’, ‘ks’]  
>  **Explanation** : Characters size increasing in list.

 **Method #1 : Using loop + slicing**

In this, we perform task of getting chunks using string slicing and keep on
increasing chunk size during iteration.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Incremental Size Chunks from Strings

# Using loop + slicing

 

# initializing string

test_str = 'geekforgeeks is best for geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

res = []

idx = 1

while True:

 if len(test_str) > idx:

 

 # chunking

 res.append(test_str[0 : idx])

 test_str = test_str[idx:]

 idx += 1

 else:

 res.append(test_str)

 break

 

# printing result 

print("The Incremental sized Chunks : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geekforgeeks is best for geeks
    The Incremental sized Chunks : ['g', 'ee', 'kfo', 'rgee', 'ks is', ' best ', 'for gee', 'ks']
    

**Method #2 : Using generator + slicing**

In this, we perform slicing as in above method, difference is that chunks are
rendered using generator expression, each chunk yields at runtime in loop.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Incremental Size Chunks from Strings

# Using generator + slicing 

 

# generator function 

def gen_fnc(test_str):

 strt = 0

 stp = 1

 while test_str[strt : strt + stp]:

 

 # return chunks runtime while looping

 yield test_str[strt : strt + stp]

 strt += stp

 stp += 1

 

# initializing string

test_str = 'geekforgeeks is best for geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# calling fnc.

res = list(gen_fnc(test_str))

 

# printing result 

print("The Incremental sized Chunks : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geekforgeeks is best for geeks
    The Incremental sized Chunks : ['g', 'ee', 'kfo', 'rgee', 'ks is', ' best ', 'for gee', 'ks']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

