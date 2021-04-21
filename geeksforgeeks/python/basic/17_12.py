Python Dictionary fromkeys() Method



Sometimes there is a need to generate a dictionary from the given keys. Brute
implementation of it would take time and would be more tedious job. Hence,
fromkeys() helps us achieve this very task with ease and using just a single
method. This article explains working and other aspects associated with this
function.

>  **Syntax :** fromkeys(seq, val)
>
>  **Parameters :**  
>  **seq :** The sequence to be transformed into a dictionary.  
>  **val :** Initial values that need to be assigned to the generated keys.
> Defaults to None.
>
>  **Returns :** A dictionary with keys mapped to None if no value is
> provided, else to the value provided in the field.

 **Code #1 :** Demonstrating the working of fromkeys()

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# working of fromkeys()

 

# initializing sequence 

seq = { 'a', 'b', 'c', 'd', 'e' }

 

# using fromkeys() to convert sequence to dict 

# initializing with None

res_dict = dict.fromkeys(seq)

 

# Printing created dict

print ("The newly created dict with None values : " +
str(res_dict))

 

 

# using fromkeys() to convert sequence to dict 

# initializing with 1

res_dict2 = dict.fromkeys(seq, 1)

 

# Printing created dict

print ("The newly created dict with 1 as value : " +
str(res_dict2))  
  
---  
  
 __

 __

 **Output :**

> The newly created dict with None values : {‘d’: None, ‘a’: None, ‘b’: None,
> ‘c’: None, ‘e’: None}  
> The newly created dict with 1 as value : {‘d’: 1, ‘a’: 1, ‘b’: 1, ‘c’: 1,
> ‘e’: 1}

**Behaviour of fromdict() with Mutable objects as values:**

fromdict() can also be supplied with mulatable object as default value. But in
this case, a deep copy is made of dictionary, i.e if we append value in
original list, the append takes place in all the values of keys.

 **Prevention :** Certain dictionary comprehension techniques can be used to
create a new list as key values, that does not point to original list as
values of keys.

 **Code #2 :** Demonstrating the behaviour with mutable objects.

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# behaviour with mutable objects

 

# initializing sequence and list

seq = { 'a', 'b', 'c', 'd', 'e' }

lis1 = [ 2, 3 ]

 

# using fromkeys() to convert sequence to dict

# using conventional method

res_dict = dict.fromkeys(seq, lis1)

 

# Printing created dict

print ("The newly created dict with list values : "

 + str(res_dict))

 

# appending to lis1

lis1.append(4)

 

# Printing dict after appending

# Notice that append takes place in all values

print ("The dict with list values after appending : "

 + str(res_dict))

 

lis1 = [ 2, 3 ]

print ('\n')

 

# using fromkeys() to convert sequence to dict

# using dict. comprehension

res_dict2 = { key : list(lis1) for key in seq }

 

# Printing created dict

print ("The newly created dict with list values : "

 + str(res_dict2))

 

# appending to lis1

lis1.append(4)

 

# Printing dict after appending

# Notice that append doesnt take place now.

print ("The dict with list values after appending (no change) : "

 + str(res_dict2))  
  
---  
  
 __

 __

 **Output:**

> The newly created dict with list values : {‘d’: [2, 3], ‘e’: [2, 3], ‘c’:
> [2, 3], ‘a’: [2, 3], ‘b’: [2, 3]}  
> The dict with list values after appending : {‘d’: [2, 3, 4], ‘e’: [2, 3, 4],
> ‘c’: [2, 3, 4], ‘a’: [2, 3, 4], ‘b’: [2, 3, 4]}
>
> The newly created dict with list values : {‘d’: [2, 3], ‘e’: [2, 3], ‘c’:
> [2, 3], ‘a’: [2, 3], ‘b’: [2, 3]}  
> The dict with list values after appending (no change) : {‘d’: [2, 3], ‘e’:
> [2, 3], ‘c’: [2, 3], ‘a’: [2, 3], ‘b’: [2, 3]}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

