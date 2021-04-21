Python – Convert Suffix denomination to Values



Given strings list with denomination suffix, the task is to write a Python
program to convert string to its actual values, substituting for denomination
actual values.

>  **Input** : test_list = [“25Cr”, “7M”, “24B”, “9L”, “2Tr”, “17K”]  
> **Output** : [250000000.0, 7000000.0, 24000000000.0, 900000.0,
> 2000000000000.0, 17000.0]  
> **Explanation** : Suffix replaced as per Symbol notations with numerical
> figure.
>
>  **Input** : test_list = [“25Cr”, “7M”, “24B”]  
> **Output** : [250000000.0, 7000000.0, 24000000000.0]  
> **Explanation** : Suffix replaced as per Symbol notations with numerical
> figure.

**Approach: Using** **float()** **+** **dictionary** **+** **loop**

In this, we construct a dictionary of all denomination with its original
values and then convert the value to float and perform multiplication with the
denomination’s actual value.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Suffix denomination to Values

# Using float() + dictionary + loop

 

# initializing list

test_list = ["25Cr", "7M", "24B", "9L", "2Tr",
"17K"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing values dictionary

val_dict = {"M": 1000000, "B": 1000000000, "Cr":
10000000,

 "L": 100000, "K": 1000, "Tr": 1000000000000}

 

res = []

for ele in test_list:

 for key in val_dict:

 if key in ele:

 

 # conversion of dictionary keys to values

 val = float(ele.replace(key, "")) * val_dict[key]

 res.append(val)

 

# printing result

print("The resolved dictionary values : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [’25Cr’, ‘7M’, ’24B’, ‘9L’, ‘2Tr’, ’17K’]  
> The resolved dictionary values : [250000000.0, 7000000.0, 24000000000.0,
> 900000.0, 2000000000000.0, 17000.0]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

