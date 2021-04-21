Python – Check if Elements delimited by K



Given a String, check if each segment is delimited by K.

>  **Input** : test_str = ’72!45!geeks!best’, K = ‘!’  
>  **Output** : True  
>  **Explanation** : All numerics and alphabets separated by delim border.
>
>  **Input** : test_str = ’72!45geeks!best’, K = ‘!’  
>  **Output** : False  
>  **Explanation** : No separation between 45 and geeks.

 **Method : Using isdigit() + isalpha() + loop**

This is way in which this task can be performed. In this, we perform task of
checking for alphabets and digits segments using isalpha() and isdigit().
Presence of any element, not entirely number or alphabet, is termed to non-
delimited by K, and it remains unresolved during split().

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if Elements delimited by K

# Using isdigit() + isalpha() + loop

 

# initializing string

test_str = '72@45@geeks@best'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing splt_chr 

K = "@"

 

res = True

 

# splitting elements

temp = test_str.split(K) 

 

for ele in temp:

 

 # checking for non-alpha or non-digit

 if len(ele) > 1 and not ele.isdigit() and not
ele.isalpha():

 res = False

 break

 

# printing result 

print("Are all delimited by K : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : 72@45@geeks@best
    Are all delimited by K : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

