Python | Find position of a character in given string



Given a string and a character, your task is to find the first position of the
character in the string. These types of problem are very competitive
programming where you need to locate the position of the character in a
string.

Let’s discuss a few methods to solve the problem.

 **Method #1: Using Naive Method**

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to find the first position of the character

# in a given string

 

# Initialising string

ini_string = 'abcdef'

 

# Character to find

c = "b"

# printing initial string and character

print ("initial_string : ", ini_string, "\ncharacter_to_find : ",
c)

 

# Using Naive Method

res = None

for i in range(0, len(ini_string)):

 if ini_string[i] == c:

 res = i + 1

 break

 

if res == None:

 print ("No such charater available in string")

else:

 print ("Character {} is present at {}".format(c, str(res)))  
  
---  
  
 __

 __

 **Output:**

    
    
    initial_string :  abcdef 
    character_to_find :  b
    Character b is present at 2
    

  
**Method #2: Using find**

  

  

This method returns -1 in case character not present.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to find first position of character

# in a given string

 

# Initialising string

ini_string = 'abcdef'

ini_string2 = 'xyze'

 

# Character to find

c = "b"

# printing initial string and character

print ("initial_strings : ", ini_string, " ", 

 ini_string2, "\ncharacter_to_find : ", c)

 

# Using find Method

res1 = ini_string.find(c)

res2 = ini_string2.find(c)

 

if res1 == -1:

 print ("No such charater available in string {}".format(

 ini_string))

else:

 print ("Character {} in string {} is present at {}".format(

 c, ini_string, str(res1 + 1)))

 

if res2 == -1:

 print ("No such charater available in string {}".format(

 ini_string2))

else:

 print ("Character {} in string {} is present at {}".format(

 c, ini_string2, str(res2 + 1)))  
  
---  
  
 __

 __

 **Output:**

    
    
    initial_strings :  abcdef   xyze 
    character_to_find :  b
    Character b in string abcdef is present at 2
    No such charater available in string xyze
    

  
**Method #3: Using index()**

This Method raises ValueError in case if character not present

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to find first position of character

# in a given string

 

# Initialising string

ini_string1 = 'xyze'

 

# Character to find

c = "b"

# printing initial string and character

print ("initial_strings : ", ini_string1,

 "\ncharacter_to_find : ", c)

 

# Using index Method

try:

 res = ini_string1.index(c)

 print ("Character {} in string {} is present at {}".format(

 c, ini_string1, str(res + 1)))

except ValueError as e:

 print ("No such charater available in string
{}".format(ini_string1))  
  
---  
  
 __

 __

 **Output:**

    
    
    initial_strings :  xyze 
    character_to_find :  b
    No such charater available in string xyze
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

