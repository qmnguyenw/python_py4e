Python – Avoid Spaces in string length



Given a String, compute all the characters, except spaces.

>  **Input** : test_str = ‘geeksforgeeks 33 best’  
>  **Output** : 19  
>  **Explanation** : Total characters are 19.
>
>  **Input** : test_str = ‘geeksforgeeks best’  
>  **Output** : 17  
>  **Explanation** : Total characters are 17 except spaces.

 **Method #1 : Using isspace() + sum()**

In this, we check for each character to be equal not to space() using
isspace() and not operator, sum() is used to check frequency.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Avoid Spaces in Characters Frequency

# Using isspace() + sum()

 

# initializing string

test_str = 'geeksforgeeks 33 is best'

 

# printing original string

print("The original string is : " + str(test_str))

 

# isspace() checks for space 

# sum checks count 

res = sum(not chr.isspace() for chr in test_str)

 

# printing result 

print("The Characters Frequency avoiding spaces : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeksforgeeks 33 is   best
    The Characters Frequency avoiding spaces : 21
    
    

**Method #2 : Using sum() + len() + map() + split()**

In this, we perform split on spaces and extract words without spaces, then the
length() of is computed using len() extended to each word using map(), the
summation of all lengths computed using sum() is final result.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Avoid Spaces in Characters Frequency

# Using sum() + len() + map() + split()

 

# initializing string

test_str = 'geeksforgeeks 33 is best'

 

# printing original string

print("The original string is : " + str(test_str))

 

# len() finds individual word Frequency 

# sum() extracts final Frequency

res = sum(map(len, test_str.split()))

 

# printing result 

print("The Characters Frequency avoiding spaces : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeksforgeeks 33 is   best
    The Characters Frequency avoiding spaces : 21
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

