Python program to count Even and Odd numbers in a List



Given a list of numbers, write a Python program to count Even and Odd numbers
in a List.

Example:

    
    
    Input: list1 = [2, 7, 5, 64, 14]
    Output: Even = 3, odd = 2
    
    Input: list2 = [12, 14, 95, 3]
    Output: Even = 2, odd = 2

Example 1: count Even and Odd numbers from given list using for loop

Iterate each element in the list using for loop and check if num % 2 == 0, the
condition to check even numbers. If the condition satisfies, then increase
even count else increase odd count.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to count Even

# and Odd numbers in a List

 

# list of numbers

list1 = [10, 21, 4, 45, 66, 93, 1]

 

even_count, odd_count = 0, 0

 

# iterating each number in list

for num in list1:

 

 # checking condition

 if num % 2 == 0:

 even_count += 1

 

 else:

 odd_count += 1

 

print("Even numbers in the list: ", even_count)

print("Odd numbers in the list: ", odd_count)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Even numbers in the list:  3
    Odd numbers in the list:  4
    

