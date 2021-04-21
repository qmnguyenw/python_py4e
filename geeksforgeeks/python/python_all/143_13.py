Python | Repeat String till K



Sometimes, while working with strings, we might encounter a use case in which
we need to repeat our string to the size of K, even though the last string
might not be complete, but has to stop as the size of string becomes K. The
problem of repeating string K times, is comparatively simpler than this
problem. Let’s discuss way outs we can perform to solve this problem.

 **Method #1 : Using list slicing and// operator**

This task can be performed using the above tools. In this we just multiply the
string till it becomes greater than or equal to K, and then just omit the
slice of extra string using the list slicing method.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Repeat string till K

# using list slicing and // operator

 

# initializing string 

test_string = "GeeksforGeeks"

 

# initializing K 

K = 30

 

# printing original string 

print("The original string : " + str(test_string))

 

# using list slicing and // operator

# Repeat string till K

res = (test_string * (K//len(test_string)+ 1))[:K]

 

# print result

print("String after performing repeatition : " + res)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : GeeksforGeeks
    String after performing repeatition : GeeksforGeeksGeeksforGeeksGeek
    

  

  

**Method #2 : Usingdivmod() \+ list slicing**

The division applied in the above method can be substituted in this method
with the divmod function, which improves code readability with the cost of
40% of performance degradation.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Repeat string till K

# using divmod() + list slicing

 

# initializing string 

test_string = "GeeksforGeeks"

 

# initializing K 

K = 30

 

# printing original string 

print("The original string : " + str(test_string))

 

# using divmod() + list slicing

# Repeat string till K

div, mod = divmod(K, len(test_string))

res = test_string * div + test_string[:mod]

 

# print result

print("String after performing repeatition : " + res)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : GeeksforGeeks
    String after performing repeatition : GeeksforGeeksGeeksforGeeksGeek
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

