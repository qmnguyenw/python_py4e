Python – Insert character in each duplicate string after every K elements



Given a string and a character, insert character after every K occurrences.

>  **Input** : test_str = ‘GeeksforGeeks’, K = 2, add_chr = “;”  
> **Output** : [‘;GeeksforGeeks’, ‘Ge;eksforGeeks’, ‘Geek;sforGeeks’,
> ‘Geeksf;orGeeks’, ‘Geeksfor;Geeks’, ‘GeeksforGe;eks’, ‘GeeksforGeek;s’]  
> **Explanation** : All combinations after adding ; after every K elements.
>
>  **Input** : test_str = ‘GeeksforGeeks’, K = 2, add_chr = “*”  
> **Output** : [‘*GeeksforGeeks’, ‘Ge*eksforGeeks’, ‘Geek*sforGeeks’,
> ‘Geeksf*orGeeks’, ‘Geeksfor*Geeks’, ‘GeeksforGe*eks’, ‘GeeksforGeek*s’]  
> **Explanation** : All combinations after adding * after every K elements.  
>

**Method #1 : Using loop + string slicing**

This is one of the ways in which this task can be performed. In this, we slice
string on every Kth occurrence using string slicing and append character
between them.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Insert character after every K elements

# Using loop + string slicing

 

 

# Function to Insert character

# in each duplicate string

# after every K elements

def insertCharacterAfterKelements(test_str, K, char):

 res = []

 # using loop to iterate

 for idx in range(0, len(test_str), K):

 

 # appending all the results

 res.append(test_str[:idx] + char + test_str[idx:])

 

 return str(res)

 

 

# Driver Code

# initializing string

input_str = 'GeeksforGeeks'

 

# printing original string

print("The original string is : " + str(input_str))

 

# initializing K

K = 2

 

# initializing add char

add_chr = ";"

 

# printing result

print("The extracted strings : " +

 insertCharacterAfterKelements(input_str, K, add_chr))  
  
---  
  
 __

 __

 **Output:**

> The original string is : GeeksforGeeks  
> The extracted strings : [‘;GeeksforGeeks’, ‘Ge;eksforGeeks’,
> ‘Geek;sforGeeks’, ‘Geeksf;orGeeks’, ‘Geeksfor;Geeks’, ‘GeeksforGe;eks’,
> ‘GeeksforGeek;s’]

 **Method #2 : Using list comprehension + string slicing**

This is yet another way in which this task can be performed. In this, we
perform similar task as loop difference being that list comprehension is
employed as shorthand to solve this question.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Insert character after every K elements

# Using list comprehension + string slicing

 

 

# Function to Insert character

# in each duplicate string

# after every K elements

def insertCharacterAfterKelements(test_str, K, char):

 # list comprehension to bind logic in one.

 res = [test_str[:idx] + char + test_str[idx:]

 for idx in range(0, len(test_str), K)]

 

 return str(res)

 

 

# Driver Code

# initializing string

input_str = 'GeeksforGeeks'

 

# printing original string

print("The original string is : " + str(input_str))

 

# initializing K

K = 2

 

# initializing add char

add_chr = ";"

 

# printing result

print("The extracted strings : " +

 insertCharacterAfterKelements(input_str, K, add_chr))  
  
---  
  
 __

 __

 **Output:**

> The original string is : GeeksforGeeks  
> The extracted strings : [‘;GeeksforGeeks’, ‘Ge;eksforGeeks’,
> ‘Geek;sforGeeks’, ‘Geeksf;orGeeks’, ‘Geeksfor;Geeks’, ‘GeeksforGe;eks’,
> ‘GeeksforGeek;s’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

