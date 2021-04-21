Python | Case Counter in String



Sometimes, while working with Python String, we can have a problem in which we
need to separate the lower and upper case count. This kind of operation can
have its application in many domains. Let’s discuss certain ways in which this
task can be done.

 **Method #1 : Usingmap() + sum() + isupper() + islower()**  
The combination of the above functions can be used to perform this task. In
this, we separately extract the count using sum() and map() and respective
inbuilt functions.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Case Counter in String

# using map() + sum() + isupper + islower

 

# initializing string 

test_str = "GFG is For GeeKs"

 

# printing original string 

print("The original string is : " + test_str)

 

# Case Counter in String

# using map() + sum() + isupper + islower

res_upper = sum(map(str.isupper, test_str))

res_lower = sum(map(str.islower, test_str))

 

# printing result

print("The count of Upper case characters : " + str(res_upper))

print("The count of Lower case characters : " + str(res_lower))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : GFG is For GeeKs
    The count of Upper case characters : 6
    The count of Lower case characters : 7
    

**Method #2 : Using Counter() +isupper() + islower()**  
The combinations of above methods can also be used to perform this particular
task. In this, we perform the task of holding count using Counter().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Case Counter in String

# using Counter() + isupper() + islower()

from collections import Counter

 

# initializing string 

test_str = "GFG is For GeeKs"

 

# printing original string 

print("The original string is : " + test_str)

 

# Case Counter in String

# using Counter() + isupper() + islower()

res = Counter("upper" if ele.isupper() else "lower" if
ele.islower()

 else " " for ele in test_str)

 

# printing result

print("The count of Upper case characters : " +
str(res['upper']))

print("The count of Lower case characters : " +
str(res['lower']))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : GFG is For GeeKs
    The count of Upper case characters : 6
    The count of Lower case characters : 7
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

