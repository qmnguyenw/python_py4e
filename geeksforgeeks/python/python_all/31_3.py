Python – Extract Strings with a digit



Given a Strings List, extract those with atleast one digit.

>  **Input** : test_list = [‘gf4g’, ‘is’, ‘best’, ‘gee1ks’]  
> **Output** : [‘gf4g’, ‘gee1ks’]  
> **Explanation** : 4, 1 are respective digits in string.
>
>  **Input** : test_list = [‘gf4g’, ‘is’, ‘best’, ‘geeks’]  
> **Output** : [‘gf4g’]  
> **Explanation** : 4 is digit in string.

**Method #1 : Using** **list comprehension** **+** **any()** **+**
**isdigit()**

In this iteration for each string is done using list comprehension, any() and
isdigit() is used for task of checking at least one digit.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Strings with a digit

# Using list comprehension + any() + isdigit()

 

# initializing list

test_list = ['gf4g', 'is', 'best', '4', 'gee1ks']

 

# printing original list

print("The original list is : " + str(test_list))

 

# checking if string contain any string using any()

res = [sub for sub in test_list if any(ele for ele
in sub if ele.isdigit())]

 

# printing result

print("Strings with any digit : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘gf4g’, ‘is’, ‘best’, ‘4’, ‘gee1ks’]  
> Strings with any digit : [‘gf4g’, ‘4’, ‘gee1ks’]

 **Method #2 : Using any() +** **filter()** **\+ lamdba**

In this, we perform task of filtering using lambda and filter(), rest remains
the same.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Strings with a digit

# Using any() + filter() + lamdba

 

# initializing list

test_list = ['gf4g', 'is', 'best', '4', 'gee1ks']

 

# printing original list

print("The original list is : " + str(test_list))

 

# checking if string contain any string using any()

# filter() used to filter strings with digits

res = list(filter(lambda sub: any(

 ele for ele in sub if ele.isdigit()), test_list))

 

# printing result

print("Strings with any digit : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘gf4g’, ‘is’, ‘best’, ‘4’, ‘gee1ks’]  
> Strings with any digit : [‘gf4g’, ‘4’, ‘gee1ks’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

