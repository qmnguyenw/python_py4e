Python – Convert Tuple value list to List of tuples



Given a dictionary with values as tuple list, convert to key mapped list of
tuples.

>  **Input** : test_dict = {‘Gfg’ : [(5, 6, 7), (6, )], ‘is’ : [(5, 5, 2, 2,
> 6)], ‘best’ :[(7, )]}  
>  **Output** : [(‘Gfg’, 5, 6, 7), (‘Gfg’, 6), (‘is’, 5, 5, 2, 2, 6), (‘best’,
> 7)]  
>  **Explanation** : Keys grouped with values.
>
>  **Input** : test_dict = {‘Gfg’ : [(5, ), (6, )], ‘is’ : [(5, )], ‘best’
> :[(7, )]}  
>  **Output** : [(‘Gfg’, 5), (‘Gfg’, 6), (‘is’, 5), (‘best’, 7)]  
>  **Explanation** : Keys grouped with values.

 **Method #1 : Using loop + * operator + items()**

This is one of the ways in which this task can be performed. In this we
iterate for all the keys using loop and map keys with all values by unpacking
all values in tuple using * operator.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Tuple value list to List of tuples

# Using loop + * operator + items()

 

# initializing dictionary

test_dict = {'Gfg' : [(5, 6, 7), (1, 3), (6,
)],

 'is' : [(5, 5, 2, 2, 6)], 

 'best' :[(7, ), (9, 16)]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# using items() to extract all the items of 

# dictionary

res = []

for key, val in test_dict.items():

 for ele in val:

 res.append((key, *ele))

 

# printing result 

print("The converted tuple list : " + str(res))   
  
---  
  
__

__

**Output**

> The original dictionary is : {‘Gfg’: [(5, 6, 7), (1, 3), (6, )], ‘is’: [(5,
> 5, 2, 2, 6)], ‘best’: [(7, ), (9, 16)]}  
> The converted tuple list : [(‘Gfg’, 5, 6, 7), (‘Gfg’, 1, 3), (‘Gfg’, 6),
> (‘is’, 5, 5, 2, 2, 6), (‘best’, 7), (‘best’, 9, 16)]

 **Method #2 : Using list comprehension + * operator + items()**

This is yet another way to solve this problem. Solves in similar way as above
method. Only difference being offers one-liner solution using list
comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Tuple value list to List of tuples

# Using list comprehension + * operator + items()

 

# initializing dictionary

test_dict = {'Gfg' : [(5, 6, 7), (1, 3), (6,
)],

 'is' : [(5, 5, 2, 2, 6)], 

 'best' :[(7, ), (9, 16)]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# list comprehension encapsulates whole logic 

# into one line

res = [(key, *ele) for key, sub in test_dict.items() for
ele in sub]

 

# printing result 

print("The converted tuple list : " + str(res))   
  
---  
  
__

__

**Output**

> The original dictionary is : {‘Gfg’: [(5, 6, 7), (1, 3), (6, )], ‘is’: [(5,
> 5, 2, 2, 6)], ‘best’: [(7, ), (9, 16)]}  
> The converted tuple list : [(‘Gfg’, 5, 6, 7), (‘Gfg’, 1, 3), (‘Gfg’, 6),
> (‘is’, 5, 5, 2, 2, 6), (‘best’, 7), (‘best’, 9, 16)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

