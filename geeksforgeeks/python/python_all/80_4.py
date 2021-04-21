Python | Split URL from Query Parameters



Sometimes, while web development, we can come across a task in which we may
require to perform a split of query parameters from URLs which is done by ‘?’
character. This has application over web develment as well as other domains
which involve URLs. Lets discuss certain ways in which this task can be
performed.

 **Method #1 : Usingsplit()**  
This is one of the way in which we can solve this problem. We split by ‘?’ and
return the first part of split for result.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Split URL from Query Parameters

# Using split()

 

# initializing string

test_str = 'www.geeksforgeeks.org?is = best'

 

# printing original string

print("The original string is : " + str(test_str))

 

# Split URL from Query Parameters

# Using split()

res = test_str.split('?')[0]

 

# printing result 

print("The base URL is : " + res)   
  
---  
  
__

__

**Output :**

    
    
    The original string is : www.geeksforgeeks.org?is=best
    The base URL is : www.geeksforgeeks.org
    

**Method #2 : Usingrfind()**  
This is another way in which we need to perform this task. In this, we find
the first occurrence of ‘?’ from right and slice the string.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Split URL from Query Parameters

# Using rfind()

 

# initializing string

test_str = 'www.geeksforgeeks.org?is = best'

 

# printing original string

print("The original string is : " + str(test_str))

 

# Split URL from Query Parameters

# Using rfind()

res = test_str[:test_str.rfind('?')]

 

# printing result 

print("The base URL is : " + res)   
  
---  
  
__

__

**Output :**

    
    
    The original string is : www.geeksforgeeks.org?is=best
    The base URL is : www.geeksforgeeks.org
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

