Python – Number of positions where Substrings Match of Length K



Given 2 Strings, count positions where substrings of Length K Match.

>  **Input** : test_str1 = ‘geeksforgeeks’, test_str2 = ‘peeksformeeks’, K = 4  
>  **Output** : 4  
>  **Explanation** : 4 positions match K length Substings.
>
>  **Input** : test_str1 = ‘geeksforgeeks’, test_str2 = ‘peeksformeeks’, K = 5  
>  **Output** : 3  
>  **Explanation** : 3 positions match K length Substings.

 **Method #1 : Using list comprehension + min() + slicing**

In this, we iterate through strings till length of minimum string, and the
comparison is done by slicing using string slicing. Iteration is done through
loop inside list comprehension.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Number of positions where Substrings Match of Length K

# Using list comprehension + min() + slicing

 

# initializing strings

test_str1 = 'geeksforgeeks'

test_str2 = 'peeksformeeks'

 

# printing original strings

print("The original string 1 is : " + str(test_str1))

print("The original string 2 is : " + str(test_str2))

 

# initializing K 

K = 3

 

# checking for substrings, 

# using len() to get total count

res = len([test_str1[idx : idx + K] for idx in
range(min(len(test_str1), len(test_str2)) - K - 1)

 if test_str1[idx : idx + K] == test_str2[idx : idx + K]])

 

# printing result 

print("Number of positions of matching K length Substrings : " +
str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string 1 is : geeksforgeeks
    The original string 2 is : peeksformeeks
    Number of positions of matching K length Substrings : 5
    
    

**Method #2 : Using map() + list comprehension**

In this, we extract all K length substrings of one string and then using in
operator and map, check for each substring if present in other String, this
ignores the positional factor of problem.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Number of positions where Substrings Match of Length K

# Using map() + list comprehension

 

# initializing strings

test_str1 = 'geeksforgeeks'

test_str2 = 'peeksformeeks'

 

# printing original strings

print("The original string 1 is : " + str(test_str1))

print("The original string 2 is : " + str(test_str2))

 

# initializing K 

K = 3

 

# Extracting Substrings

subs_str = [test_str1[idx : idx + K] for idx in
range(len(test_str1) - K - 1)]

 

# checking in other string

# using count() to get number

res = list(map(lambda ele: ele in test_str2,
subs_str)).count(True)

 

# printing result 

print("Number of positions of matching K length Substrings : " +
str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string 1 is : geeksforgeeks
    The original string 2 is : peeksformeeks
    Number of positions of matching K length Substrings : 5
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

