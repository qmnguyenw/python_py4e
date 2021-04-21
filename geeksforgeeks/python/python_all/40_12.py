Python – Assign values to Values List



Given 2 dictionaries, assign values to value list elements mapping from
dictionary 2.

>  **Input** : test_dict = {‘Gfg’ : [3, 6], ‘best’ :[9]}, look_dict = {3 : [1,
> 5], 6 : “Best”, 9 : 12}  
>  **Output** : {‘Gfg’: {3: [1, 5], 6: ‘Best’}, ‘best’: {9: 12}}  
>  **Explanation** : 3 is replaced by key 3 and value [1, 5] and so on.
>
>  **Input** : test_dict = {‘Gfg’ : [3, 6]}, look_dict = {3 : [1, 5], 6 :
> “Best”}  
>  **Output** : {‘Gfg’: {3: [1, 5], 6: ‘Best’}}  
>  **Explanation** : 3 is replaced by key 3 and value [1, 5] and so on.

 **Method #1 : Using nested dictionary comprehension**

In this, we use inner dictionary comprehension to map values elements to dict
2, and outer dict is used to extract all keys from dictionary 1.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Assign values to Values List

# Using nested dictionary comprehension

 

# initializing dictionary

test_dict = {'Gfg' : [3, 6],

 'is' : [4, 2], 

 'best' :[9]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing lookup dict 

look_dict = {3 : [1, 5], 6 : "Best", 4 : 10,
9 : 12, 2 : "CS"}

 

# nested dictionaries to sought solution

res = {idx: {ikey: look_dict[ikey] for ikey in test_dict[idx]}
for idx in test_dict}

 

# printing result 

print("The mapped dictionary : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': [3, 6], 'is': [4, 2], 'best': [9]}
    The mapped dictionary : {'Gfg': {3: [1, 5], 6: 'Best'}, 'is': {4: 10, 2: 'CS'}, 'best': {9: 12}}
    

**Method #2 : Using items() + dictionary comprehension**

Similar to above method, another one-liner, difference being that items() is
used for element access.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Assign values to Values List

# Using items() + dictionary comprehension

 

# initializing dictionary

test_dict = {'Gfg': [3, 6],

 'is': [4, 2],

 'best': [9]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing lookup dict

look_dict = {3: [1, 5], 6: "Best", 4: 10,
9: 12, 2: "CS"}

 

# nested dictionaries to sought solution

# items() used to access key-val pairs

res = {key: {ikey: ival for (ikey, ival) in look_dict.items(

) if ikey in val} for (key, val) in test_dict.items()}

 

# printing result

print("The mapped dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original dictionary is : {'Gfg': [3, 6], 'is': [4, 2], 'best': [9]}
    The mapped dictionary : {'Gfg': {3: [1, 5], 6: 'Best'}, 'is': {4: 10, 2: 'CS'}, 'best': {9: 12}}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

