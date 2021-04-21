Python – Every Kth Strings Uppercase



Given a String list, change every Kth string to uppercase.

>  **Input** : test_list = [“gfg”, “is”, “best”, “for”, “geeks”], K = 3  
>  **Output** : [‘GFG’, ‘is’, ‘best’, ‘FOR’, ‘geeks’]  
>  **Explanation** : All Kth strings are uppercased.
>
>  **Input** : test_list = [“gfg”, “is”, “best”, “for”, “geeks”], K = 4  
>  **Output** : [‘GFG’, ‘is’, ‘best’, ‘for’, ‘GEEKS’]  
>  **Explanation** : All Kth strings are uppercased.

 **Method #1 : Using loop + upper()**

In this, we iterate for all strings using loop and upper is used to perform
uppercase, Kth index is detected using modulo operator.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Every Kth Strings Uppercase

# Using loop + upper()

 

# initializing list

test_list = ["gfg", "is", "best", "for", "geeks",
"and", "CS"] 

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 3

 

res = []

for idx in range(len(test_list)):

 

 # checking for Kth index

 if idx % K == 0:

 res.append(test_list[idx].upper())

 else :

 res.append(test_list[idx])

 

# printing result 

print("The resultant String list : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['gfg', 'is', 'best', 'for', 'geeks', 'and', 'CS']
    The resultant String list : ['GFG', 'is', 'best', 'FOR', 'geeks', 'and', 'CS']
    

**Method #2 : Using list comprehension**

This yet another way in which this task can be performed. In this we use list
comprehension as shorthand, performs tasks similar to above method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Every Kth Strings Uppercase

# Using list comprehension

 

# initializing list

test_list = ["gfg", "is", "best", "for", "geeks",
"and", "CS"] 

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 3

 

# shorthand to perform this task

res = [test_list[idx].upper() if idx % K == 0 else
test_list[idx]

 for idx in range(len(test_list))]

 

# printing result 

print("The resultant String list : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['gfg', 'is', 'best', 'for', 'geeks', 'and', 'CS']
    The resultant String list : ['GFG', 'is', 'best', 'FOR', 'geeks', 'and', 'CS']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

