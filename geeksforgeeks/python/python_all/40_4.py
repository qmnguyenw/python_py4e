Python – Extract domain name from Email address



Given a String Email address, extract the domain name.

>  **Input** : test_str = ‘manjeet@geeks.com’  
>  **Output** : geeks.com  
>  **Explanation** : Domain name, geeks.com extracted.
>
>  **Input** : test_str = ‘manjeet@gfg.com’  
>  **Output** : gfg.com  
>  **Explanation** : Domain name, gfg.com extracted.

 **Method #1 : Using index() + slicing**

In this, we harness the fact that “@” symbol is separator for domain name and
local-part of Email address, so, index() is used to get its index, and is then
sliced till end.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract domain name from Email address

# Using index() + slicing 

 

# initializing strings

test_str = 'manjeet@geeksforgeeks.com'

 

# printing original string

print("The original string is : " + str(test_str))

 

# slicing domain name using slicing 

res = test_str[test_str.index('@') + 1 : ]

 

# printing result 

print("The extracted domain name : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : manjeet@geeksforgeeks.com
    The extracted domain name : geeksforgeeks.com
    

**Method #2 : Using split()**

In this, we split the string on “@” and use its 1st index to get the required
domain name.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract domain name from Email address

# Using split()

 

# initializing strings

test_str = 'manjeet@geeksforgeeks.com'

 

# printing original string

print("The original string is : " + str(test_str))

 

# using split() to get domain name

res = test_str.split('@')[1]

 

# printing result 

print("The extracted domain name : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : manjeet@geeksforgeeks.com
    The extracted domain name : geeksforgeeks.com
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

