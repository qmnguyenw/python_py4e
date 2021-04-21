Python – Check if string starts with any element in list



While working with strings, their prefixes and suffix play an important role
in making any decision. For data manipulation tasks, we may need to sometimes,
check if a string starts with any of the matching strings. Let’s discuss
certain ways in which this task can be performed.

 **Method #1 : Usingfilter() + startswith()**  
The combination of the above function can help to perform this particular
task. The filter method is used to check for each word and startswith method
tests for the prefix logic at target list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Prefix tests in Strings

# using filter() + startswith()

 

# initializing string 

test_string = "GfG is best"

 

# initializing prefix list

pref_list = ['best', 'GfG', 'good']

 

# printing original string 

print("The original string : " + str(test_string))

 

# using filter() + startswith()

# Prefix tests in Strings

res = list(filter(test_string.startswith, pref_list)) != []

 

# print result

print("Does string start with any prefix list sublist ? : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : GfG is best
    Does string start with any prefix list sublist ? : True
    

**Method #2 : Usingstartswith()**  
As improvement to the above method, it is not always necessary to include
filter method for comparison. This task can be handled solely by supplying a
prefix check list as argument to startswith method as well.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Prefix tests in Strings

# using startswith()

 

# initializing string 

test_string = "GfG is best"

 

# initializing prefix list

pref_list = ['best', 'GfG', 'good']

 

# printing original string 

print("The original string : " + str(test_string))

 

# using startswith()

# Prefix tests in Strings

res = test_string.startswith(tuple(pref_list))

 

# print result

print("Does string start with any prefix list sublist ? : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : GfG is best
    Does string start with any prefix list sublist ? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

