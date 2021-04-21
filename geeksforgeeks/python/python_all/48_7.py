Python – Extract values of Particular Key in Nested Values



Given a dictionary with nested dictionaries as values, extract all the values
with of particular key.

>  **Input** : test_dict = {‘Gfg’ : {“a” : 7, “b” : 9, “c” : 12}, ‘is’ : {“a”
> : 15, “b” : 19, “c” : 20}, ‘best’ :{“a” : 5, “b” : 10, “c” : 2}}, temp = “b”  
>  **Output** : [9, 10, 19]  
>  **Explanation** : All values of “b” key are extracted.
>
>  **Input** : test_dict = {‘Gfg’ : {“a” : 7, “b” : 9, “c” : 12}, ‘is’ : {“a”
> : 15, “b” : 19, “c” : 20}, ‘best’ :{“a” : 5, “b” : 10, “c” : 2}}, temp = “a”  
>  **Output** : [7, 15, 5]  
>  **Explanation** : All values of “a” key are extracted.

 **Method #1 : Using list comprehension + items()**

This is one of the ways in which this task can be performed. In this, we use
list comprehension to perform the task of extracting particular key and
items() is used to get all the items().

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract values of Particular Key in Nested Values

# Using list comprehension

 

# initializing dictionary

test_dict = {'Gfg' : {"a" : 7, "b" : 9, "c" :
12},

 'is' : {"a" : 15, "b" : 19, "c" : 20}, 

 'best' :{"a" : 5, "b" : 10, "c" : 2}}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing key

temp = "c"

 

# using item() to extract key value pair as whole

res = [val[temp] for key, val in test_dict.items() if temp
in val]

 

# printing result 

print("The extracted values : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': {'a': 7, 'b': 9, 'c': 12}, 'is': {'a': 15, 'b': 19, 'c': 20}, 'best': {'a': 5, 'b': 10, 'c': 2}}
    The extracted values : [12, 20, 2]
    

**Method #2 : Using list comprehension + values() + keys()**

The combination of above functions can be used to solve this problem. In this,
we use values() and keys() to get values and keys separately rather than at
once extracted using items().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract values of Particular Key in Nested Values

# Using list comprehension + values() + keys() 

 

# initializing dictionary

test_dict = {'Gfg' : {"a" : 7, "b" : 9, "c" :
12},

 'is' : {"a" : 15, "b" : 19, "c" : 20}, 

 'best' :{"a" : 5, "b" : 10, "c" : 2}}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing key

temp = "c"

 

# using keys() and values() to extract values

res = [sub[temp] for sub in test_dict.values() if temp in
sub.keys()]

 

# printing result 

print("The extracted values : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': {'a': 7, 'b': 9, 'c': 12}, 'is': {'a': 15, 'b': 19, 'c': 20}, 'best': {'a': 5, 'b': 10, 'c': 2}}
    The extracted values : [12, 20, 2]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

