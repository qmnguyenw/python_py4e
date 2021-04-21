Python – Convert Float to digit list



Sometimes, while working with Python data, we can have a problem in which we
need to convert a float number into a list of digits. This problem is common
in day-day programming. Let’s discuss certain ways in which this task can be
performed.

 **Method #1 : Using list comprehension +isdigit()**  
The combination of above functions can be used to perform this task. In this,
we first convert the float number to string and then iterate it converting
each digit to integer and constructing the list using list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Float to digit list

# using list comprehension + isdigit()

 

# initialize N 

N = 6.456

 

# printing N 

print("The floating number is : " + str(N))

 

# Convert Float to digit list

# using list comprehension + isdigit()

res = [int(ele) for ele in str(N) if ele.isdigit()]

 

# printing result

print("List of floating numbers is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The floating number is : 6.456
    List of floating numbers is : [6, 4, 5, 6]
    

**Method #2 : Usingmap() \+ regex expression + findall()**  
The combination of above functionalities can be used to perform this task. In
this, we iterate through list using map() and extract and convert each element
of float number using regex expression and findall().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Float to digit list

# using map() + regex expression + findall()

import re

 

# initialize N 

N = 6.456

 

# printing N 

print("The floating number is : " + str(N))

 

# Convert Float to digit list

# using map() + regex expression + findall()

res = list(map(int, re.findall('\d', str(N))))

 

# printing result

print("List of floating numbers is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The floating number is : 6.456
    List of floating numbers is : [6, 4, 5, 6]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

