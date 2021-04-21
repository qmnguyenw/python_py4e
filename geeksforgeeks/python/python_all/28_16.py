Python – Extract Similar Key Values



Given a dictionary, extract all values which are from similar keys, i.e
contains all similar characters, just jumbled to form each other.

>  **Input** : test_dict = {‘gfg’ : 5, ‘ggf’ : 19, ‘gffg’ : 9, ‘gff’ : 3,
> ‘fgg’ : 3}, tst_wrd = ‘fgg’  
> **Output** : [5, 19, 3]  
> **Explanation** : gfg, ggf and fgg have values, 5, 19 and 3.
>
>  **Input** : test_dict = {‘gfg’ : 5, ‘gffg’ : 9, ‘gff’ : 3, ‘fgg’ : 3},
> tst_wrd = ‘fgg’  
> **Output** : [5, 3]  
> **Explanation** : gfg and fgg have values, 5 and 3.

**Method #1 : Using sorted() + loop**

In this, we compare the key after sorting with target key, will have similar
elements in correct order, and can be checked for equality. Once with match,
their values are extracted.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Similar Key Values

# Using loop + sorted()

 

# initializing dictionary

test_dict = {'gfg': 5, 'ggf': 19, 'gffg': 9,
'gff': 3, 'fgg': 3}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing word

tst_wrd = 'fgg'

 

res = []

for key, val in test_dict.items():

 

 # sorted to get similar key order

 if ''.join(list(sorted(key))) == tst_wrd:

 res.append(val)

 

# printing result

print("The extracted keys : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original dictionary is : {‘gfg’: 5, ‘ggf’: 19, ‘gffg’: 9, ‘gff’: 3,
> ‘fgg’: 3}  
> The extracted keys : [5, 19, 3]

 **Method #2 : Using list comprehension + sorted()**

In this, we perform similar task as above, just perform using shorthand using
_sorted()_ and list comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Similar Key Values

# Using list comprehension + sorted()

 

# initializing dictionary

test_dict = {'gfg': 5, 'ggf': 19, 'gffg': 9,
'gff': 3, 'fgg': 3}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing word

tst_wrd = 'fgg'

 

# one-liner to solve this

res = [val for key, val in test_dict.items(

) if ''.join(list(sorted(key))) == tst_wrd]

 

# printing result

print("The extracted keys : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original dictionary is : {‘gfg’: 5, ‘ggf’: 19, ‘gffg’: 9, ‘gff’: 3,
> ‘fgg’: 3}  
> The extracted keys : [5, 19, 3]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

