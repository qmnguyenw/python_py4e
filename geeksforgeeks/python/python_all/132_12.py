Python | Key-Value to URL Parameter Conversion



Many times, while working in web development domain, we can encounter a
problem in which we require to set as URL parameter some of the key-value
pairs we have, either in form of tuples, or a key and value list. Let’s
discuss a solution for both the cases.

 **Method #1 : Usingurllib.urlencode() ( with tuples )**  
The urlencode function is root function that can perform the task that we
wish to achieve. In case of tuples, we can just pass the tuples and encoder
does the rest of conversion of string. Works only with Python2.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# Key-Value to URL Parameter Conversion

# Using urllib.urlencode() ( with tuples )

import urllib

 

# initializing tuples

test_tuples = (('Gfg', 1), ('is', 2), ('best',
3))

 

# printing original tuples

print("The original tuples are : " + str(test_tuples))

 

# Using urllib.urlencode() ( with tuples )

# Key-Value to URL Parameter Conversion

res = urllib.urlencode(test_tuples)

 

# printing URL string

print("The URL parameter string is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuples are : (('Gfg', 1), ('is', 2), ('best', 3))
    The URL parameter string is : Gfg=1&is=2&best=3
    

**Method #2 : Usingurllib.urlencode() ( with dictionary value list )**  
This method is when we have a dictionary key and many values corresponding to
them as a potential candidate for being the URL parameter. In this case we
perform this function. This also works with just Python2.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# Key-Value to URL Parameter Conversion

# Using urllib.urlencode() ( with dictionary value list )

import urllib

 

# initializing dictionary

test_dict = {'gfg' : [1, 2, 3]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Using urllib.urlencode() ( with dictionary value list )

# Key-Value to URL Parameter Conversion

res = urllib.urlencode(test_dict, doseq = True)

 

# printing URL string

print("The URL parameter string is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'gfg': [1, 2, 3]}
    The URL parameter string is : gfg=1&gfg=2&gfg=3
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

