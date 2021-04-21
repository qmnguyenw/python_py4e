Python program to find the sum of Characters ascii values in String List



Given the string list, the task is to write a Python program to compute the
summation value of each character’s ASCII value.

 **Examples:**

>  **Input** : test_list = [“geeksforgeeks”, “teaches”, “discipline”]  
> **Output** : [133, 61, 100]  
> **Explanation** : Positional character summed to get required values.
>
>  **Input** : test_list = [“geeksforgeeks”, “discipline”]  
> **Output** : [133, 100]  
> **Explanation** : Positional character summed to get required values.

**Method 1 : Using** **ord()** **+** **loop**

  

  

In this, we iterate each character in each string and keep on adding
positional values to get its sum. The summed value is appended back to the
result in a list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Characters Positions Summation in String List

# Using ord() + loop

 

# initializing list

test_list = ["geeksforgeeks",

 "teaches", "us", "discipline"]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = []

for sub in test_list:

 ascii_sum = 0

 

 # getting ascii value sum 

 for ele in sub :

 ascii_sum += (ord(ele) - 96)

 

 res.append(ascii_sum)

 

# printing result 

print("Position Summation List : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘geeksforgeeks’, ‘teaches’, ‘us’, ‘discipline’]  
> Position Summation List : [133, 61, 40, 100]

 **Method 2 : Using** **list comprehension** **+** **sum()** **\+ ord()**

In this, we get summation using sum(), ord() is used to get the ASCII
positional value, and list comprehension offers one-liner solution to this
problem.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Characters Positional Summation in String List

# Using list comprehension + sum() + ord()

 

# initializing list

test_list = ["geeksforgeeks", "teaches", 

 "us", "discipline"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# sum() gets summation, list comprehension

# used to perform task in one line 

res = [sum([ord(ele) - 96 for ele in sub]) for
sub in test_list]

 

# printing result 

print("Positional Summation List : " + str(res))  
  
---  
  
 __

 __

**Output:**

> The original list is : [‘geeksforgeeks’, ‘teaches’, ‘us’, ‘discipline’]  
> Position Summation List : [133, 61, 40, 100]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

