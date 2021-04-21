Python – Render Initials as Dictionary Key



Given List of Strings, convert to dictionary with Key as initial value of
values. Won’t work in cases having words with similar initials.

> **Input** : test_list = [“geeksforgeeks”, “is”, “best”]  
> **Output** : {‘g’: ‘geeksforgeeks’, ‘i’: ‘is’, ‘b’: ‘best’}  
> **Explanation** : Keys constructed from initial character.  
>  **Input** : test_list = [“geeksforgeeks”, “best”]  
> **Output** : {‘g’: ‘geeksforgeeks’, ‘b’: ‘best’}  
> **Explanation** : Keys constructed from initial character.

**Method #1 : Using loop**

In this, we create each dictionary by getting initial element using string
element access and render value as list element.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Render Initials as Dictionary Key

# Using loop

 

# initializing list

test_list = ["geeksforgeeks", "is", "best"]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = dict()

for ele in test_list:

 

 # assigning initials as key

 res[ele[0]] = ele

 

# printing result 

print("Constructed Dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output**

  

  

    
    
    The original list is : ['geeksforgeeks', 'is', 'best']
    Constructed Dictionary : {'g': 'geeksforgeeks', 'i': 'is', 'b': 'best'}
    
    

