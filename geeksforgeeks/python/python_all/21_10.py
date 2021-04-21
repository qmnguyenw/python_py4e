Python – Remove strings with any non-required character



Given a Strings list, remove string, if it contains any unwanted character.

>  **Input** : test_list = [“gfg”, “is”, “best”, “for”, “geeks”], chr_list =
> [‘f’, ‘m’, ‘n’, ‘i’]  
> **Output** : [‘best’, ‘geeks’]  
> **Explanation** : Given Strings don’t contain f, m, n or i.
>
>  **Input** : test_list = [“gfg”, “is”, “best”, “for”, “geeks”], chr_list =
> [‘f’, ‘m’, ‘n’]  
> **Output** : [‘best’, ‘geeks’, ‘is’]  
> **Explanation** : Given Strings don’t contain f, m or n.

**Method #1 : Using** **list comprehension** **+** **any()**

In this, we test all strings and use any() to iterate all the non-required
characters list and check its presence in string, if found, that list is not
included in result list.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove strings with any non-required character

# Using list comprehension + any()

 

# initializing list

test_list = ["gfg", "is", "best", "for", "geeks"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# non-required char list

chr_list = ['f', 'm', 'n', 'i']

 

# checking for all strings

# removing if contains even 1 character

res = [sub for sub in test_list if not any(ele in sub
for ele in chr_list)]

 

# printing result

print("Filtered Strings : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['gfg', 'is', 'best', 'for', 'geeks']
    Filtered Strings : ['best', 'geeks']
    

**Method #2 : Using filter() + lambda + any()**

In this, we perform task of filtering using filter() and lambda function. Rest
any() is used to check for any character present in strings for its removal.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove strings with any non-required character

# Using filter() + lambda + any()

 

# initializing list

test_list = ["gfg", "is", "best", "for", "geeks"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# non-required char list

chr_list = ['f', 'm', 'n', 'i']

 

# checking for all strings

# filter and lambda used to do this task

res = list(filter(lambda sub: not any(

 ele in sub for ele in chr_list), test_list))

 

# printing result

print("Filtered Strings : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['gfg', 'is', 'best', 'for', 'geeks']
    Filtered Strings : ['best', 'geeks']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

