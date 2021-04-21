Python – Concatenate Random characters in String List



Given a String list, perform concatenaton of random characters.

>  **Input** : test_list = [“Gfg”, “is”, “Best”, “for”, “Geeks”]  
>  **Output** : “GiBfe”  
>  **Explanation** : Random elements selected, e.g G from Gfg, etc.
>
>  **Input** : test_list = [“Gfg”, “is”, “Best”]  
>  **Output** : “fst”  
>  **Explanation** : Random elements selected, e.g t from Best, etc.

 **Method #1 : Using loop + random.choice()**

In this, we extract random character using choice() and perform task of
iteration using loop. The character concatenation is done using + operator.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Concatenate Random characters in String List

# Using loop + choice()

import random

 

# initializing list

test_list = ["Gfg", "is", "Best", "for", "Geeks"]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = ''

for ele in test_list:

 

 # Concatenating random elements

 res += random.choice(ele)

 

# printing results

print("Concatenated String : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['Gfg', 'is', 'Best', 'for', 'Geeks']
    Concatenated String : Gsere
    

**Method #2 : Using list comprehension + choice() + join()**

In this, we perform task of getting random using choice() and concatenation is
done using join().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Concatenate Random characters in String List

# Using list comprehension + choice() + join()

import random

 

# initializing list

test_list = ["Gfg", "is", "Best", "for", "Geeks"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# characters joining using join()

res = ''.join([random.choice(ele) for ele in test_list])

 

# printing results

print("Concatenated String : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['Gfg', 'is', 'Best', 'for', 'Geeks']
    Concatenated String : Gitrk
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

