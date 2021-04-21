Python program to Swap Keys and Values in Dictionary



Dictionary is quite a useful data structure in programming that is usually
used to hash a particular key with value, so that they can be retrieved
efficiently.

Let’s discuss various ways of swapping the keys and values in Python
Dictionary.

 **Method#1 (Does not work when there are multiple same values):**  
One naive solution may be something like just swapping the key and values
respectively.  
 **Example:**

>  **Input:** {‘A’: 67, ‘B’: 23, ‘C’: 45, ‘D’: 56, ‘E’: 12, ‘F’: 69, ‘G’: 67,
> ‘H’: 23}  
>  **Output:** {67: ‘G’, 69: ‘F’, 23: ‘H’, 56: ‘D’, 12: ‘E’, 45: ‘C’}

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# swap of key and value 

 

# initializing dictionary 

old_dict = {'A': 67, 'B': 23, 'C': 45, 'D':
56, 'E': 12, 'F': 69, 'G': 67, 'H': 23}

 

new_dict = dict([(value, key) for key, value in
old_dict.items()])

 

# Printing original dictionary 

print ("Original dictionary is : ")

print(old_dict) 

 

print()

 

# Printing new dictionary after swapping keys and values

print ("Dictionary after swapping is : ") 

print("keys: values")

for i in new_dict:

 print(i, " : ", new_dict[i])  
  
---  
  
 __

 __

 **Output**

  

  

    
    
    Original dictionary is : 
    {'D': 56, 'E': 12, 'C': 45, 'A': 67, 'F': 69, 'H': 23, 'B': 23, 'G': 67}
    
    Dictionary after swapping is :  
    keys: values
    67  :   G
    69  :   F
    23  :   B
    56  :   D
    12  :   E
    45  :   C
    

But there is a problem in this approach. In our example we have multiple keys
with same values i.e. (‘A’, 67) and (‘G’, 67) and the other keys having same
values is (‘B’, 23) and (‘H’, 23).  
But in the result we obtained only one key from each.  
i.e we obtained only (‘G’, 67) and (‘B’, 23).

So, here’s another approach to deal with this problem:

 **Method#2 (Handles multiple same values):**  
In this approach we will check if value is already present or not. If present
then just append it to the list.

 **Example:**

>  **Input:** {‘A’: 67, ‘B’: 23, ‘C’: 45, ‘E’: 12, ‘F’: 69, ‘G’: 67, ‘H’: 23}  
>  **Output:** {45: [‘C’], 67: [‘A’, ‘G’], 12: [‘E’], 69: [‘F’], 23: [‘B’,
> ‘H’]}

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# swap of key and value 

 

# initializing dictionary 

old_dict = {'A': 67, 'B': 23, 'C': 45, 'E':
12, 'F': 69, 'G': 67, 'H': 23}

 

# Printing original dictionary 

print ("Original dictionary is : ")

print(old_dict) 

 

print()

new_dict = {}

for key, value in old_dict.items():

 if value in new_dict:

 new_dict[value].append(key)

 else:

 new_dict[value]=[key]

 

# Printing new dictionary after swapping

# keys and values

print ("Dictionary after swapping is : ") 

print("keys: values")

for i in new_dict:

 print(i, " :", new_dict[i])  
  
---  
  
 __

 __

 **Output**

    
    
    Original dictionary is : 
    {'F': 69, 'G': 67, 'H': 23, 'A': 67, 'C': 45, 'B': 23, 'E': 12}
    
    Dictionary after swapping is :  
    keys: values
    45  : ['C']
    67  : ['G', 'A']
    12  : ['E']
    69  : ['F']
    23  : ['H', 'B']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

