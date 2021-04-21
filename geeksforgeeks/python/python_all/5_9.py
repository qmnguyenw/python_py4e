Python Program To Convert dictionary values to Strings



Given dictionary with mixed data types as values, the task is to write a
Python program to convert to parsed strings by different delims.

 **Examples:**

>  **Input :** test_dict = {‘Gfg’ : 4, ‘is’ : “1”, ‘best’ : [8, 10], ‘geek’ :
> (10, 11, 2)}, list_delim, tuple_delim = ‘-‘, ‘^’
>
>  **Output :** {‘Gfg’: ‘4’, ‘is’: ‘1’, ‘best’: ‘8-10’, ‘geek’: ’10^11^2′}
>
>  **Explanation :** List elements are joined by -, tuples by ^ symbol.
>
>  
>
>
>  
>
>
>  **Input :** test_dict = {‘Gfg’ : 4, ‘is’ : “1”, ‘best’ : [8, 10], ‘geek’ :
> (10, 11, 2)}, list_delim, tuple_delim = ‘*’, ‘,’
>
>  **Output :** {‘Gfg’: ‘4’, ‘is’: ‘1’, ‘best’: ‘8*10’, ‘geek’: ‘10,11,2’}
>
>  **Explanation :** List elements are joined by *, tuples by , symbol.

 **Example: Using** **loop** **+** **isinstance()** **+** **join()**

In this, we check for all the values data types using isinstance() and join
using join() for difference delims, converting to parsed strings.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert dictionary values to Strings

# Using loop + isinstance()

 

# initializing dictionary

test_dict = {'Gfg' : 4,

 'is' : "1",

 'best' : [8, 10],

 'geek' : (10, 11, 2)}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing delims

list_delim, tuple_delim = '-', '^'

 

res = dict()

for sub in test_dict:

 

 # checking data types

 if isinstance(test_dict[sub], list):

 res[sub] = list_delim.join([str(ele) for ele in
test_dict[sub]])

 elif isinstance(test_dict[sub], tuple):

 res[sub] = tuple_delim.join(list([str(ele) for ele in
test_dict[sub]]))

 else:

 res[sub] = str(test_dict[sub])

 

# printing result

print("The converted dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original dictionary is : {‘Gfg’: 4, ‘is’: ‘1’, ‘best’: [8, 10], ‘geek’:
> (10, 11, 2)}
>
> The converted dictionary : {‘Gfg’: ‘4’, ‘is’: ‘1’, ‘best’: ‘8-10’, ‘geek’:
> ’10^11^2′}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

