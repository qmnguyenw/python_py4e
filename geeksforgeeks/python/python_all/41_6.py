Python – Replace to K at ith Index in String



Given a String, replace ith index by K value.

>  **Input** : test_str = ‘geeks5geeks’, K = ‘7’, i = 5  
>  **Output** : ‘geeks7geeks’  
>  **Explanation** : Element is 5, converted to 7 on ith index.
>
>  **Input** : test_str = ‘geeks5geeks’, K = ‘7’, i = 6  
>  **Output** : ‘geeks56eeks’  
>  **Explanation** : Element is g, converted to 7 on ith index.

 **Method #1 : Using string slicing**

In this, we perform the slicing of pre string, till i, and then add K, then
add post values, using string slice method.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace to K at ith Index in String

# using string slicing

 

# initializing strings

test_str = 'geeks5geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing K

K = '4'

 

# initializing i

i = 5

 

# the replaced result 

res = test_str[: i] + K + test_str[i + 1:]

 

# printing result 

print("The constructed string : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeks5geeks
    The constructed string : geeks4geeks
    
    

**Method #2 : Using join() + generator expression**

In this, we perform the task of checking for ith index and conditionally
appending K, using generator expression and convert the result into string
using join().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace to K at ith Index in String

# using join() + generator expression

 

# initializing strings

test_str = 'geeks5geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing K

K = '4'

 

# initializing i

i = 5

 

# the replaced result 

res = ''.join(test_str[idx] if idx != i else K for idx
in range(len(test_str)))

 

# printing result 

print("The constructed string : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeks5geeks
    The constructed string : geeks4geeks
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

