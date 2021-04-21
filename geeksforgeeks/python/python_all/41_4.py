Python – Filter all uppercase characters Tuples from given list of tuples



Given a Tuple list, filter tuples which contains all uppercase characters.

>  **Input** : test_list = [(“GFG”, “IS”, “BEST”), (“GFg”, “AVERAGE”), (“GfG”,
> ), (“Gfg”, “CS”)]  
>  **Output** : [(‘GFG’, ‘IS’, ‘BEST’)]  
>  **Explanation** : Only 1 tuple has all uppercase Strings.
>
>  **Input** : test_list = [(“GFG”, “iS”, “BEST”), (“GFg”, “AVERAGE”), (“GfG”,
> ), (“Gfg”, “CS”)]  
>  **Output** : []  
>  **Explanation** : No has all uppercase Strings.

 **Method #1 : Using loop**

In this, we iterate for each tuple, and check if every string is uppercase, if
no, that tuple is omitted from new tuple.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter uppercase characters Tuples

# Using loop

 

# initializing list

test_list = [("GFG", "IS", "BEST"), ("GFg",
"AVERAGE"), ("GFG", ), ("Gfg", "CS")]

 

# printing original list

print("The original list is : " + str(test_list))

 

res_list = []

for sub in test_list:

 res = True

 for ele in sub:

 

 # checking for uppercase

 if not ele.isupper():

 res = False

 break

 if res:

 res_list.append(sub)

 

# printing results

print("Filtered Tuples : " + str(res_list))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [('GFG', 'IS', 'BEST'), ('GFg', 'AVERAGE'), ('GFG', ), ('Gfg', 'CS')]
    Filtered Tuples : [('GFG', 'IS', 'BEST'), ('GFG', )]
    

**Method #2 : Using list comprehension + all() + isupper()**

In this, we check for all strings uppercase using all(), and list
comprehension provides compact solution of problem. isupper() is used to check
for uppercase.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter uppercase characters Tuples

# Using list comprehension + all() + isupper()

 

# initializing list

test_list = [("GFG", "IS", "BEST"), ("GFg",
"AVERAGE"), ("GFG", ), ("Gfg", "CS")]

 

# printing original list

print("The original list is : " + str(test_list))

 

# all() returns true only when all strings are uppercase

res = [sub for sub in test_list if all(ele.isupper() for
ele in sub)]

 

# printing results

print("Filtered Tuples : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [('GFG', 'IS', 'BEST'), ('GFg', 'AVERAGE'), ('GFG', ), ('Gfg', 'CS')]
    Filtered Tuples : [('GFG', 'IS', 'BEST'), ('GFG', )]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

