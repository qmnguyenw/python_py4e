Python – Replace Different characters in String at Once



Given a mapping of characters to be replaced with corresponding values,
perform all replaces at one, in one liner.

>  **Input** : test_str = ‘geeksforgeeks is best’, map_dict = {‘e’:’1′,
> ‘b’:’6′}  
>  **Output** : g11ksforg11ks is 61st  
>  **Explanation** : All e are replaced by 1 and b by 6.
>
>  **Input** : test_str = ‘geeksforgeeks’, map_dict = {‘e’:’1′, ‘b’:’6′}  
>  **Output** : g11ksforg11ks  
>  **Explanation** : All e are replaced by 1 and b by 6.

 **Method #1 : Using join() + generator expression**

In this, we perform the task of getting characters present in dictionary and
map them to their values by dictionary access, all other characters are
appended unchanged, the result is converted back to dictionary using join().

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace Different characters in String at Once

# using join() + generator expression 

 

# initializing string

test_str = 'geeksforgeeks is best'

 

# printing original String

print("The original string is : " + str(test_str))

 

# initializing mapping dictionary

map_dict = {'e':'1', 'b':'6', 'i':'4'}

 

# generator expression to construct vals 

# join to get string 

res = ''.join(idx if idx not in map_dict else map_dict[idx]
for idx in test_str)

 

# printing result 

print("The converted string : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeksforgeeks is best
    The converted string : g11ksforg11ks 4s 61st
    

**Method #2 : Using regex + lambda**

This is complex way to approach problem. In this, we construct appropriate
regex using lambda functions and peform the required task of replacement.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace Different characters in String at Once

# using regex + lambda

import re

 

# initializing string

test_str = 'geeksforgeeks is best'

 

# printing original String

print("The original string is : " + str(test_str))

 

# initializing mapping dictionary

map_dict = {'e':'1', 'b':'6', 'i':'4'}

 

# using lambda and regex functions to achieve task 

res = re.compile("|".join(map_dict.keys())).sub(lambda ele:
map_dict[re.escape(ele.group(0))], test_str)

 

# printing result 

print("The converted string : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeksforgeeks is best
    The converted string : g11ksforg11ks 4s 61st
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

