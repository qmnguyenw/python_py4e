Python – Extract Upper Case Characters



Sometimes, while working with strings, we are concerned about the case-
sensitivity of strings and might require to get just a specific case of
character in a long string. Let’s discuss certain ways in which only uppercase
letters can be extracted from a string.

 **Method #1 : Using list comprehension +isupper()**  
List comprehension and isupper function can be used to perform this particular
task. The list comprehension is primarily used to iterate over the list and
isupper function checks for the uppercase characters.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Upper Case Characters 

# Using list comprehension + isupper()

 

# initializing string 

test_str = "GeeksForGeeKs"

 

# printing original string 

print("The original string is : " + str(test_str))

 

# Extract Upper Case Characters 

# Using list comprehension + isupper()

res = [char for char in test_str if char.isupper()]

 

# printing result 

print("The uppercase characters in string are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : GeeksForGeeKs
    The uppercase characters in string are : ['G', 'F', 'G', 'K']
    

**Method #2 : Usingfilter() \+ lambda**  
Filter function along with lambda functionality can be used to perform this
particular task. The filter function performs the specific selection of case
characters and lambda function is used for string traversal.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Upper Case Characters

# Using filter() + lambda

 

# initializing string 

test_str = "GeeksForGeeKs"

 

# printing original string 

print("The original string is : " + str(test_str))

 

# Extract Upper Case Characters

# Using filter() + lambda

res = list(filter(lambda c: c.isupper(), test_str))

 

# printing result 

print("The uppercase characters in string are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : GeeksForGeeKs
    The uppercase characters in string are : ['G', 'F', 'G', 'K']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

