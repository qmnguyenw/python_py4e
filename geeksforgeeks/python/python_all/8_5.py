Python – Replace occurrences by K except first character



Given a String, the task is to write a Python program to replace occurrences
by K of character at 1st index, except at 1st index.

 **Examples:**

    
    
     **Input :** test_str = 'geeksforgeeksforgeeks', K = '@'
    **Output :** geeksfor@eeksfor@eeks
    
    **Explanation :** All occurrences of g are converted to @ except 0th index.
    
    **Input :** test_str = 'geeksforgeeks', K = '#'
    **Output :** geeksfor#eeks
    
    **Explanation :** All occurrences of g are converted to # except 0th index.

 **Method #1 : Using slicing + replace()**

In this, we perform task of replacing entire string from 2nd character with K
of the character occurring at 1st index. The result is prefix joined by first
character.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace occurrences by K except first character

# Using slicing + replace()

 

# initializing string

test_str = 'geeksforgeeksforgeeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing K

K = '$'

 

# replacing using replace()

res = test_str[0] + test_str[1:].replace(test_str[0], K)

 

# printing result

print("Replaced String : " + str(res))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    The original string is : geeksforgeeksforgeeks
    Replaced String : geeksfor$eeksfor$eeks

 **Method #2 : Using replace()**

In this, replace() is called twice for task of replacing all occurences, and
then just reverse replace the first occurrence.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace occurrences by K except first character

# Using replace()

 

# initializing string

test_str = 'geeksforgeeksforgeeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing K

K = '$'

 

# replacing using replace()

res = test_str.replace(test_str[0], K).replace(K, test_str[0],
1)

 

# printing result

print("Replaced String : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original string is : geeksforgeeksforgeeks
    Replaced String : geeksfor$eeksfor$eeks

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

