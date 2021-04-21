Python program to find largest number in a list



Given a list of numbers, the task is to write a Python program to find the
largest number in given list.

Examples:

    
    
    Input : list1 = [10, 20, 4]
    Output : 20
    
    Input : list2 = [20, 10, 20, 4, 100]
    Output : 100

Method 1 : Sort the list in ascending order and print the last element in the
list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to find largest

# number in a list

 

# list of numbers

list1 = [10, 20, 4, 45, 99]

 

# sorting the list

list1.sort()

 

# printing the last element

print("Largest element is:", list1[-1])  
  
---  
  
 __

 __

Output:

    
    
    Largest element is: 99

Method 2 : Using max() method

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to find largest

# number in a list

 

# list of numbers

list1 = [10, 20, 4, 45, 99]

 

 

# printing the maximum element

print("Largest element is:", max(list1))  
  
---  
  
 __

 __

Output:

    
    
    Largest element is: 99

Method 3 : Find max list element on inputs provided by user

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to find largest

# number in a list

 

# creating empty list

list1 = []

 

# asking number of elements to put in list

num = int(input("Enter number of elements in list: "))

 

# iterating till num to append elements in list

for i in range(1, num + 1):

 ele = int(input("Enter elements: "))

 list1.append(ele)

 

# print maximum element

print("Largest element is:", max(list1))  
  
---  
  
 __

 __

Output:

    
    
    Enter number of elements in list: 4
    Enter elements: 12
    Enter elements: 19
    Enter elements: 1
    Enter elements: 99
    Largest element is: 99

Method 4 : Without using built in functions in python:

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to find largest

# number in a list

 

def myMax(list1):

 

 # Assume first number in list is largest

 # initially and assign it to variable "max"

 max = list1[0]

 

 # Now traverse through the list and compare 

 # each number with "max" value. Whichever is 

 # largest assign that value to "max'.

 for x in list1:

 if x > max :

 max = x

 

 # after complete traversing the list 

 # return the "max" value

 return max

 

 

# Driver code

list1 = [10, 20, 4, 45, 99]

print("Largest element is:", myMax(list1))  
  
---  
  
 __

 __

Output:

    
    
    Largest element is: 99

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

