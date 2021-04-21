Python program to find the key of maximum value tuples in a dictionary



Given a dictionary with values as tuples, the task is to write a python
program to find the key of maximum value tuples.

**Examples:**

>  **Input :** test_dict = {‘gfg’ : (“a”, 3), ‘is’ : (“c”, 9), ‘best’ : (“k”,
> 10), ‘for’ : (“p”, 11), ‘geeks’ : (‘m’, 2)}
>
>  **Output :** for
>
>  **Explanation :** 11 is maximum value of tuple and for key “for”.
>
>  
>
>
>  
>
>
>  **Input :** test_dict = {‘gfg’ : (“a”, 13), ‘is’ : (“c”, 9), ‘best’ : (“k”,
> 10), ‘for’ : (“p”, 1), ‘geeks’ : (‘m’, 2)}
>
>  **Output :** gfg
>
>  **Explanation :** 13 is maximum value of tuple and for key “gfg”.

 **Method #1 : Using** **max()** **+** **values()** **+** **next()**

In this, the maximum of all the tuple values are found using max(), and values
are extracted using values(). The next(), is used for iteration using the
iterator method of access, and each tuple value is compared with the maximum
value.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Maximum tuple value key

# Using max() + values() + next()

 

# initializing dictionary

test_dict = {'gfg': ("a", 3), 'is': ("c", 9),
'best': (

 "k", 10), 'for': ("p", 11), 'geeks': ('m',
2)}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# getting maximum value

max_val = max(test_dict.values(), key=lambda sub: sub[1])

 

# getting key with maximum value using comparison

res = next(key for key, val in test_dict.items() if val
== max_val)

 

# printing result

print("The maximum key : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original dictionary is : {‘gfg’: (‘a’, 3), ‘is’: (‘c’, 9), ‘best’: (‘k’,
> 10), ‘for’: (‘p’, 11), ‘geeks’: (‘m’, 2)}
>
> The maximum key : for
>
>  
>
>
>  
>

 **Method #2 : Using** **list comprehension** **+** **max()** **+**
**values()**

In this, we perform the task of getting all the maximum matching values using
list comprehension. Getting maximum is done using max().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Maximum tuple value key

# Using list comprehension + max() + values()

 

# initializing dictionary

test_dict = {'gfg': ("a", 3), 'is': ("c", 9),
'best': (

 "k", 10), 'for': ("p", 11), 'geeks': ('m',
2)}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# getting maximum value

max_val = max(test_dict.values(), key=lambda sub: sub[1])

 

# getting key with maximum value using comparison

res = [key for key, val in test_dict.items() if val ==
max_val][0]

 

# printing result

print("The maximum key : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original dictionary is : {‘gfg’: (‘a’, 3), ‘is’: (‘c’, 9), ‘best’: (‘k’,
> 10), ‘for’: (‘p’, 11), ‘geeks’: (‘m’, 2)}
>
> The maximum key : for

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

