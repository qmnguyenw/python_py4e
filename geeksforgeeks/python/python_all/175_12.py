Python program to find smallest number in a list



Given a list of numbers, the task is to write a Python program to find the
smallest number in given list.  
Examples:

    
    
    Input : list1 = [10, 20, 4]
    Output : 4
    
    Input : list2 = [20, 10, 20, 1, 100]
    Output : 1

Method 1 : Sort the list in ascending order and print the first element in the
list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to find smallest

# number in a list

# list of numbers

list1 = [10, 20, 4, 45, 99]

# sorting the list

list1.sort()

# printing the first element

print("Smallest element is:", *list1[:1])  
  
---  
  
 __

 __

 **Output:**

    
    
    smallest element is: 4

Method 2 : Using min() method

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to find smallest

# number in a list

# list of numbers

list1 = [10, 20, 1, 45, 99]

# printing the maximum element

print("Smallest element is:", min(list1))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Smallest element is: 1

Method 3 : Find min list element on inputs provided by user.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to find smallest

# number in a list

# creating empty list

list1 = []

# asking number of elements to put in list

num = int(input("Enter number of elements in list: "))

# iterating till num to append elements in list

for i in range(1, num + 1):

 ele= int(input("Enter elements: "))

 list1.append(ele)

 

# print maximum element

print("Smallest element is:", min(list1))  
  
---  
  
 __

 __

 **Output:**

    
    
    Enter number of elements in list: 4
    Enter elements: 12
    Enter elements: 19
    Enter elements: 11
    Enter elements: 99
    Smallest element is: 11

Method 4: Find the smallest element in list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to find smallest

# number in a list

l=[ int(l) for l in input("List:").split(",")]

print("The list is ",l)

# Assign first element as a minimum.

min1 = l[0]

for i in range(len(l)):

 # If the other element is min than first element

 if l[i] < min1:

 min1 = l[i] #It will change

print("The smallest element in the list is ",min1)  
  
---  
  
 __

 __

 **Input:**

    
    
    List: 23,-1,45,22.6,78,100,-5

 **Output:**

    
    
    The list is ['23', '-1', '45', '22.6', '78', '100','-5']
    The smallest element in the list is  -5

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

