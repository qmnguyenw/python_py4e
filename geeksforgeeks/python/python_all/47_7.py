Python – Remove Keys with K value



Given a dictionary, remove all keys with value equals K.

>  **Input** : test_dict = {‘Gfg’ : 8, ‘is’ : 7, ‘best’ : 8, ‘for’ : 6,
> ‘geeks’ : 11}, K = 8  
>  **Output** : {‘is’ : 7, ‘for’ : 6, ‘geeks’ : 11}  
>  **Explanation** : “Gfg” and “Best”, valued 8, are removed.
>
>  **Input** : test_dict = {‘Gfg’ : 8, ‘is’ : 8, ‘best’ : 8, ‘for’ : 8,
> ‘geeks’ : 8}, K = 8  
>  **Output** : {}  
>  **Explanation** : All keys, valued 8, are removed.

 **Method #1 : Using dictionary comprehension**

This is one of the ways in which this task can be performed. In this, we check
for only elements that are not equal to K and retain it, inside dictionary
comprehension as one-liner.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove Keys with K value

# Using dictionary comprehension

 

# initializing dictionary

test_dict = {'Gfg' : 6, 'is' : 7, 'best' : 9,
'for' : 6, 'geeks' : 11} 

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing K 

K = 6

 

# using dictionary comprehension 

# to compare not equal to K and retain 

res = {key: val for key, val in test_dict.items() if val
!= K}

 

# printing result 

print("The filtered dictionary : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': 6, 'is': 7, 'best': 9, 'for': 6, 'geeks': 11}
    The filtered dictionary : {'is': 7, 'best': 9, 'geeks': 11}
    

**Method #2 : Using dict() + filter() + lambda**

The combination of above functions can be used to solve this problem. In this,
we filter all the non-K elements and retain. Finally the result is converted
to dictionary using dict().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove Keys with K value

# Using dict() + filter() + lambda

 

# initializing dictionary

test_dict = {'Gfg' : 6, 'is' : 7, 'best' : 9,
'for' : 6, 'geeks' : 11} 

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing K 

K = 6

 

# employing lambda for computation 

# filter() to perform filter according to lambda

res = dict(filter(lambda key: key[1] != K,
test_dict.items()))

 

# printing result 

print("The filtered dictionary : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': 6, 'is': 7, 'best': 9, 'for': 6, 'geeks': 11}
    The filtered dictionary : {'is': 7, 'best': 9, 'geeks': 11}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

