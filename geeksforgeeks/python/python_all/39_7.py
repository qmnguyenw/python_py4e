Python – Split Numeric String into K digit integers



Given a String, convert it to K digit integers

>  **Input** : test_str = ‘457336’, K = 2  
>  **Output** : [45, 73, 36]  
>  **Explanation** : Divided in 2 digit integers.
>
>  **Input** : test_str = ‘457336’, K = 3  
>  **Output** : [457, 336]  
>  **Explanation** : Divided in 3 digit integers.

 **Method #1 : Using int() + slice + loop**

In this, we iterate for string and perform slicing till K digits and then
perform task of conversion to integer using int().

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Split Numeric String into K digit integers

# Using int() + slice + loop

 

# initializing string

test_str = '457336842'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing substring

K = 3

 

res = []

for idx in range(0, len(test_str), K):

 

 # converting to int, after slicing

 res.append(int(test_str[idx : idx + K]))

 

# printing result 

print("Converted number list : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : 457336842
    Converted number list : [457, 336, 842]
    

**Method #2 : Using list comprehension + int() + slicing**

Similar method to above, just a shorthand to solve this problem.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Split Numeric String into K digit integers

# Using list comprehension + int() + slicing

 

# initializing string

test_str = '457336842'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing substring

K = 3

 

# one liner to solve problem

res = [int(test_str[idx : idx + K]) for idx in
range(0, len(test_str), K)]

 

# printing result 

print("Converted number list : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : 457336842
    Converted number list : [457, 336, 842]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

