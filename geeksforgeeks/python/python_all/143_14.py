Python | Find last occurrence of substring



Sometimes, while working with strings, we need to find if a substring exists
in the string. This problem is quite common and its solution has been
discussed many times before. The variation of getting the last occurrence of
the string is discussed here. Let’s discuss certain ways in which this can be
performed.

 **Method #1 : Usingrindex()**

This method returns the last occurrence of the substring if present in the
string. The drawback of this function is that it throws the exception if there
is no substring in the string and hence breaks the code.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Find last occurrence of substring

# using rindex()

 

# initializing string 

test_string = "GfG is best for CS and also best for Learning"

 

# initializing target word 

tar_word = "best"

 

# printing original string 

print("The original string : " + str(test_string))

 

# using rindex()

# Find last occurrence of substring

res = test_string.rindex(tar_word)

 

# print result

print("Index of last occurrence of substring is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : GfG is best for CS and also best for Learning
    Index of last occurrence of substring is : 28
    

  

  

**Method #2 : Usingrfind()**

This is the alternate method to perform this task. The advantage that this
function offers better than the above method is that, this function returns a
“-1” if a substring is not found rather than throwing the error.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Find last occurrence of substring

# using rfind()

 

# initializing string 

test_string = "GfG is best for CS and also best for Learning"

 

# initializing target word 

tar_word = "best"

 

# printing original string 

print("The original string : " + str(test_string))

 

# using rfind()

# Find last occurrence of substring

res = test_string.rfind(tar_word)

 

# print result

print("Index of last occurrence of substring is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : GfG is best for CS and also best for Learning
    Index of last occurrence of substring is : 28
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

