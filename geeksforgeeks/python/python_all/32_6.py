Python – Remove Kth key from dictionary



Many times, while working with Python, we can have a situation in which we
require to remove the Kth key of the dictionary. This is useful for Python
version 3.8 +, where key ordering is similar to the insertion order. Let’s
discuss certain ways in which this task can be performed.

 **Examples:**

>  **Input** : test_dict = {“Gfg” : 20, “is” : 36, “best” : 100, “for” : 17,
> “geeks” : 1} , K = 4  
> **Output** : {‘Gfg’: 20, ‘is’: 36, ‘best’ : 100, ‘geeks’: 1}  
> **Explanation** : 4th index, for is removed.
>
>  **Input** : test_dict = {“Gfg” : 20, “is” : 36, “best” : 100, “for” : 17,
> “geeks” : 1} , K = 2  
> **Output** : {‘Gfg’: 20, ‘best’ : 100, ‘for’ : 17, ‘geeks’: 1}  
> **Explanation** : 2nd index, ‘is’ is removed.

**Method #1 : Using del + loop**

  

  

This is one of the ways in which this task can be performed. In this, we
iterate for the keys, along with the counter, when we get the key, we perform
its removal. This performs inplace removal.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove Kth key from dictionary

# Using loop

 

# initializing dictionary

test_dict = {"Gfg" : 20, "is" : 36, "best" :
100,

 "for" : 17, "geeks" : 1} 

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing size 

K = 3

 

cnt = 0

for key in test_dict:

 cnt += 1

 

 # delete key if counter is equal to K

 if cnt == K:

 del test_dict[key]

 break

 

# printing result 

print("Required dictionary after removal : " + str(test_dict))   
  
---  
  
__

__

**Output:**

> The original dictionary is : {‘Gfg’: 20, ‘is’: 36, ‘best’: 100, ‘for’: 17,
> ‘geeks’: 1}  
> Required dictionary after removal : {‘Gfg’: 20, ‘is’: 36, ‘for’: 17,
> ‘geeks’: 1}

 **Method #2 : Using keys() + dictionary comprehension**

This is yet another way in which this task can be performed. In this, we
recreate the dictionary without including the required key, by extracting key
to be removed using keys(), we include all keys except required into new
dictionary.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove Kth key from dictionary

# Using Remove Kth key from dictionary

 

# initializing dictionary

test_dict = {"Gfg" : 20, "is" : 36, "best" :
100,

 "for" : 17, "geeks" : 1} 

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing size 

K = 3

 

# dictionary comprehension remakes dictionary, 

# rather than removing

res = {key: val for key, val in test_dict.items() 

 if key != list(test_dict.keys())[K - 1]}

 

# printing result 

print("Required dictionary after removal : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original dictionary is : {‘Gfg’: 20, ‘is’: 36, ‘best’: 100, ‘for’: 17,
> ‘geeks’: 1}  
> Required dictionary after removal : {‘Gfg’: 20, ‘is’: 36, ‘for’: 17,
> ‘geeks’: 1}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

