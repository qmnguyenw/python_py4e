Python – Test if list is Palindrome



Given a List, check if its palindrome.

> **Input** : test_list = [4, 5, 4]  
> **Output** : True  
> **Explanation** : List is same from front and rear.
>
>  **Input** : test_list = [4, 5, 5]  
> **Output** : True  
> **Explanation** : List is not same from front and rear.

**Method #1: Using** **list slicing**

In this, we extract first and reversed 2nd half of list, and then compare for
equality, if found equal, then we conclude its palindrome.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if list is Palindrome

# Using list slicing

 

# initializing list

test_list = [1, 4, 5, 4, 1]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Reversing the list

reverse = test_list[::-1]

 

# checking if palindrome

res = test_list == reverse

 

# printing result 

print("Is list Palindrome : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [1, 4, 5, 4, 1]
    Is list Palindrome : True
    

**Method #2 : Using** **reversed()**

In this, we simply reverse the list and check if both original list and
reversed list is similar.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if list is Palindrome

# Using reversed()

 

# initializing list

test_list = [1, 4, 5, 4, 1]

 

# printing original list

print("The original list is : " + str(test_list))

 

# reversing list

rev_list = list(reversed(test_list))

 

# checking for Palindrome

res = rev_list == test_list

 

# printing result 

print("Is list Palindrome : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [1, 4, 5, 4, 1]
    Is list Palindrome : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

