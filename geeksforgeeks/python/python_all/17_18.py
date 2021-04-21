Python program to calculate the number of words and characters in the string



Given a String. The task is to find out the Number Of Words And Characters
Present In The String.

 **Examples:**

    
    
     **Input:** Geeksforgeeks is best Computer Science Portal
    **Output:**
    The number Of Words are : 6
    The Number Of Charaters are : 45
    
    **Input:** Hello World!!!
    **Output:**
    The original string is : Hello World!!!
    The number of words in string are : 2
    The number of words in string are :  14

Count The Number Of Characters present in a string using len() function. You
can also use a for loop for counting characters

    
    
    char=0
    for i in string:
        char=char+1
    

For Counting

**Method 1: Using** **split()**

  

  

The split function is quite useful and usually quite a generic method to get
words out of the list, but this approach fails once we introduce special
characters in the list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to count words in string

# using split()

 

# initializing string

test_string = "Geeksforgeeks is best Computer Science Portal"

 

 

# printing original string

print("The original string is : " + test_string)

 

# using split()

# to count words in string

res = len(test_string.split())

 

# printing result

print("The number of words in string are : " + str(res))

print("The number of words in string are : ", len(test_string))  
  
---  
  
 __

 __

 **Output:**

> The original string is : Geeksforgeeks is best Computer Science Portal  
> The number of words in string are : 6  
> The number of words in string are : 45

 **Method 2:** Using regex module

Here findall() function is used to count the number of words in the sentence
available in a regex module.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import re

test_string = "GeeksForGeeks is a learning platform"

 

# original string

print("The original string is : " + test_string)

 

# using regex (findall()) function

res = len(re.findall(r'\w+', test_string))

 

# total no of words

print("The number of words in string are : " + str(res))

print("The number of Characters in string are : ",
len(test_string))  
  
---  
  
 __

 __

 **Output:**

> The original string is : GeeksForGeeks is a learning platform  
> The number of words in string are : 5  
> The number of Characters in string are : 36

 **Method 3:** Using sum()\+ strip()\+ split() function

Here we first check all the words in the given sentence and add them using the
sum() function.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import string

 

 

test_string = "GeeksForGeeks is a learning platform"

 

# printing original string

print("The original string is: " + test_string)

 

# using sum() + strip() + split() function

res = sum([i.strip(string.punctuation).isalpha() for i in

 test_string.split()])

 

# no of words

print("The number of words in string are : " + str(res))

print("The number of characters in string are : ",
len(test_string))  
  
---  
  
 __

 __

 **Output:**

> The original string is: GeeksForGeeks is a learning platform  
> The number of words in string are : 5  
> The number of characters in string are : 36

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

