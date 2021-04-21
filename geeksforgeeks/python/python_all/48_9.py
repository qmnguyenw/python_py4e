Python – Dictionary items in value range



Given a range of values, extract all the items whose keys lie in range of
values.

>  **Input** : {‘Gfg’ : 6, ‘is’ : 7, ‘best’ : 9, ‘for’ : 8, ‘geeks’ : 11}, i,
> j = 9, 12  
>  **Output** : {‘best’ : 9, ‘geeks’ : 11}  
>  **Explanation** : Keys within 9 and 11 range extracted.
>
>  **Input** : {‘Gfg’ : 6, ‘is’ : 7, ‘best’ : 9, ‘for’ : 8, ‘geeks’ : 11}, i,
> j = 14, 18  
>  **Output** : {}  
>  **Explanation** : No values in range.

 **Method #1 : Using loop**

This is brute way in which this task can be performed. In this, we run a loop
for all the keys with conditional checks for range of values.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Dictionary items in value range

# Using loop

 

# initializing dictionary

test_dict = {'Gfg' : 6, 'is' : 7, 'best' : 9,
'for' : 8, 'geeks' : 11} 

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing range 

i, j = 8, 12

 

# using loop to iterate through all keys

res = dict()

for key, val in test_dict.items():

 if int(val) >= i and int(val) <= j:

 res[key] = val

 

# printing result 

print("The extracted dictionary : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': 6, 'is': 7, 'best': 9, 'for': 8, 'geeks': 11}
    The extracted dictionary : {'best': 9, 'for': 8, 'geeks': 11}
    

**Method #2 : Using filter() + lambda + dictionary comprehension**

The combination of above functions can be used to solve this problem. In this,
we perform task of filtering using filter() and lambda is used for conditional
checks.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Dictionary items in value range

# Using filter() + lambda + dictionary comprehension 

 

# initializing dictionary

test_dict = {'Gfg' : 6, 'is' : 7, 'best' : 9,
'for' : 8, 'geeks' : 11} 

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing range 

i, j = 8, 12

 

# using dictionary comprehension to compile result in one 

res = {key: val for key, val in filter(lambda sub:
int(sub[1]) >= i and

 int(sub[1]) <= j, test_dict.items())}

 

# printing result 

print("The extracted dictionary : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': 6, 'is': 7, 'best': 9, 'for': 8, 'geeks': 11}
    The extracted dictionary : {'best': 9, 'for': 8, 'geeks': 11}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

