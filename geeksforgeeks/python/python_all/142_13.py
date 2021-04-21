Python | Extract digits from given string



While programming, sometimes, we just require a certain type of data and need
to discard other. This type of problem is quite common in Data Science domain,
and since Data Science uses Python worldwide, its important to know how to
extract specific elements. This article discusses certain ways in which only
digit can be extracted. Let’s discuss the same.

 **Method #1 : Usingjoin() + isdigit() + filter()**

This task can be performed using the combination of above functions. The
filter function filters the digits detected by the isdigit function and join
function performs the task of reconstruction of join function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Extract digit string 

# using join() + isdigit() + filter()

 

# initializing string

test_string = 'g1eeks4geeks5'

 

# printing original strings 

print("The original string : " + test_string)

 

# using join() + isdigit() + filter()

# Extract digit string 

res = ''.join(filter(lambda i: i.isdigit(), test_string))

 

# print result

print("The digits string is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : g1eeks4geeks5
    The digits string is : 145
    

  

  

**Method #2 : Usingre**  
The regular expressions can also be used to perform this particular task. We
can define the digit type requirement, using “\D”, and only digits are
extracted from the string.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Extract digit string 

# using re

import re

 

# initializing string

test_string = 'g1eeks4geeks5'

 

# printing original strings 

print("The original string : " + test_string)

 

# using re

# Extract digit string 

res = re.sub("\D", "", test_string)

 

# print result

print("The digits string is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : g1eeks4geeks5
    The digits string is : 145
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

