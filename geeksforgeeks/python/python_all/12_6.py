Python program to Increment Numeric Strings by K



Given the Strings list, write a Python program to increment strings that are
numeric by K.

 **Examples:**

>  **Input** : test_list = [“gfg”, “234”, “is”, “98”, “123”, “best”, “4”], K =
> 6  
> **Output** : [‘gfg’, ‘240’, ‘is’, ‘104’, ‘129’, ‘best’, ’10’]  
> **Explanation** : 234, 98 and 4 are incremented by 6 in result.
>
>  **Input** : test_list = [“gfg”, “234”, “is”, “98”, “123”, “best”, “4”], K =
> 4  
> **Output** : [‘gfg’, ‘238’, ‘is’, ‘102’, ‘129’, ‘best’, ‘8’]  
> **Explanation** : 234, 98 and 4 are incremented by 4 in result.

**Method #1 : Using** **str()** **+** **int()** **\+ loop +** **isdigit()**

  

  

In this, we perform task of interconversion of elements using str() + int(),
and check for number using isdigit(), iteration is done using loop.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Increment Numeric Strings by K

# Using str() + int() + loop + isdigit()

 

# initializing Matrix

test_list = ["gfg", "234", "is", "98", "123",
"best", "4"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 6

 

res = []

for ele in test_list:

 

 # incrementing on testing for digit.

 if ele.isdigit():

 res.append(str(int(ele) + K))

 else:

 res.append(ele)

 

# printing result

print("Incremented Numeric Strings : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘gfg’, ‘234’, ‘is’, ’98’, ‘123’, ‘best’, ‘4’]  
> Incremented Numeric Strings : [‘gfg’, ‘240’, ‘is’, ‘104’, ‘129’, ‘best’,
> ’10’]

 **Method #2 : Using** **list comprehension** **+** **isdigit()**

This is one of the ways in which this task can be performed. Similar to above,
just one line alternative to compact the solution using list comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Increment Numeric Strings by K

# Using list comprehension + isdigit()

 

# initializing Matrix

test_list = ["gfg", "234", "is", "98", "123",
"best", "4"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 6

 

# increment Numeric digits.

res = [str(int(ele) + K) if ele.isdigit() else ele
for ele in test_list]

 

# printing result

print("Incremented Numeric Strings : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘gfg’, ‘234’, ‘is’, ’98’, ‘123’, ‘best’, ‘4’]  
> Incremented Numeric Strings : [‘gfg’, ‘240’, ‘is’, ‘104’, ‘129’, ‘best’,
> ’10’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

