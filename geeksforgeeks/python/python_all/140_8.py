Python | Check if string repeats itself



While working with strings, many times, we can come across a use case in which
we need to find if a string has in it the repeating substring, which repeats
all over the string and thus making a multiple of the root substring. Let’s
discuss certain ways in which we can get the root substring of string.

 **Method #1 : Using List comprehension + Brute Force**  
We can perform this task using selective slicing and brute force manner. This
is the naive method to find the string in which we try to get the root string
by repetitive division of string.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if string repeats itself

# Using List comprehension + Brute Force

 

# initializing string 

test_str = "GeeksforGeeksGeeksforGeeksGeeksforGeeks"

 

# printing original string 

print("The original string is : " + test_str)

 

# using List comprehension + Brute Force

# Check if string repeats itself

res = None

for i in range(1, len(test_str)//2 + 1):

 if (not len(test_str) % len(test_str[0:i]) and
test_str[0:i] *

 (len(test_str)//len(test_str[0:i])) == test_str):

 res = test_str[0:i]

 

# printing result 

print("The root substring of string : " + res)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : GeeksforGeeksGeeksforGeeksGeeksforGeeks
    The root substring of string : GeeksforGeeks
    

**Method #2 : Using list slicing +find()**

  

  

This problem can also be solved using the fact that we can search for root
string after adding a string and checking the root string in this string
except last and first character, represents the string is repeating itself.  
Doesn’t work for string length < 2.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if string repeats itself

# Using list slicing + find()

 

# initializing string 

test_str = "GeeksforGeeksGeeksforGeeksGeeksforGeeks"

 

# printing original string 

print("The original string is : " + test_str)

 

# using list slicing + find()

# Check if string repeats itself

res = None

temp = (test_str + test_str).find(test_str, 1, -1)

if temp != -1:

 res = test_str[:temp]

 

# printing result 

print("The root substring of string : " + res)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : GeeksforGeeksGeeksforGeeksGeeksforGeeks
    The root substring of string : GeeksforGeeks
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

