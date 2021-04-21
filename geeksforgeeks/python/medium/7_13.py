Ways to convert string to dictionary



Dictionary is an unordered collection in Python which store data values like a
map i.e., key:value pair. In order to convert a String into a dictionary,
the stored string must be in such a way that key:value pair can be generated
from it. This article demonstrates several ways of converting a string into a
dictionary.

 **Method 1: Splitting a string to generatekey:value pair of the
dictionary**  
In this approach, the given string will be analysed and with the use of
split() method, the string will be split in such a way that it generates the
key:value pair for the creation of a dictionary.

Below is the implementation of the approach.

 __

 __  
 __

 __

 __  
 __  
 __

# Python implementation of converting

# a string into a dictionary

 

# initialising string 

str = " Jan = January; Feb = February; Mar = March"

 

# At first the string will be splitted

# at the occurence of ';' to divide items 

# for the dictionaryand then again splitting 

# will be done at occurence of '=' which

# generates key:value pair for each item

dictionary = dict(subString.split("=") for subString in
str.split(";"))

 

# printing the generated dictionary

print(dictionary)  
  
---  
  
 __

 __

 **Output:**

    
    
    {' Feb ': ' February', ' Mar ': ' March', ' Jan ': ' January'}
    

**Method 2: Using 2 strings to generate thekey:value pair for the
dictionary**  
In this approach, 2 different strings will be considered and one of them will
be used to generate keys and another one will be used to generate values for
the dictionary. After manipulating both the strings the dictionary items will
be created using those key:value pair.

  

  

Below is the implementation of the approach.

 __

 __  
 __

 __

 __  
 __  
 __

# Python implementation of converting

# a string into a dictionary

 

# initialising first string

str1 = "Jan, Feb, March"

str2 = "January | February | March"

 

# splitting first string

# in order to get keys

keys = str1.split(", ")

 

# splitting second string

# in order to get values

values = str2.split("|")

 

# declaring the dictionary

dictionary = {}

 

# Assigning keys and its 

# corresponding values in

# the dictionary

for i in range(len(keys)):

 dictionary[keys[i]] = values[i]

 

# printing the generated dictionary

print(dictionary)  
  
---  
  
 __

 __

 **Output:**

    
    
    {'Jan': 'January ', 'Feb': ' February ', 'March': ' March'}
    

**Method 3: Usingzip() method to combine the key:value pair extracted from
2 string**  
In this approach, again 2 strings will be used, one for generating keys and
another for generating values for the dictionary. When all the keys and values
are stored, zip() method will be used to create key:value pair and thus
generating the complete dictionary.

Below is the implementation of the approach.

 __

 __  
 __

 __

 __  
 __  
 __

# Python implementation of converting

# a string into a dictionary

 

# initialising first string

str1 = "Jan, Feb, March"

str2 = "January | February | March"

 

# splitting first string

# in order to get keys

keys = str1.split(", ")

 

# splitting second string

# in order to get values

values = str2.split("|")

 

# declaring the dictionary

dictionary = {}

 

# Merging all keys and values

# to generate items for

# the dictionary

dictionary = dict(zip(keys, values))

 

# printing the generated dictionary

print(dictionary)  
  
---  
  
 __

 __

 **Output:**

    
    
    {' March': ' March', 'Jan': 'January ', ' Feb': ' February '}
    

**Method 4: If the string is itself in the form of string dictionary**  
In this approach, a string which is already in the form of string dictionary
i.e., the **string has a dictionary expression** is converted into a
dictionary using ast.literal_eval() method.

Below is the implementation of the approach.

 __

 __  
 __

 __

 __  
 __  
 __

# Python implementation of converting

# a string into a dictionary

 

# importing ast module

import ast 

 

# initialising string dictionary 

str = '{"Jan" : "January", "Feb" : "February", "Mar" : "March"}'

 

# converting string into dictionary

dictionary = ast.literal_eval(str)

 

# printing the generated dictionary

print(dictionary)  
  
---  
  
 __

 __

 **Output:**

    
    
    {'Feb': 'February', 'Jan': 'January', 'Mar': 'March'}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

