Python – Convert String List to Key-Value List dictionary



Given a string, convert it to key-value list dictionary, with key as 1st word
and rest words as value list.

>  **Input** : test_list = [“gfg is best for geeks”, “CS is best subject”]  
>  **Output** : {‘gfg’: [‘is’, ‘best’, ‘for’, ‘geeks’], ‘CS’: [‘is’, ‘best’,
> ‘subject’]}  
>  **Explanation** : 1st elements are paired with respective rest of words as
> list.
>
>  **Input** : test_list = [“gfg is best for geeks”]  
>  **Output** : {‘gfg’: [‘is’, ‘best’, ‘for’, ‘geeks’]}  
>  **Explanation** : 1st elements are paired with respective rest of words as
> list.

 **Method #1 : Using split() + loop**

In this, we iterate for each string, and then perform split of string using
split(), assign 1st element as key and pack other elements into list, using *
operator and create key-value list pair.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert String List to Key-Value List dictionary

# Using split() + loop

 

# initializing list

test_list = ["gfg is best for geeks", "I love gfg", "CS is best
subject"]

 

# printing string

print("The original list : " + str(test_list))

 

 

res = dict()

for sub in test_list:

 

 # split() for key 

 # packing value list

 key, *val = sub.split()

 res[key] = val

 

# printing results 

print("The key values List dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : ['gfg is best for geeks', 'I love gfg', 'CS is best subject']
    The key values List dictionary : {'gfg': ['is', 'best', 'for', 'geeks'], 'I': ['love', 'gfg'], 'CS': ['is', 'best', 'subject']}
    

**Method #2 : Using split() + dictionary comprehension**

This is similar way to solve this problem. In this, dictionary comprehension
is used to solve this problem.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert String List to Key-Value List dictionary

# Using split() + dictionary comprehension

 

# initializing list

test_list = ["gfg is best for geeks", "I love gfg", "CS is best
subject"]

 

# printing string

print("The original list : " + str(test_list))

 

# using dictionary comprehension to solve this problem

res = {sub[0] : sub[1:] for sub in (ele.split() for
ele in test_list)}

 

# printing results 

print("The key values List dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : ['gfg is best for geeks', 'I love gfg', 'CS is best subject']
    The key values List dictionary : {'gfg': ['is', 'best', 'for', 'geeks'], 'I': ['love', 'gfg'], 'CS': ['is', 'best', 'subject']}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

