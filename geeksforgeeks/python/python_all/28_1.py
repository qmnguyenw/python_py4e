Python – Extract Monodigit elements



Given List of numbers, extract all numbers with only similar digit.

>  **Input** : test_list = [463, 888, 123, ‘aaa’, 112, 111, ‘gfg’, 939, 4,
> ‘ccc’]  
> **Output** : [888, ‘aaa’, 111, 4, ‘ccc’]  
> **Explanation** : All elements having single unique digit or character.
>
>  **Input** : test_list = [463, “GFG”, 8838, 43, 991]  
> **Output** : []  
> **Explanation** : No element found to be having only single digit.

**Method #1 : Using list comprehension + all()**

In this, we iterate all the elements using list comprehension, _all()_ is used
to check equality of all digits with first digit.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Monodigit elements

# Using list comprehension + all()

 

# initializing list

test_list = [463, 888, 123, "aaa", 112, 111,
"gfg", 939, 4, "ccc"]

 

# printing original lists

print("The original list is : " + str(test_list))

 

# all() checks for all similar digits

res = [sub for sub in test_list if all(

 str(ele) == str(sub)[0] for ele in str(sub))]

 

# printing result

print("Extracted Numbers : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [463, 888, 123, ‘aaa’, 112, 111, ‘gfg’, 939, 4,
> ‘ccc’]  
> Extracted Numbers : [888, ‘aaa’, 111, 4, ‘ccc’]

 **Method #2 : Using filter() + lambda + all()**

In this, we perform task of filtering using _lambda_ function, _filter()_ ,
and _all()_ is again used to check equality of all digits.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Monodigit elements

# Using filter() + lambda + all()

 

# initializing list

test_list = [463, 888, 123, "aaa", 112, 111,
"gfg", 939, 4, "ccc"]

 

# printing original lists

print("The original list is : " + str(test_list))

 

# all() checks for all similar digits

# filter() used for filtering

res = list(filter(lambda sub: all(str(ele) ==
str(

 sub)[0] for ele in str(sub)), test_list))

 

# printing result

print("Extracted Numbers : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [463, 888, 123, ‘aaa’, 112, 111, ‘gfg’, 939, 4,
> ‘ccc’]  
> Extracted Numbers : [888, ‘aaa’, 111, 4, ‘ccc’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

