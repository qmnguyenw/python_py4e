Python – Create Nested Dictionary using given List



Given a list and dictionary, map each element of list with each item of
dictionary, forming nested dictionary as value.

>  **Input** : test_dict = {‘Gfg’ : 4, ‘best’ : 9}, test_list = [8, 2]  
>  **Output** : {8: {‘Gfg’: 4}, 2: {‘best’: 9}}  
>  **Explanation** : Index-wise key-value pairing from list [8] to dict {‘Gfg’
> : 4} and so on.
>
>  **Input** : test_dict = {‘Gfg’ : 4}, test_list = [8]  
>  **Output** : {8: {‘Gfg’: 4}}  
>  **Explanation** : Index-wise key-value pairing from list [8] to dict {‘Gfg’
> : 4}.

 **Method #1 : Using loop + zip()**

This is one of the ways in which this task can be performed. In this, we
combine both the lists using zip() and loop is used to do iteration of zipped
keys and dictionary construction.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Nested Dictionary with List

# Using loop + zip()

 

# initializing dictionary and list

test_dict = {'Gfg' : 4, 'is' : 5, 'best' : 9} 

test_list = [8, 3, 2]

 

# printing original dictionary and list

print("The original dictionary is : " + str(test_dict))

print("The original list is : " + str(test_list))

 

# using zip() and loop to perform 

# combining and assignment respectively.

res = {}

for key, ele in zip(test_list, test_dict.items()):

 res[key] = dict([ele])

 

# printing result 

print("The mapped dictionary : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': 4, 'is': 5, 'best': 9}
    The original list is : [8, 3, 2]
    The mapped dictionary : {8: {'Gfg': 4}, 3: {'is': 5}, 2: {'best': 9}}
    

**Method #2 : Using dictionary comprehension + zip()**

This is yet another way in which this task can be performed. In this, we
perform similar task as above method, but in one liner using dictionary
comprehension

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Nested Dictionary with List

# Using dictionary comprehension + zip()

 

# initializing dictionary and list

test_dict = {'Gfg' : 4, 'is' : 5, 'best' : 9} 

test_list = [8, 3, 2]

 

# printing original dictionary and list

print("The original dictionary is : " + str(test_dict))

print("The original list is : " + str(test_list))

 

# zip() and dictionary comprehension mapped in one liner to solve

res = {idx: {key : test_dict[key]} for idx, key in
zip(test_list, test_dict)}

 

# printing result 

print("The mapped dictionary : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': 4, 'is': 5, 'best': 9}
    The original list is : [8, 3, 2]
    The mapped dictionary : {8: {'Gfg': 4}, 3: {'is': 5}, 2: {'best': 9}}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

