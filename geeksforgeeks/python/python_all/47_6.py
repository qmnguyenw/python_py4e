Python – Unpacking Values in Strings



Given a dictionary, unpack its values into a string.

>  **Input** : test_str = “First value is {} Second is {}”, test_dict = {3 :
> “Gfg”, 9 : “Best”}  
>  **Output** : First value is Gfg Second is Best  
>  **Explanation** : After substitution, we get Gfg and Best as values.
>
>  **Input** : test_str = “First value is {} Second is {}”, test_dict = {3 :
> “G”, 9 : “f”}  
>  **Output** : First value is G Second is f.  
>  **Explanation** : After substitution, we get G and f as values.

 **Method : Using format() + * operator + values()**

The combination of above functions can be used to solve this problem. In this,
we use format to map required value with braces in string. The * operator is
used to unpack and assign. The values are extracted using values().

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Unpacking Integer Keys in Strings

# Using format() + * operator + values()

 

# initializing string

test_str = "First value is {} Second is {} Third {}"

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing dictionary 

test_dict = {3 : "Gfg", 4 : "is", 9 : "Best"}

 

# using format() for mapping required values 

res = test_str.format(*test_dict.values())

 

# printing result 

print("String after unpacking dictionary : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : First value is {} Second is {} Third {}
    String after unpacking dictionary : First value is Gfg Second is is Third Best
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

