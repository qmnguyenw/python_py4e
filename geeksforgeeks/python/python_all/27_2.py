Python program to check whether the values of a dictionary are in same order
as in a list



Given a dictionary, test if values are in order with list values.

>  **Input** : test_dict = {“gfg” : 4, “is” : 10, “best” : 11}, sub_list = [4,
> 10, 11]  
> **Output** : True  
> **Explanation** : Values are 4, 10, 11, same as list order. Hence True is
> returned.  
>
>
> **Input** : test_dict = {“gfg” : 4, “is” : 10, “best” : 11}, sub_list = [4,
> 11, 10]  
> **Output** : False  
> **Explanation** : Values are 4, 10, 11, list order is 4, 11, 10, not same
> order. Hence False is returned.

**Method #1 : Using** **loop**

In this, we iterate for dictionary values and list alongside, and test if all
the values are in order, flag off in case any element is out of order.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test for Ordered values from List

# Using loop

 

# initializing dictionary

test_dict = {"gfg" : 4, "is" : 10, "best" : 11,
"for" : 19, "geeks" : 1}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing list 

sub_list = [4, 10, 11, 19, 1]

 

idx = 0

res = True

for key in test_dict:

 

 # checking for inequality in order

 if test_dict[key] != sub_list[idx]:

 res = False

 break

 idx += 1

 

# printing result 

print("Are values in order : " + str(res))   
  
---  
  
__

__

**Output:**

> The original dictionary is : {‘gfg’: 4, ‘is’: 10, ‘best’: 11, ‘for’: 19,
> ‘geeks’: 1}  
> Are values in order : True

 **Method #2 : Using** **values()** **+** **comparison** **operators**

In this, we extract all the values using values() and then use comparison
operators to check for equality with list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test for Ordered values from List

# Using values() + comparison operators

 

# initializing dictionary

test_dict = {"gfg" : 4, "is" : 10, "best" : 11,
"for" : 19, "geeks" : 1}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing list 

sub_list = [4, 10, 11, 19, 1]

 

# comparing values with list

res = list(test_dict.values()) == sub_list

 

# printing result 

print("Are values in order : " + str(res))   
  
---  
  
__

__

**Output:**

> The original dictionary is : {‘gfg’: 4, ‘is’: 10, ‘best’: 11, ‘for’: 19,
> ‘geeks’: 1}  
> Are values in order : True

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

