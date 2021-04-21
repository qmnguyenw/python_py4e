Python program to concatenate Strings around K



Given List of Strings, join all the strings which occurs around string K.

>  **Input** : test_list = [“Gfg”, “*”, “is”, “best”, “*”, “love”, “gfg”], K =
> “*”  
> **Output** : [‘Gfg*is’, ‘best*love’, ‘gfg’]  
> **Explanation** : All elements around * are joined.
>
>  **Input** : test_list = [“Gfg”, “$”, “is”, “best”, “$”, “love”, “gfg”], K =
> “$”  
> **Output** : [‘Gfg$is’, ‘best$love’, ‘gfg’]  
> **Explanation** : All elements around $ are joined.  
>

**Method 1: Using** a **loop**

This is a brute way in which this task can be performed. In this, we iterate
through all the elements and check for K, if found we perform required
concatenation with preceding and successive element.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Concatenate Strings on K String

# Using loop

 

# initializing list

test_list = ["Gfg", "+", "is", "best", "+",
"love", "gfg"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K for Concatenate

K = "+"

 

res = []

idx = 0

 

while idx < len(test_list):

 

 ele = test_list[idx]

 

 # concatenation if next symbol is K

 if (idx < len(test_list) - 1) and test_list[idx + 1]
== K:

 ele = ele + K + test_list[idx + 2]

 

 # increasing counter by 2

 idx += 2

 res.append(ele)

 idx += 1

 

# printing result

print("Strings after required concatenation : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['Gfg', '+', 'is', 'best', '+', 'love', 'gfg']
    Strings after required concatenation : ['Gfg+is', 'best+love', 'gfg']
    

  
**Method 2 : Using** **join()** **+** **replace()** **+** **split()**

The combination of the above functions can be used to solve this problem. In
this, we perform joining of all elements and then remove space around target
K. Being treated as a single string, splitting the required string produces
joined values around K.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = ["Gfg", "+", "is", "best", "+",
"love", "gfg"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K for Concatenate

K = "+"

 

# performing split after removing space around K

# splits assuming Strings joined around K

res = ' '.join(test_list).replace(' ' + K + ' ',
K).split()

 

# printing result

print("Strings after required concatenation : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['Gfg', '+', 'is', 'best', '+', 'love', 'gfg']
    Strings after required concatenation : ['Gfg+is', 'best+love', 'gfg']
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

