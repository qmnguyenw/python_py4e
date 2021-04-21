Python | Add one string to another



Concatenation of two strings have been discussed multiple times over various
languages. But the task of adding one string to other is quite easy task in
Python. Knowledge of performing this task has many application. Let’s discuss
certain ways in which this can be performed.

 **Method #1 : Using+= operator**

This operator can be used to perform this particular task of concatenating the
string. This is quite simpler than the traditional methods that are employed
in other languages, like using a dedicated function to perform this particular
task.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# Adding one string to another

# Using += operator

 

# initializing string 

test_string = "GFG"

 

# initializing add_string

add_string = " is best"

 

# printing original string 

print("The original string : " + str(test_string))

 

# printing original add string 

print("The add string : " + str(add_string))

 

# Using += operator

# adding one string to another 

test_string += add_string

 

# print result

print("The concatenated string is : " + test_string)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : GFG
    The add string :  is best
    The concatenated string is : GFG is best
    

  

  

**Method #2 : Using join()**

One can also perform this very task of the concatenation of string using the
join function. The advantage this method holds over the above method is when
we have many strings to concatenate rather than just two.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# Adding one string to another

# Using join()

 

# initializing string 

test_string = "GFG"

 

# initializing add_string

add_string = " is best"

 

# printing original string 

print("The original string : " + str(test_string))

 

# printing original add string 

print("The add string : " + str(add_string))

 

# Using join()

# adding one string to another 

res = "".join((test_string, add_string))

 

# print result

print("The concatenated string is : " + res)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : GFG
    The add string :  is best
    The concatenated string is : GFG is best
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

