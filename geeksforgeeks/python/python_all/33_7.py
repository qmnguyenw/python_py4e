Python program to extract key-value pairs with substring in a dictionary



Given a dictionary list, extract all the dictionaries which have substring
present in particular key.

>  **Input** : [{“Gfg” : “4”, “best” : “1”}, {“Gfg” : “good CS content”,
> “best” : “10”}], K = “Gfg”, sub_str = “CS”  
> **Output** : [{‘Gfg’: ‘good CS content’, ‘best’: ’10’}]  
> **Explanation** : “Gfg” has “CS” as substring value.
>
>  **Input** : [{“Gfg” : “4”, “best” : “1”}, {“Gfg” : “good content”, “best” :
> “10”}], K = “Gfg”, sub_str = “CS”  
> **Output** : []  
> **Explanation** : No dictionary with “CS” as substring to “Gfg” key.

**Method #1 : Using list comprehension**

This is one of the ways in which this task can be performed. In this, we
iterate for all the dictionaries and check for key’s value substring presence
using in operator.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Dictionaries with Substring values

# Using list comprehension

 

# initializing lists

test_list = [{"Gfg": "4", "best": "1"},

 {"Gfg": "good for CS", "best": "8"},

 {"Gfg": "good CS content", "best": "10"}]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing K key

K = "Gfg"

 

# initializing target value

sub_str = "CS"

 

# list comprehension to extract values with

# substring values using in operator

res = [val for val in test_list if sub_str in val[K]]

 

# printing result

print("Dictionaries with particular substring values : " +
str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list : [{‘Gfg’: ‘4’, ‘best’: ‘1’}, {‘Gfg’: ‘good for CS’,
> ‘best’: ‘8’}, {‘Gfg’: ‘good CS content’, ‘best’: ’10’}]  
> Dictionaries with particular substring values : [{‘Gfg’: ‘good for CS’,
> ‘best’: ‘8’}, {‘Gfg’: ‘good CS content’, ‘best’: ’10’}]

 **Method #2 : Using map() + in operator**

This is yet another way in which this task can be performed. In this, we
extract all the values with required substring using map() + lambda function.
The in operator is used to check for substring inside the key’s value.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Dictionaries with Substring values

# Using map() + in operator

 

# initializing lists

test_list = [{"Gfg": "4", "best": "1"},

 {"Gfg": "good for CS", "best": "8"},

 {"Gfg": "good CS content", "best": "10"}]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing K key

K = "Gfg"

 

# initializing target value

val = "CS"

 

# map() used to perform filtering

res = list(map(lambda sub: val in sub[K], test_list))

res = [test_list[idx] for idx, ele in enumerate(res) if
res[idx]]

 

# printing result

print("Dictionaries with particular substring values : " +
str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list : [{‘Gfg’: ‘4’, ‘best’: ‘1’}, {‘Gfg’: ‘good for CS’,
> ‘best’: ‘8’}, {‘Gfg’: ‘good CS content’, ‘best’: ’10’}]  
> Dictionaries with particular substring values : [{‘Gfg’: ‘good for CS’,
> ‘best’: ‘8’}, {‘Gfg’: ‘good CS content’, ‘best’: ’10’}]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

