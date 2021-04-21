Python – Random Replacement of Word in String



Given a string and List, replace each occurrence of K word in string with
random element from list.

> **Input** : test_str = “Gfg is x. Its also x for geeks”, repl_list =
> [“Good”, “Better”, “Best”], repl_word = “x”  
>  **Output** : Gfg is Best. Its also Better for geeks  
>  **Explanation** : x is replaced by random replace list values.
>
>  **Input** : test_str = “Gfg is x. Its also x for geeks”, repl_list =
> [“Good”, “Better”, “Nice”], repl_word = “x”  
>  **Output** : Gfg is Best. Its also Nice for geeks  
>  **Explanation** : x is replaced by random replace list values, “Best” and
> “Nice”.

 **Method #1 : Using shuffle() + loop + replace()**

The combination of above functions can be used to solve this problem. In this,
we replace each occurrence of K word with random string from list using
replace().

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Random Replacement of Word in String

# Using replace() + shuffle() + loop

from random import shuffle

 

# initializing string

test_str = "Gfg is val. Its also val for geeks"

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing list 

repl_list = ["Good", "Better", "Best"]

 

# initializing replace word

repl_word = "val"

 

# shuffing list order

shuffle(repl_list)

for ele in repl_list:

 

 # replacing with random string 

 test_str = test_str.replace(repl_word, ele, 1)

 

# printing result 

print("String after random replacement : " + str(test_str))   
  
---  
  
__

__

**Output**

    
    
    The original string is : Gfg is val. Its also val for geeks
    String after random replacement : Gfg is Best. Its also Better for geeks
    
    

**Method #2 : Using list comprehension + replace() + shuffle()**

This is one of the ways in which this task can be performed. In this, we
encapsulate entire logic in one-liner using similar functionalities as above
method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Random Replacement of Word in String

# Using list comprehension + replace() + shuffle()

from random import shuffle

 

# initializing string

test_str = "Gfg is val. Its also val for geeks"

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing list 

repl_list = ["Good", "Better", "Best"]

 

# initializing replace word

repl_word = "val"

 

# one-liner to solve problem

shuffle(repl_list)

res = [test_str.replace(repl_word, ele, 1) for ele in
repl_list]

 

# printing result 

print("String after random replacement : " + str(res))   
  
---  
  
__

__

**Output**

> The original string is : Gfg is val. Its also val for geeks  
> String after random replacement : [‘Gfg is Good. Its also val for geeks’,
> ‘Gfg is Better. Its also val for geeks’, ‘Gfg is Best. Its also val for
> geeks’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

