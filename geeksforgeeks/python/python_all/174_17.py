Python program to print all odd numbers in a range



Given starting and end points, write a Python program to print all odd numbers
in that given range.

 **Example:**

    
    
     **Input:** start = 4, end = 15
    **Output:** 5, 7, 9, 11, 13, 15
    
    **Input:** start = 3, end = 11
    **Output:** 3, 5, 7, 9, 11

 **Example #1:** Print all odd numbers from given list using for loop

Define start and end limit of range. Iterate from start till the range in the
list using for loop and check if num % 2 != 0. If the condition satisfies,
then only print the number.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to print odd Numbers in given range

 

start, end = 4, 19

 

# iterating each number in list

for num in range(start, end + 1):

 

 # checking condition

 if num % 2 != 0:

 print(num, end = " ")  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    5 7 9 11 13 15 17 19 

  
**Example #2:** Taking range limit from user input

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to print Even Numbers in given range

 

start = int(input("Enter the start of range: "))

end = int(input("Enter the end of range: "))

 

# iterating each number in list

for num in range(start, end + 1):

 

 # checking condition

 if num % 2 != 0:

 print(num, end = " ")  
  
---  
  
 __

 __

 **Output:**

    
    
    Enter the start of range: 3
    Enter the end of range: 11
    3 5 7 9 11 

  
**Example #3:** Taking range limit from user input

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to print Even Numbers in given range

 

start = int(input("Enter the start of range: "))

end = int(input("Enter the end of range: "))

 

#create a list that contains only Even numbers in given range

even_list = range(start, end + 1)[start%2::2]

 

for num in even_list:

 print(num, end = " ")  
  
---  
  
 __

 __

 **Output:**

    
    
    Enter the start of range: 3
    Enter the end of range: 11
    3 5 7 9 11 

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

