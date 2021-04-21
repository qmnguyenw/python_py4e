Python | Removing Initial word from string



During programming, sometimes, we can have such a problem in which it is
required that first word from the string has to be removed. These kind of
problems are common and one should be aware about the solution for such
problems. Let’s discuss certain ways in which this problem can be solved.

 **Method #1 : Usingsplit()**  
This task can be performed using the split function which performs a split
of words and separates the first word of string with the entire words.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Removing Initial word from string

# Using split()

 

# initializing string 

test_str = "GeeksforGeeks is best"

 

# printing original string 

print("The original string is : " + test_str)

 

# Using split()

# Removing Initial word from string

res = test_str.split(' ', 1)[1]

 

# printing result 

print("The string after omitting first word is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : GeeksforGeeks is best
    The string after omitting first word is : is best
    

**Method #2 : Usingpartition()**  
The partition function is used to perform this particular task in
comparatively lesser internal task as compared to function used in above
method.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Removing Initial word from string

# Using partition()

 

# initializing string 

test_str = "GeeksforGeeks is best"

 

# printing original string 

print("The original string is : " + test_str)

 

# Using partition()

# Removing Initial word from string

res = test_str.partition(' ')[2]

 

# printing result 

print("The string after omitting first word is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : GeeksforGeeks is best
    The string after omitting first word is : is best
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

