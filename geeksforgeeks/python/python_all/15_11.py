Python – Summation of consecutive elements power



Given a List, the task is to write a Python program to compute summation of
power of consecutive elements occurrences frequency.

 **Examples:**

>  **Input** : test_list = [2, 2, 2, 3, 3, 3, 3, 4, 4, 5]  
> **Output** : 110  
> **Explanation** : 2^3 + 3^4 + 4^2 + 5 = 110  
>
>
> **Input** : test_list = [2, 2, 2, 3, 3, 3, 3, 4, 4]  
> **Output** : 105  
> **Explanation** : 2^3 + 3^4 + 4^2 = 105

**Method #1 : Using loop**

  

  

In this, we iterate for each element and test for next element, if found to be
different, perform summation of power of consecutive elements, else add
counter to get frequency to raise number to.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Summation of consecutive elements power

# Using loop

 

# initializing list

test_list = [2, 2, 2, 3, 3, 3, 3, 4,
4, 5]

 

# printing original lists

print("The original list is : " + str(test_list))

 

freq = 1

res = 0

for idx in range(0, len(test_list) - 1):

 

 # adding powers

 if test_list[idx] != test_list[idx + 1]:

 res = res + test_list[idx] ** freq

 freq = 1

 else:

 freq += 1

 

# catering for last element

res = res + test_list[len(test_list) - 1] ** freq

 

# printing result

print("Computed summation of powers : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [2, 2, 2, 3, 3, 3, 3, 4, 4, 5]
    Computed summation of powers : 110

 **Method #2 : Using** **defaultdict()** **\+ loop +** **sum()**

In this we capture frequency using defautldict using key value pairs and loop
is used to iterate through each element. Next, summation is performed using
sum().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Summation of consecutive elements power

# Using defaultdict() + loop + sum()

from collections import defaultdict

 

# initializing list

test_list = [2, 2, 2, 3, 3, 3, 3, 4,
4, 5]

 

# printing original lists

print("The original list is : " + str(test_list))

 

# getting frequency

temp = defaultdict(int)

for ele in test_list:

 temp[ele] += 1

 

temp = dict(temp)

 

# computing summation

res = sum([key ** temp[key] for key in temp])

 

# printing result

print("Computed summation of powers : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [2, 2, 2, 3, 3, 3, 3, 4, 4, 5]
    Computed summation of powers : 110

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

