Python – Differential Sort String Numbers and Alphabets



Given a List String, Reorder List, with Sorted Alphabets followed by Sorted
Strings.

>  **Input** : test_list = [“1”, “G”, “10”, “L”, “9”, “K”, “4”]  
>  **Output** : [‘G’, ‘K’, ‘L’, ‘1’, ‘4’, ‘9’, ’10’]  
>  **Explanation** : Alphabets sorted, succeeded by sorted digits.
>
>  **Input** : test_list = [“1”, “G”, “10”, “L”, “9”]  
>  **Output** : [‘G’, ‘L’, ‘1’, ‘9’, ’10’]  
>  **Explanation** : Alphabets sorted, succeeded by sorted digits.

 **Method #1 : Using isnumeric() + loop**

In this, we separate numerics and alphabetic characters, using isnumeric(),
and then perform sort on each list, then perform join of both lists for
obtaining result. Works with only 1 digit numbers string.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Differential Sort String Numbers and Alphabets

# Using isnumeric() + loop

 

# initializing list

test_list = ["1", "G", "7", "L", "9", "M",
"4"] 

 

# printing original list

print("The original list is : " + str(test_list))

 

numerics = []

alphabets = []

for sub in test_list:

 

 # checking and inserting in respective container

 if sub.isnumeric():

 numerics.append(sub)

 else:

 alphabets.append(sub)

 

# attaching lists post sort

res = sorted(alphabets) + sorted(numerics)

 

# printing result 

print("The Custom sorted result : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['1', 'G', '7', 'L', '9', 'M', '4']
    The Custom sorted result : ['G', 'L', 'M', '1', '4', '7', '9']
    
    

**Method #2 : Using sorted() + isnumeric()**

This is one liner way to solve this problem, it checks for numerics using
isnumeric and sorted() is used to perform sort(). Converts elements to
intergers and tests, can handle more than 1 digit numbers.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Differential Sort String Numbers and Alphabets

# Using sorted() + isnumeric()

 

# initializing list

test_list = ["100", "G", "74", "L", "98", "M",
"4"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# using int() to type convert to integer

# using sorted() to perform sort operation

res = sorted(test_list, key = lambda ele: (ele.isnumeric(),
int(ele) if ele.isnumeric() else ele))

 

# printing result 

print("The Custom sorted result : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['100', 'G', '74', 'L', '98', 'M', '4']
    The Custom sorted result : ['G', 'L', 'M', '4', '74', '98', '100']
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

