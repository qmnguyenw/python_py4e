Python – Remove rows with Numbers



Given a Matrix, remove rows with integer instance.

>  **Input** : test_list = [[4, ‘Gfg’, ‘best’], [‘gfg’, 5, ‘is’, ‘best’], [3,
> 5], [‘GFG’, ‘Best’]]  
> **Output** : [[‘GFG’, ‘Best’]]  
> **Explanation** : All rows with numbers are removed.
>
>  **Input** : test_list = [[4, ‘Gfg’, ‘best’], [‘gfg’, 5, ‘is’, ‘best’], [3,
> 5], [‘GFG’, ‘Best’, 1]]  
> **Output** : []  
> **Explanation** : All rows with numbers are removed. No list left.

**Method #1 : Using any() + list comprehension**

In this, we check for any integer element using _any()_ in any row, and use
list comprehension to perform task of iteration.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove rows with Numbers

# Using list comprehension + any

 

# initializing lists

test_list = [[4, 'Gfg', 'best'], [

 'gfg', 'is', 'best'], [3, 5], ['GFG', 'Best']]

 

# printing original lists

print("The original list is : " + str(test_list))

 

# using isinstance to check for integer and not include them

res = [sub for sub in test_list if not any(

 isinstance(ele, int) for ele in sub)]

 

# printing result

print("The filtered rows : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[4, ‘Gfg’, ‘best’], [‘gfg’, ‘is’, ‘best’], [3, 5],
> [‘GFG’, ‘Best’]]  
> The filtered rows : [[‘gfg’, ‘is’, ‘best’], [‘GFG’, ‘Best’]]

 **Method #2 : Using filter() + lambda + any()**

In this, we perform task of filtering using _lambda_ and _filter()_ , _any()_
is used in similar way as in above method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove rows with Numbers

# Using filter() + lambda + any()

 

# initializing lists

test_list = [[4, 'Gfg', 'best'], [

 'gfg', 'is', 'best'], [3, 5], ['GFG', 'Best']]

 

# printing original lists

print("The original list is : " + str(test_list))

 

# using isinstance to check for integer and not include them

# filter() used to filter with lambda fnc.

res = list(filter(lambda sub: not any(isinstance(ele,
int)

 for ele in sub), test_list))

 

# printing result

print("The filtered rows : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[4, ‘Gfg’, ‘best’], [‘gfg’, ‘is’, ‘best’], [3, 5],
> [‘GFG’, ‘Best’]]  
> The filtered rows : [[‘gfg’, ‘is’, ‘best’], [‘GFG’, ‘Best’]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

