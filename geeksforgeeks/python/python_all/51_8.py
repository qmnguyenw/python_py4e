Python – Sort String by Custom Integer Substrings



Given a list of strings, sort strings by occurrence of substring from list.

>  **Input** : test_list = [“Good at 4”, “Wake at 7”, “Work till 6”, “Sleep at
> 11”], subord_list = [“11”, “7”, “4”, “6”]  
>  **Output** : [‘Sleep at 11’, ‘Wake at 7’, ‘Good at 4’, ‘Work till 6’]  
>  **Explanation** : Strings sorted by substring presence.
>
>  **Input** : test_list = [“Good at 9”, “Wake at 7”, “Work till 6”, “Sleep at
> 11”], subord_list = [“11”, “7”, “9”, “6”]  
>  **Output** : [‘Sleep at 11’, ‘Wake at 7’, ‘Good at 9’, ‘Work till 6’]  
>  **Explanation** : Strings sorted by substring presence.

 **Method #1 : Using sorted() + zip() + lambda + regex()**

The combination of above functions can be used to solve this problem. In this,
we perform task of sorting by substring using regex() and sorted(), zip() is
used to produce end result.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort String by Custom Substrings

# Using sorted() + zip() + lambda + regex()

import re

 

# initializing list

test_list = ["Good at 4", "Wake at 7", "Work till 6",
"Sleep at 11"]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing subtring list 

subord_list = ["6", "7", "4", "11"]

 

 

# crearing inverse mapping with index

temp_dict = {val: key for key, val in enumerate(subord_list)}

 

# custom sorting 

temp_list = sorted([[ele, temp_dict[re.search("(\d+)$",
ele).group()]] \

 for ele in test_list], key = lambda x: x[1])

# compiling result

res = [ele for ele in list(zip(*temp_list))[0]]

 

# printing result 

print("The sorted list : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : ['Good at 4', 'Wake at 7', 'Work till 6', 'Sleep at 11']
    The sorted list : ['Work till 6', 'Wake at 7', 'Good at 4', 'Sleep at 11']
    

**Method #2 : Using sorted() + zip() + comparator + regex()**

This is yet another way in which this task can be performed. In this similar
functionality is used as above method, difference is that comparator function
is fed to sorted() rather than lambda to sort.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort String by Custom Substrings

# Using sorted() + comparator + regex()

import re

 

# helper function to solve problem

def hlper_fnc(ele):

 temp = re.search("(\d+)$", ele).group()

 return temp_dict[temp] if temp in temp_dict else
int(temp)

 

# initializing list

test_list = ["Good at 4", "Wake at 7", "Work till 6",
"Sleep at 11"]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing subtring list 

subord_list = ["6", "7", "4", "11"]

 

# crearing inverse mapping with index

temp_dict = {val: key for key, val in enumerate(test_list)}

 

# sorting using comparator

test_list.sort(key = lambda ele: hlper_fnc(ele))

 

# printing result 

print("The sorted list : " + str(test_list))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : ['Good at 4', 'Wake at 7', 'Work till 6', 'Sleep at 11']
    The sorted list : ['Good at 4', 'Work till 6', 'Wake at 7', 'Sleep at 11']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

