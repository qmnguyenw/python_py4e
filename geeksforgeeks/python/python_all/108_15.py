Python | Alternate cases in String



The problem of case changes a string is quite common and has been discussed
many times. Sometimes, we might have a problem like this in which we need to
convert the odd character of string to upper case and even positioned
characters to lowercase. Let’s discuss certain ways in which this can be
performed.

 **Method #1 : Usingupper() + lower() \+ loop**  
This task can be performed in brute force method in a way that we iterate
through the string and convert odd elements to uppercase and even to lower
case using upper() and lower() respectively.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Alternate cases in String

# Using upper() + lower() + loop

 

# initializing string 

test_str = "geeksforgeeks"

 

# printing original string 

print("The original string is : " + str(test_str))

 

# Using upper() + lower() + loop

# Alternate cases in String

res = ""

for idx in range(len(test_str)):

 if not idx % 2 :

 res = res + test_str[idx].upper()

 else:

 res = res + test_str[idx].lower()

 

# printing result 

print("The alterate case string is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : geeksforgeeks
    The alterate case string is : GeEkSfOrGeEkS
    

**Method #2 : Using list comprehension**  
This is the shortened one liner approach to this problem. It uses same logic
as above but in much more compact way.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Alternate cases in String

# Using list comprehension

 

# initializing string 

test_str = "geeksforgeeks"

 

# printing original string 

print("The original string is : " + str(test_str))

 

# Using list comprehension

# Alternate cases in String

res = [ele.upper() if not idx % 2 else ele.lower() for
idx, ele in enumerate(test_str)]

res = "".join(res)

 

# printing result 

print("The alterate case string is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : geeksforgeeks
    The alterate case string is : GeEkSfOrGeEkS
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

