Python – Vertical Concatenation in Matrix



Given a String Matrix, perform column-wise concatenation of strings, handling
variable lists lengths.

>  **Input** : [[“Gfg”, “good”], [“is”, “for”]]  
>  **Output** : [‘Gfgis’, ‘goodfor’]  
>  **Explanation** : Column wise concatenated Strings, “Gfg” concatenated with
> “is”, and so on.
>
>  **Input** : [[“Gfg”, “good”, “geeks”], [“is”, “for”, “best”]]  
>  **Output** : [‘Gfgis’, ‘goodfor’, “geeksbest”]  
>  **Explanation** : Column wise concatenated Strings, “Gfg” concatenated with
> “is”, and so on.

 **Method #1 : Using loop**

This is brute way in which this task can be performed. In this, we iterate for
all the columns and perform concatenation.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Vertical Concatenation in Matrix

# Using loop

 

# initializing lists

test_list = [["Gfg", "good"], ["is", "for"],
["Best"]]

 

# printing original list

print("The original list : " + str(test_list))

 

# using loop for iteration

res = []

N = 0

while N != len(test_list):

 temp = ''

 for idx in test_list:

 

 # checking for valid index / column

 try: temp = temp + idx[N]

 except IndexError: pass

 res.append(temp)

 N = N + 1

 

res = [ele for ele in res if ele]

 

# printing result 

print("List after column Concatenation : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [['Gfg', 'good'], ['is', 'for'], ['Best']]
    List after column Concatenation : ['GfgisBest', 'goodfor']
    

**Method #2 : Using join() + list comprehension + zip_longest()**

The combination of above functions can be used to solve this problem. In this,
we handle the null index values using zip_longest, and join() is used to
perform task of concatenation. The list comprehension drives one-liner logic.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Vertical Concatenation in Matrix

# Using join() + list comprehension + zip_longest()

from itertools import zip_longest

 

# initializing lists

test_list = [["Gfg", "good"], ["is", "for"],
["Best"]]

 

# printing original list

print("The original list : " + str(test_list))

 

# using join to concaternate, zip_longest filling values using 

# "fill"

res = ["".join(ele) for ele in zip_longest(*test_list, fillvalue
="")]

 

# printing result 

print("List after column Concatenation : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [['Gfg', 'good'], ['is', 'for'], ['Best']]
    List after column Concatenation : ['GfgisBest', 'goodfor']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

