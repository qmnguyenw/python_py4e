Python – Strings with all given List characters



GIven Strings List and character list, extract all strings, having all
characters from character list.

>  **Input** : test_list = [“Geeks”, “Gfg”, “Geeksforgeeks”, “free”], chr_list
> = [ ‘f’, ‘r’, ‘e’]  
>  **Output** : [‘free’, “Geeksforgeeks”]  
>  **Explanation** : Only “free” and “Geeksforgeeks” contains all ‘f’, ‘r’ and
> ‘e’.
>
>  **Input** : test_list = [“Geeks”, “Gfg”, “Geeksforgeeks”, “free”], chr_list
> = [‘x’]  
>  **Output** : []  
>  **Explanation** : No word contains ‘x’.

 **Method #1 : Using loop**

In this, we iterate for all elements from list, and check if all are present
in particular string, if yes, then that string is appended to result.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Strings with all List characters

# Using loop

 

# initializing list

test_list = ["Geeks", "Gfg", "Geeksforgeeks", "free"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing char_list 

chr_list = ['g', 'f']

 

res_list = []

for sub in test_list:

 res = True

 for ele in chr_list:

 

 # check if any element is not present

 if ele not in sub:

 res = False

 break

 if res:

 res_list.append(sub)

 

# printing results

print("Filtered Strings : " + str(res_list))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['Geeks', 'Gfg', 'Geeksforgeeks', 'free']
    Filtered Strings : ['Gfg', 'Geeksforgeeks']
    

**Method #2 : Using all() + list comprehension**

In this, we check for all characters presence using all(), and if checks out,
String is appended into result. Iteration part done in list comprehension as
one-liner.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Strings with all List characters

# Using all() + list comprehension

 

# initializing list

test_list = ["Geeks", "Gfg", "Geeksforgeeks", "free"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing char_list 

chr_list = ['g', 'f']

 

# using all() to check containment of all characters

res_list = [sub for sub in test_list if all(ele in sub
for ele in chr_list)]

 

# printing results

print("Filtered Strings : " + str(res_list))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['Geeks', 'Gfg', 'Geeksforgeeks', 'free']
    Filtered Strings : ['Gfg', 'Geeksforgeeks']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

