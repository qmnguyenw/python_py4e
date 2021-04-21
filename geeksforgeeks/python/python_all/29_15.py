Python program to convert String to K sized Numerical Rows



Given a string of alphabets, convert it to K sized numerical rows, which
contains the number being the positional value of characters.

>  **Input** : test_str = ‘geeksforgeek’, K = 4  
> **Output** : [[6, 4, 4, 10], [18, 5, 14, 17], [6, 4, 4, 10]]  
> **Explanation** : g is at 6th position in alphabet hence g→ 6 and the string
> is split after every fourth character
>
>  **Input** : test_str = ‘geeksforgeek’, K = 3  
> **Output** : [[6, 4, 4], [10, 18, 5], [14, 17, 6], [4, 4, 10]]  
> **Explanation** : g is at 6th position in alphabet hence g→ 6 and the string
> is split after every third character  
>

**Method 1 : Using loop +** **index()**

In this, we perform an iteration of each character using a loop and fetch the
required position of the character in alphabets using index() on an ordered
character list.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing string

test_str = 'geeksforgeekscse'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing K

K = 4

 

alphabs = "abcdefghijklmnopqrstuvwxyz"

 

res = []

temp = []

for ele in test_str:

 

 # finding numerical position using index()

 temp.append(alphabs.index(ele))

 

 # regroup on K

 if len(temp) == K:

 res.append(temp)

 temp = []

 

# appending remaining characters

if temp != []:

 res.append(temp)

 

# printing result

print("Grouped and Converted String : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original string is : geeksforgeekscse  
> Grouped and Converted String : [[6, 4, 4, 10], [18, 5, 14, 17], [6, 4, 4,
> 10], [18, 2, 18, 4]]

 **Method #2 : Using ljust() + ord() + list comprehension**

In this, we perform the task of padding is required to have equal length rows
using ljust(), then get numerical alphabetic positions using ord(), list
comprehension with slicing helps to convert the list to K chunked Matrix.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from math import ceil

 

# initializing string

test_str = 'geeksforgeekscse'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing K

K = 4

 

# filling the rear to K size rows

temp = test_str.ljust(ceil(len(test_str) / K) * K)

 

# convert to numerical characters

temp = [0 if char == ' ' else (ord(char) - 97)
for char in temp]

 

# slice and render to matrix

res = [temp[idx: idx + K] for idx in range(0,
len(temp), K)]

 

# printing result

print("Grouped and Converted String : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original string is : geeksforgeekscse  
> Grouped and Converted String : [[6, 4, 4, 10], [18, 5, 14, 17], [6, 4, 4,
> 10], [18, 2, 18, 4]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

