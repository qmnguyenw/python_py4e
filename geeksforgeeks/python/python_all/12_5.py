Python program to find maximum uppercase run



Giving a String, write a Python program to find maximum run of uppercase
characters.

 **Examples:**

>  **Input** : test_str = ‘GeEKSForGEEksISBESt’  
> **Output** : 5  
> **Explanation** : ISBES is best run of uppercase.
>
>  **Input** : test_str = ‘GeEKSForGEEKSISBESt’  
> **Output** : 10  
> **Explanation** : GEEKSISBES is best run of uppercase.

**Method : Using** **isupper()** **\+ loop**

  

  

In this, we update maximum run when non-uppercase is encountered otherwise
counter is incremented if character is uppercase.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Maximum uppercase run

# Using isupper() + loop 

 

# initializing string

test_str = 'GeEKSForGEEksISBESt'

 

# printing original string

print("The original string is : " + str(test_str))

 

cnt = 0

res = 0

for idx in range(0, len(test_str)):

 

 # updating run count on uppercase

 if test_str[idx].isupper():

 cnt += 1

 

 # on lowercase, update the maxrun

 else :

 res = cnt 

 cnt = 0

if test_str[len(test_str) - 1].isupper(): 

 res = cnt

 

# printing result

print("Maximum Uppercase Run : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original string is : GeEKSForGEEksISBESt
    Maximum Uppercase Run : 5

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

