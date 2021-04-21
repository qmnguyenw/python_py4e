Python – Replace words from Dictionary



Given String, replace it’s words from lookup dictionary.

>  **Input** : test_str = ‘geekforgeeks best for geeks’, repl_dict = {“geeks”
> : “all CS aspirants”}  
>  **Output** : geekforgeeks best for all CS aspirants  
>  **Explanation** : “geeks” word is replaced by lookup value.
>
>  **Input** : test_str = ‘geekforgeeks best for geeks’, repl_dict = {“good” :
> “all CS aspirants”}  
>  **Output** : geekforgeeks best for geeks  
>  **Explanation** : No lookup value, unchanged result.

 **Method #1 : Using split() + get() + join()**

In this, we initially split the list using split(), then look for lookups
using get(), and if found, replaced and joined back to string using join().

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace words from Dictionary

# Using split() + join() + get()

 

# initializing string

test_str = 'geekforgeeks best for geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# lookup Dictionary

lookp_dict = {"best" : "good and better", "geeks" : "all CS
aspirants"}

 

# performing split()

temp = test_str.split()

res = []

for wrd in temp:

 

 # searching from lookp_dict

 res.append(lookp_dict.get(wrd, wrd))

 

res = ' '.join(res)

 

# printing result 

print("Replaced Strings : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geekforgeeks best for geeks
    Replaced Strings : geekforgeeks good and better for all CS aspirants
    

**Method #2 : Using list comprehension + join()**

Similar to above method, difference just being 1 liner rather than 3-4 steps
in separate lines.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace words from Dictionary

# Using list comprehension + join()

 

# initializing string

test_str = 'geekforgeeks best for geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# lookup Dictionary

lookp_dict = {"best" : "good and better", "geeks" : "all CS
aspirants"}

 

# one-liner to solve problem

res = " ".join(lookp_dict.get(ele, ele) for ele in
test_str.split())

 

# printing result 

print("Replaced Strings : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geekforgeeks best for geeks
    Replaced Strings : geekforgeeks good and better for all CS aspirants
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

