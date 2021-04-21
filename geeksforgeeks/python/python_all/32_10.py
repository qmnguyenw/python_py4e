Python – Convert String to matrix having K characters per row



Given a String, convert it to Matrix, having K characters in each row.

>  **Input** : test_str = ‘GeeksforGeeks is best’, K = 7  
> **Output** : [[‘G’, ‘e’, ‘e’, ‘k’, ‘s’, ‘f’, ‘o’], [‘r’, ‘G’, ‘e’, ‘e’, ‘k’,
> ‘s’, ‘ ‘], [‘i’, ‘s’, ‘ ‘, ‘b’, ‘e’, ‘s’, ‘t’]]  
> **Explanation** : Each character is assigned to 7 element row in matrix.
>
>  **Input** : test_str = ‘GeeksforGeeks ‘, K = 7  
> **Output** : [[‘G’, ‘e’, ‘e’, ‘k’, ‘s’, ‘f’, ‘o’], [‘r’, ‘G’, ‘e’, ‘e’, ‘k’,
> ‘s’, ‘ ‘]]  
> **Explanation** : Each character is assigned to 7 element row in matrix.  
>

**Method #1 : Using list comprehension + slicing**

The combination of above functionalities can be used to solve this problem. In
this, we first extract separate strings for each row using slicing and list
comprehension. Then convert each string to character list using _list()_.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert String to K characters row Matrix

# Using list comprehension + slicing

 

 

# Function to Convert String

# to K characters row Matrix

def convertToMatrix(test_str, K):

 # slicing strings

 temp = [test_str[idx: idx + K] for idx in range(0,
len(test_str), K)]

 

 # conversion to list of characters

 res = [list(ele) for ele in temp]

 

 # printing result

 print("The converted Matrix : " + str(res))

 

 

# Driver Code 

# initializing string

input_str = 'GeeksforGeeks is best'

 

# printing original string

print("The original string is : " + str(input_str))

 

# initializing K

K = 7

 

# calling the function

convertToMatrix(input_str, K)  
  
---  
  
 __

 __

 **Output:**

> The original string is : GeeksforGeeks is best  
> The converted Matrix : [[‘G’, ‘e’, ‘e’, ‘k’, ‘s’, ‘f’, ‘o’], [‘r’, ‘G’, ‘e’,
> ‘e’, ‘k’, ‘s’, ‘ ‘], [‘i’, ‘s’, ‘ ‘, ‘b’, ‘e’, ‘s’, ‘t’]]

 **Method #2 : Using list comprehension + map() + slicing**

This is yet another way in which this task can be performed. In this, we
perform task in similar way as above functions, difference being conversion to
list is done using _map()_ rather than list comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert String to K characters row Matrix

# Using list comprehension + map() + slicing

 

 

# Function to Convert String

# to K characters row Matrix

def convertToMatrix(test_str, K):

 # slicing strings

 temp = [test_str[idx: idx + K] for idx in range(0,
len(test_str), K)]

 

 # conversion using map

 res = list(map(lambda ele: list(ele), temp))

 

 # printing result

 print("The converted Matrix : " + str(res))

 

 

# Driver Code

# initializing string

input_str = 'GeeksforGeeks is best'

 

# printing original string

print("The original string is : " + str(input_str))

 

# initializing K

K = 7

 

# calling the function

convertToMatrix(input_str, K)  
  
---  
  
 __

 __

 **Output:**

> The original string is : GeeksforGeeks is best  
> The converted Matrix : [[‘G’, ‘e’, ‘e’, ‘k’, ‘s’, ‘f’, ‘o’], [‘r’, ‘G’, ‘e’,
> ‘e’, ‘k’, ‘s’, ‘ ‘], [‘i’, ‘s’, ‘ ‘, ‘b’, ‘e’, ‘s’, ‘t’]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

