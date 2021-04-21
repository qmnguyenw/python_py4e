Python Program to Print all Integers that Aren’t Divisible by Either 2 or 3



We can input a set of integer, and check which integers in this range,
beginning with 1 are not divisible by 2 or 3, by checking the remainder of the
integer with 2 and 3.

**Example:**

    
    
     **Input:** 10
    **Output:** Numbers not divisible by 2 and 3
    1
    5
    7
    

**Method 1** : We check if the number is not divisible by 2 and 3 using the
and clause, then outputs the number.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# input the maximum number to

# which you want to send

max_num = 20

 

# starting numbers from 0

n = 1

 

# run until it reaches maximum number

print("Numbers not divisible by 2 and 3")

while n <= max_num:

 

 # check if number is divisible by 2 and 3

 if n % 2 != 0 and n % 3 != 0:

 print(n)

 

 # incrementing the counter

 n = n+1  
  
---  
  
 __

 __

 **Output:**

    
    
    Numbers not divisible by 2 and 3
    1
    5
    7
    11
    13
    17
    19

 **Method 2** : We traverse the odd numbers starting with 1 since even numbers
are divisible by 2. So, we increment the for a loop by 2, traversing only odd
numbers and check, which one of them is not divisible by 3. This approach is
better than the previous one since it only iterates through half the number of
elements in the specified range.

  

  

The following Python code illustrates this :

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# input the maximum number to

# which you want to send

max_num = 40

print("Numbers not divisible by 2 or 3 : ")

 

# run until it reaches maximum number

# we increment the loop by +2 each time,

# since odd numbers are not divisible by 2

for i in range(1, max_num, 2):

 

 # check if number is not divisible by 3

 if i % 3 != 0:

 print(i)  
  
---  
  
 __

 __

 **Output:**

    
    
    Numbers not divisible by 2 or 3 : 
    1
    5
    7
    11
    13
    17
    19
    23
    25
    29
    31
    35
    37
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

