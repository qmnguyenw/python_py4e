Python | Frequency of substring in given string



Finding a substring in a string has been dealt in many ways. But sometimes, we
are just interested to know how many times a particular substring occurs in a
string. Let’s discuss certain ways in which this task is performed.

 **Method #1 : Usingcount()**  
This is a quite straightforward method in which this task is performed. It
simply counts the occurrence of substrings in a string that we pass as an
argument.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Frequency of substring in string 

# Using count()

 

# initializing string 

test_str = "GeeksforGeeks is for Geeks"

 

# initializing substring

test_sub = "Geeks"

 

# printing original string 

print("The original string is : " + test_str)

 

# printing substring

print("The original substring : " + test_sub)

 

# using count()

# Frequency of substring in string

res = test_str.count(test_sub)

 

# printing result 

print("The frequency of substring in string is " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : GeeksforGeeks is for Geeks
    The original substring : Geeks
    The frequency of substring in string is 3
    

**Method #2 : Usinglen() + split()**  
The combination of above functions can be used to perform this task. This is
performed in 2 steps, in 1st step, we split the string to list by the
substring and then count the elements, which is 1 more than the required
value.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Frequency of substring in string 

# Using split() + len()

 

# initializing string 

test_str = "GeeksforGeeks is for Geeks"

 

# initializing substring

test_sub = "Geeks"

 

# printing original string 

print("The original string is : " + test_str)

 

# printing substring

print("The original substring : " + test_sub)

 

# using split() + len()

# Frequency of substring in string

res = len(test_str.split(test_sub))-1

 

# printing result 

print("The frequency of substring in string is " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : GeeksforGeeks is for Geeks
    The original substring : Geeks
    The frequency of substring in string is 3
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

