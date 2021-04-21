Python – Similar characters Strings comparison



Given two Strings, separated by delim, check if both contain same characters.

>  **Input** : test_str1 = ‘e!e!k!s!g’, test_str2 = ‘g!e!e!k!s’, delim = ‘!’  
>  **Output** : True  
>  **Explanation** : Same characters, just diff. positions.
>
>  **Input** : test_str1 = ‘e!e!k!s’, test_str2 = ‘g!e!e!k!s’, delim = ‘!’  
>  **Output** : False  
>  **Explanation** : g missing in 1st String.

 **Method #1 : Using sorted() + split()**

In this, we perform split using split(), and then perform task of sorting to
get strings in order, post that strings are compared using the comparison
operator.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Similar characters Strings comparison

# Using split() + sorted()

 

# initializing strings

test_str1 = 'e:e:k:s:g'

test_str2 = 'g:e:e:k:s'

 

# printing original strings

print("The original string 1 is : " + str(test_str1))

print("The original string 2 is : " + str(test_str2))

 

# initializing delim 

delim = ':'

 

# == operator is used for comparison

res = sorted(test_str1.split(':')) ==
sorted(test_str2.split(':'))

 

# printing result 

print("Are strings similar : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string 1 is : e:e:k:s:g
    The original string 2 is : g:e:e:k:s
    Are strings similar : True
    
    

**Method #2 : Using set() + split()**

In this, instead of sort(), we convert strings to set(), to get ordering. This
works only on unique character strings.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Similar characters Strings comparison

# Using set() + split()

 

# initializing strings

test_str1 = 'e:k:s:g'

test_str2 = 'g:e:k:s'

 

# printing original strings

print("The original string 1 is : " + str(test_str1))

print("The original string 2 is : " + str(test_str2))

 

# initializing delim 

delim = ':'

 

# == operator is used for comparison

# removes duplicates and compares

res = set(test_str1.split(':')) ==
set(test_str2.split(':'))

 

# printing result 

print("Are strings similar : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string 1 is : e:k:s:g
    The original string 2 is : g:e:k:s
    Are strings similar : True
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

