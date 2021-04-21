Python program to print negative numbers in a list



Given a list of numbers, write a Python program to print all negative numbers
in given list.

 **Example:**

    
    
     **Input:** list1 = [12, -7, 5, 64, -14]
    **Output:** -7, -14
    
    **Input:** list2 = [12, 14, -95, 3]
    **Output:** -95

 **Example #1:** Print all negative numbers from given list using for loop

Iterate each element in the list using for loop and check if number is less
than 0. If the condition satisfies, then only print the number.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to print negative Numbers in a List

 

# list of numbers

list1 = [11, -21, 0, 45, 66, -93]

 

# iterating each number in list

for num in list1:

 

 # checking condition

 if num < 0:

 print(num, end = " ")  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    -21 -93 

  
**Example #2:** Using while loop

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to print negative Numbers in a List

 

# list of numbers

list1 = [-10, 21, -4, -45, -66, 93]

num = 0

 

# using while loop 

while(num < len(list1)):

 

 # checking condition

 if list1[num] < 0:

 print(list1[num], end = " ")

 

 # increment num 

 num += 1

   
  
---  
  
__

__

**Output:**

    
    
    -10 -4 -45 -66 

  
**Example #3:** Using list comprehension

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to print negative Numbers in a List

 

# list of numbers

list1 = [-10, -21, -4, 45, -66, 93]

 

# using list comprehension

neg_nos = [num for num in list1 if num < 0]

 

print("Negative numbers in the list: ", *neg_nos)  
  
---  
  
 __

 __

 **Output:**

    
    
    Negative numbers in the list:  -10 -21 -4 -66

  
**Example #4:** Using lambda expressions

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to print negative Numbers in a List

 

# list of numbers 

list1 = [-10, 21, 4, -45, -66, 93,
-11] 

 

 

# we can also print negative no's using lambda exp. 

neg_nos = list(filter(lambda x: (x < 0), list1))

 

print("Negative numbers in the list: ", *neg_nos)   
  
---  
  
__

__

**Output:**

    
    
    Negative numbers in the list:  -10 -45 -66 -11

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

