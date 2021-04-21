Python – Filter Supersequence Strings



Given a Strings list and substring, the task is to write a Python program to
extract all the strings that has all the characters that can be used to make
substring.

 **Examples:**

>  **Input :** test_list = [“gfg”, “/”, “geeksforgeeks”, “best”, “for”,
> “geeks”], substr = “kgs”
>
>  **Output :** [“geeksforgeeks”, “geeks”]
>
>  **Explanation :** All kgs characters are present in both strings.
>
>  
>
>
>  
>
>
>  **Input :** test_list = [“gfg”, “/”, “geeksforgeeks”, “best”, “for”,
> “geeks”], substr = “kgf”
>
>  **Output** : [“geeksforgeeks”]
>
>  **Explanation :** All kgs characters are present in only geeksforgeeks
> string.

 **Method 1 : Using** **all()** **+** **list comprehension**

In this, we check for all the character presence in string using all(). The
iteration of strings is done using list comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter Supersequence Strings

# Using all() + list comprehension

 

# initializing list

test_list = ["gfg", "/", "geeksforgeeks", "best",
"for", "geeks"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing substr

substr = "kgs"

 

# all() checks for all characters in strings

res = [sub for sub in test_list if all(ele in sub
for ele in substr)]

 

# printing result

print("Filtered strings : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘gfg’, ‘/’, ‘geeksforgeeks’, ‘best’, ‘for’, ‘geeks’]
>
> Filtered strings : [‘geeksforgeeks’, ‘geeks’]
>
>  
>
>
>  
>

 **Method #2 : Using** **filter()** **\+ all()**

In this, we perform task of filtering using filter() and lambda function
rather than list comprehension and conditionals used in upper method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter Supersequence Strings

# Using filter() + all()

 

# initializing list

test_list = ["gfg", "/", "geeksforgeeks", "best",
"for", "geeks"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing substr

substr = "kgs"

 

# all() checks for all characters in strings

res = list(filter(lambda sub: all(ele in sub for
ele in substr), test_list))

 

# printing result

print("Filtered strings : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘gfg’, ‘/’, ‘geeksforgeeks’, ‘best’, ‘for’, ‘geeks’]
>
> Filtered strings : [‘geeksforgeeks’, ‘geeks’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

