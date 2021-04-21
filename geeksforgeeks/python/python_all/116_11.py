Python | Split strings and digits from string list



Sometimes, while working with String list, we can have a problem in which we
need to remove the surrounding stray characters or noise from list of digits.
This can be in form of Currency prefix, signs of numbers etc. Let’s discuss a
way in which this task can be performed.

 **Method : Using list comprehension +strip() + isdigit() + join()**  
The combination of above functions can be used to perform this task. In this,
we strip the stray characters from numbers that are identified from the
strings and return the result.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract digit from string list 

# using list comprehension + strip() + isdigit() + join()

from itertools import groupby

 

# initialize list 

test_list = ["-4", "Rs 25", "5 kg", "+15"]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Extract digit from string list 

# using list comprehension + strip() + isdigit() + join()

res = [''.join(j).strip() for sub in test_list 

 for k, j in groupby(sub, str.isdigit)]

 

# printing result

print("List after removing stray characters : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['-4', 'Rs 25', '5 kg', '+15']
    List after removing stray characters : ['-', '4', 'Rs', '25', '5', 'kg', '+', '15']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

