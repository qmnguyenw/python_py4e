Python program to Replace all Characters of a List Except the given character



Given a List. The task is to replace all the characters of the list with N
except the given character.

>  **Input** : test_list = [‘G’, ‘F’, ‘G’, ‘I’, ‘S’, ‘B’, ‘E’, ‘S’, ‘T’],
> repl_chr = ‘*’, ret_chr = ‘G’  
> **Output** : [‘G’, ‘*’, ‘G’, ‘*’, ‘*’, ‘*’, ‘*’, ‘*’, ‘*’]  
> **Explanation** : All characters except G replaced by *
>
>  **Input** : test_list = [‘G’, ‘F’, ‘G’, ‘B’, ‘E’, ‘S’, ‘T’], repl_chr =
> ‘*’, ret_chr = ‘G’  
> **Output** : [‘G’, ‘*’, ‘G’, ‘*’, ‘*’, ‘*’, ‘*’]  
> **Explanation** : All characters except G replaced by *

**Method #1 : Using list comprehension + conditional expressions**

In this, we perform the task of iteration using list comprehension, and
replacements are taken care of using conditional operators.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace all Characters Except K

# Using list comprehension and conditional expressions

 

# initializing lists

test_list = ['G', 'F', 'G', 'I', 'S', 'B',
'E', 'S', 'T']

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing repl_chr

repl_chr = '$'

 

# initializing retain chararter

ret_chr = 'G'

 

# list comprehension to remake list after replacement

res = [ele if ele == ret_chr else repl_chr for ele
in test_list]

 

# printing result

print("List after replacement : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : ['G', 'F', 'G', 'I', 'S', 'B', 'E', 'S', 'T']
    List after replacement : ['G', '$', 'G', '$', '$', '$', '$', '$', '$']
    

**Method #2 : Using map() + lambda**

In this, we use map() and lambda function to extend the logic to each element
of the list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace all Characters Except K

# Using map() + lambda

 

# initializing lists

test_list = ['G', 'F', 'G', 'I', 'S', 'B',
'E', 'S', 'T']

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing repl_chr

repl_chr = '$'

 

# initializing retain chararter

ret_chr = 'G'

 

# using map() to extend logic to each element of list

res = list(map(lambda ele: ret_chr if ele == ret_chr
else repl_chr, test_list))

 

# printing result

print("List after replacement : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : ['G', 'F', 'G', 'I', 'S', 'B', 'E', 'S', 'T']
    List after replacement : ['G', '$', 'G', '$', '$', '$', '$', '$', '$']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

