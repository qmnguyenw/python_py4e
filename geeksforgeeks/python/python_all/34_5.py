Python program to Extract Mesh matching Strings



Given a character mesh, containing missing characters, match the string which
matches the mesh.

 **Example:**

>  **Input** : test_list = [“geeks”, “best”, “peeks”], mesh = “_ee_s”  
> **Output** : [‘geeks’, ‘peeks’]  
> **Explanation** : Elements according to mesh are geeks and peeks.
>
>  **Input** : test_list = [“geeks”, “best”, “test”], mesh = “_e_t”  
> **Output** : [‘best’, ‘test’]  
> **Explanation** : Elements according to mesh are best and test.  
>

**Method #1 : Using loop + all() + len() + zip()**

  

  

The combination of the above can be used to solve this problem. In this, we
perform the task of matching mesh and each string using zip() and all() is
used to check for all strings, len() is used to test for correct string length
matching mesh.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Mesh matching Strings

# Using len() + loop + zip() + all()

 

# initializing list

test_list = ["geeks", "best", "peeks", "for",
"seeks"]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing mesh 

mesh = "_ee_s"

 

res = []

for sub in test_list:

 

 # testing for matching mesh, checking each character and length

 if (len(sub) == len(mesh)) and all((ele1 ==
"_") or (ele1 == ele2)

 for ele1, ele2 in zip(mesh, sub)):

 res.append(sub)

 

# printing result 

print("The extracted strings : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : ['geeks', 'best', 'peeks', 'for', 'seeks']
    The extracted strings : ['geeks', 'peeks', 'seeks']
    
    

**Method #2 : Using list comprehension**

This solves the problem in a similar way as the above method, the only
difference here is that 1 liner solution is provided.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Mesh matching Strings

# Using list comprehension

 

# initializing list

test_list = ["geeks", "best", "peeks", "for",
"seeks"]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing mesh 

mesh = "_ee_s"

 

# one liner to solve this problem

res = [sub for sub in test_list if (len(sub) ==
len(mesh)) and all((ele1 == "_") or (ele1 == ele2)

 for ele1, ele2 in zip(mesh, sub))]

 

# printing result 

print("The extracted strings : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : ['geeks', 'best', 'peeks', 'for', 'seeks']
    The extracted strings : ['geeks', 'peeks', 'seeks']
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

