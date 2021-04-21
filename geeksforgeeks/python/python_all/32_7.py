Python program to count the number of characters in a String



Given a String. The task is to return the number of characters in the string.

 **Examples:**

>  **Input** : test_str = ‘geeksforgeeks !!$*** best 4 all Geeks 10-0’  
> **Output** : 25  
>  **Explanation** : Only alphabets, when counted are 25
>
>  **Input** : test_str = ‘geeksforgeeks !!$*** best for all Geeks 10—0’  
> **Output** : 27  
>  **Explanation** : Only alphabets, when counted are 27

 **Method #1 : Using isalpha() + len()**

  

  

In this approach, we check for each character to be alphabet using isalpha()
and len() is used to get the length of the list of alphabets to get count.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Alphabets Frequency in String

# Using isalpha() + len()

 

# initializing string

test_str = 'geeksforgeeks !!$ is best 4 all Geeks 10-0'

 

# printing original string

print("The original string is : " + str(test_str))

 

# isalpha() to computation of Alphabets

res = len([ele for ele in test_str if ele.isalpha()])

 

# printing result

print("Count of Alphabets : " + str(res))  
  
---  
  
 __

 __

 **Output**

> The original string is : geeksforgeeks !!$ is best 4 all Geeks 10-0  
> Count of Alphabets : 27

 **Method #2 : Using ascii_uppercase() + ascii_lowercase() + len()**

In this, we perform the task of getting alphabets as a combination of upper
and lowercase, using inbuilt functions, len() returns frequency.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Alphabets Frequency in String

# Using ascii_uppercase() + ascii_lowercase() + len()

import string

 

# initializing string

test_str = 'geeksforgeeks !!$ is best 4 all Geeks 10-0'

 

# printing original string

print("The original string is : " + str(test_str))

 

# ascii_lowercase and ascii_uppercase

# to check for Alphabets

res = len([ele for ele in test_str if ele in
string.ascii_uppercase or ele in string.ascii_lowercase])

 

# printing result

print("Count of Alphabets : " + str(res))  
  
---  
  
 __

 __

 **Output**

> The original string is : geeksforgeeks !!$ is best 4 all Geeks 10-0  
> Count of Alphabets : 27

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

