Python | Alternate character addition



Sometimes, while working with Python, we can have a problem in which we need
to add a character after every character in String. This kind of problem can
have its application in many day-day programming domains. Lets discuss certain
ways in which this task can be performed.

 **Method #1 : Using loop**  
This is brute force way in which this task can be performed. In this, we
iterate for each element and insert the character required. We erase tha last
stray character.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Alternate character addition

# Using loop

 

# initializing string

test_str = "geeksforgeeks"

 

# printing original string

print("The original string is : " + test_str)

 

# initializing K 

K = '*'

 

# Alternate character addition

# Using loop

res = ''

for ele in test_str:

 res += ele + K

res = res[:-1]

 

# printing result 

print("String after character addition : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : geeksforgeeks
    String after character addition : g*e*e*k*s*f*o*r*g*e*e*k*s
    

**Method #2 : Usingjoin()**  
This is easiest, elegant and recommended way to perform this task. In this, we
just use one line to perform this task. The join() is used to perform it.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Alternate character addition

# Using join()

 

# initializing string

test_str = "geeksforgeeks"

 

# printing original string

print("The original string is : " + test_str)

 

# initializing K 

K = '*'

 

# Alternate character addition

# Using join()

res = K.join(test_str)

 

# printing result 

print("String after character addition : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : geeksforgeeks
    String after character addition : g*e*e*k*s*f*o*r*g*e*e*k*s
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

