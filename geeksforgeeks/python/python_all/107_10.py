Python – Kth word replace in String



Sometimes, while working with String list, we can have a problem in which we
need to replace the most Kth word of string. This problem has many application
in web development domain. Let’s discuss a way in which this problem can be
solved.

 **Method : Usingsplit() + join()**  
This is way in which we can perform this task. In this, we break elements into
parts and then return the Kth value and perform the addition of new element
using join().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Kth word replace in String

# using split() + join()

 

# initializing string 

test_str = "GFG is good"

 

# printing original string 

print("The original string is : " + test_str)

 

# initializing replace string 

rep_str = "best"

 

# initializing K 

K = 1

 

# Kth word replace in String

# using split() + join()

temp = test_str.split(' ')

res = " ".join(temp[: K] + [rep_str] + temp[K + 1 :])

 

# printing result

print("The String after performing replace : " + res)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : GFG is good
    The String after performing replace : GFG best good
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

