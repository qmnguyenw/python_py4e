Python | Check if string ends with any string in given list



While working with strings, their prefixes and suffix play an important role
in making any decision. For data manipulation tasks, we may need to sometimes,
check if a string ends with any of the matching strings. Let’s discuss certain
ways in which this task can be performed.

 **Method #1 : Usingfilter() + endswith()**

The combination of the above function can help to perform this particular
task. The filter method is used to check for each word and endswith method
tests for the suffix logic at target list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Checking for string match suffix

# using filter() + endswith()

 

# initializing string 

test_string = "GfG is best"

 

# initializing suffix list

suff_list = ['best', 'iss', 'good']

 

# printing original string 

print("The original string : " + str(test_string))

 

# using filter() + endswith()

# Checking for string match suffix

res = list(filter(test_string.endswith, suff_list)) != []

 

# print result

print("Does string end with any suffix list sublist ? : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : GfG is best
    Does string end with any suffix list sublist ? : True
    

  

  

**Method #2 : Usingendswith()**

As an improvement to the above method, it is not always necessary to include
filter method for comparison. This task can be handled solely by supplying a
suffix check list as an argument to endswith method as well.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Checking for string match suffix

# using endswith()

 

# initializing string 

test_string = "GfG is best"

 

# initializing suffix list

suff_list = ['best', 'iss', 'good']

 

# printing original string 

print("The original string : " + str(test_string))

 

# using endswith()

# Checking for string match suffix

res = test_string.endswith(tuple(suff_list))

 

# print result

print("Does string end with any suffix list sublist ? : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : GfG is best
    Does string end with any suffix list sublist ? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

