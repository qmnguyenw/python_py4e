Python | Return lowercase characters from given string



Sometimes, while working with strings, we are concerned about the case-
sensitivity of strings and might require to get just a specific case of
character in a long string. Let’s discuss certain ways in which only lowercase
letters can be extracted from a string.

 **Method #1 : Using list comprehension +islower()**  
List comprehension and islower function can be used to perform this particular
task. The list comprehension is primarily used to iterate over the list and
islower function checks for the lowercase characters.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Return lowercase characters in string 

# Using list comprehension + islower()

 

# initializing string 

test_str = "GeeksForGeeKs"

 

# printing original string 

print("The original string is : " + str(test_str))

 

# Return lowercase characters in string 

# Using list comprehension + islower()

res = [char for char in test_str if char.islower()]

 

# printing result 

print("The lowercase characters in string are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original string is : GeeksForGeeKs  
> The lowercase characters in string are : [‘e’, ‘e’, ‘k’, ‘s’, ‘o’, ‘r’, ‘e’,
> ‘e’, ‘s’]

  

  

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

# Return lowercase characters in string 

# Using filter() + lambda

 

# initializing string 

test_str = "GeeksForGeeKs"

 

# printing original string 

print("The original string is : " + str(test_str))

 

# Return lowercase characters in string 

# Using filter() + lambda

res = list(filter(lambda c: c.islower(), test_str))

 

# printing result 

print("The lowercase characters in string are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original string is : GeeksForGeeKs  
> The lowercase characters in string are : [‘e’, ‘e’, ‘k’, ‘s’, ‘o’, ‘r’, ‘e’,
> ‘e’, ‘s’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

