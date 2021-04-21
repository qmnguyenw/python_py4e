Python – Extract Key’s value from Mixed Dictionaries List



Given a list of dictionaries, with each dictionary having different keys,
extract value of key K.

>  **Input** : test_list = [{“Gfg” : 3, “b” : 7}, {“is” : 5, ‘a’ : 10},
> {“Best” : 9, ‘c’ : 11}], K = ‘b’  
>  **Output** : 7  
>  **Explanation** : Value of b is 7.
>
>  **Input** : test_list = [{“Gfg” : 3, “b” : 7}, {“is” : 5, ‘a’ : 10},
> {“Best” : 9, ‘c’ : 11}], K = ‘c’  
>  **Output** : 11  
>  **Explanation** : Value of c is 11.

 **Method #1 : Using list comprehension**

This is one of the ways in which this task can be performed. In this, we
iterate for each dictionary inside list, and check for key in it, if present
the required valu is returned.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Key's value from Mixed Dictionaries List

# Using list comprehension

 

# initializing list

test_list = [{"Gfg" : 3, "b" : 7}, 

 {"is" : 5, 'a' : 10}, 

 {"Best" : 9, 'c' : 11}]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing K 

K = 'Best'

 

# list comprehension to get key's value 

# using in operator to check if key is present in dictionary

res = [sub[K] for sub in test_list if K in sub][0]

 

# printing result 

print("The extracted value : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [{'Gfg': 3, 'b': 7}, {'is': 5, 'a': 10}, {'Best': 9, 'c': 11}]
    The extracted value : 9
    

**Method #2 : Using update() + loop**

This is yet another way in which this task can be performed. In this, we
update each dictionary into each other. Forming one large dictionary, and then
value is extracted from this dictionary.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Key's value from Mixed Dictionaries List

# Using update() + loop

 

# initializing list

test_list = [{"Gfg" : 3, "b" : 7}, 

 {"is" : 5, 'a' : 10}, 

 {"Best" : 9, 'c' : 11}]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing K 

K = 'Best'

 

res = dict()

for sub in test_list:

 

 # merging all Dictionaries into 1

 res.update(sub)

 

# printing result 

print("The extracted value : " + str(res[K]))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [{'Gfg': 3, 'b': 7}, {'is': 5, 'a': 10}, {'Best': 9, 'c': 11}]
    The extracted value : 9
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

