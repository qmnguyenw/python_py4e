Python | Check if any element occurs n times in given list



Given a list, the task is to find whether any element occurs ‘n’ times in
given list of integers. It will basically check for the first element that
occurs n number of times.  
**Examples:**  

    
    
    **Input:** l =  [1, 2, 3, 4, 0, 4, 3, 2, 1, 2], n = 3
    **Output :** 2
    
    **Input:** l =  [1, 2, 3, 4, 0, 4, 3, 2, 1, 2, 1, 1], n = 4
    **Output :** 1
    
    
    

Below are some methods to do the task in Python –  
**Method 1: Using Simple Iteration and Sort**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to find occurrence of any element

# appearing 'n' times

# Input Initialisation

input = [1, 2, 3, 0, 4, 3, 4, 0, 0]

# Sort Input

input.sort()

# Constants Declaration

n = 3

prev = -1

count = 0

flag = 0

# Iterating

for item in input:

 if item == prev:

 count = count + 1

 else:

 count = 1

 prev = item

 

 if count == n:

 flag = 1

 print("There are {} occurrences of {} in {}".format(n, item,
input))

 break

# If no element is not found.

if flag == 0:

 print("No occurrences found")  
  
---  
  
 __

 __

 **Output :**  

    
    
    There are 3 occurrences of 0 in [0, 0, 0, 1, 2, 3, 3, 4, 4]
    
    

  
**Method 2: Using Count**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to find occurrence of any element

# appearing 'n' times

# Input list initialisation

input = [1, 2, 3, 4, 0, 4, 3, 4]

# Constant declaration

n = 3

# print

print("There are {} occurrences of {} in
{}".format(input.count(n), n, input))  
  
---  
  
 __

 __

 **Output :**  

  

  

    
    
    There are 2 occurrences of 3 in [1, 2, 3, 4, 0, 4, 3, 4]
    
    

  
**Method 3: Using defaultdict**  
We first populate item of list in a dictionary and then we find whether count
of any element is equal to n.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to find occurrence of any element

# appearing 'n' times

# importing

from collections import defaultdict

# Dictionary declaration

dic = defaultdict(int)

# Input list initialisation

Input = [9, 8, 7, 6, 5, 9, 2]

# Dictionary populate

for i in Input:

 dic[i]+= 1

# constant declaration

n = 2

flag = 0

# Finding from dictionary

for element in Input:

 if element in dic.keys() and dic[element] == n:

 print("Yes, {} has {} occurrence in {}.".format(element, n,
Input))

 flag = 1

 break

# if element not found.

if flag == 0:

 print("No occurrences found")  
  
---  
  
 __

 __

 **Output :**  

    
    
    Yes, 9 has 2 occurrence in [9, 8, 7, 6, 5, 9, 2]
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

