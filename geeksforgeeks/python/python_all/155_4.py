Python | Extract numbers from string



Many times, while working with strings we come across this issue in which we
need to get all the numeric occurrences. This type of problem generally occurs
in competitive programming and also in web development. Let’s discuss certain
ways in which this problem can be solved.

 **Method #1 : Using List comprehension +isdigit() \+ split()**  
This problem can be solved by using split function to convert string to list
and then the list comprehension which can help us iterating through the list
and isdigit function helps to get the digit out of a string.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# getting numbers from string 

# using List comprehension + isdigit() +split()

 

# initializing string 

test_string = "There are 2 apples for 4 persons"

 

# printing original string 

print("The original string : " + test_string)

 

# using List comprehension + isdigit() +split()

# getting numbers from string 

res = [int(i) for i in test_string.split() if
i.isdigit()]

 

# print result

print("The numbers list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : There are 2 apples for 4 persons
    The numbers list is : [2, 4]
    

**Method #2 : Usingre.findall()**  
This particular problem can also be solved using python regex, we can use the
findall function to check for the numeric occurrences using matching regex
string.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# getting numbers from string 

# using re.findall()

import re

 

# initializing string 

test_string = "There are 2 apples for 4 persons"

 

# printing original string 

print("The original string : " + test_string)

 

# using re.findall()

# getting numbers from string 

temp = re.findall(r'\d+', test_string)

res = list(map(int, temp))

 

# print result

print("The numbers list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : There are 2 apples for 4 persons
    The numbers list is : [2, 4]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

