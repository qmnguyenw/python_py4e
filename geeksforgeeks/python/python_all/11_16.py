Python Program to Flatten a Nested List using Recursion



Given a nested list, the task is to write a python program to flatten a nested
list using recursion.

 **Examples:**

>  **Input:** [[8, 9], [10, 11, ‘geeks’], [13]]
>
>  **Output:** [8, 9, 10, 11, ‘geeks’, 13]
>
>  **Input:** [[‘A’, ‘B’, ‘C’], [‘D’, ‘E’, ‘F’]]
>
>  
>
>
>  
>
>
>  **Output:** [‘A’, ‘B’, ‘C’, ‘D’, ‘E’, ‘F’]

 **Step-by-step Approach:**

  * Firstly, we try to initialize a variable into the linked list.
  * Then, our next task is to pass our list as an argument to a recursive function for flattening the list.
  * In that recursive function, if we find the list as empty then we return the list.
  * Else, we call the function in recursive form along with its sublists as parameters until the list gets flattened.
  * Then finally, we will print the flattened list as output.

 **Below are some python programs based on the above approach:**

 **Example 1:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to flatten a nested list

 

# explict function to flatten a

# nested list

def flattenList(nestedList):

 

 # check if list is empty

 if not(bool(nestedList)):

 return nestedList

 

 # to check instance of list is empty or not

 if isinstance(nestedList[0], list):

 

 # call function with sublist as argument

 return flattenList(*nestedList[:1]) +
flattenList(nestedList[1:])

 

 # call function with sublist as argument

 return nestedList[:1] + flattenList(nestedList[1:])

 

 

# Driver Code

nestedList = [[8, 9], [10, 11, 'geeks'], [13]]

print('Nested List:\n', nestedList)

 

print("Flattened List:\n", flattenList(nestedList))  
  
---  
  
 __

 __

 **Output:**

    
    
    Nested List:
     [[8, 9], [10, 11, 'geeks'], [13]]
    Flattened List:
     [8, 9, 10, 11, 'geeks', 13]

 **Example 2:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to flatten a nested list

 

# explict function to flatten a

# nested list

def flattenList(nestedList):

 

 # check if list is empty

 if not(bool(nestedList)):

 return nestedList

 

 # to check instance of list is empty or not

 if isinstance(nestedList[0], list):

 

 # call function with sublist as argument

 return flattenList(*nestedList[:1]) +
flattenList(nestedList[1:])

 

 # call function with sublist as argument

 return nestedList[:1] + flattenList(nestedList[1:])

 

 

# Driver Code

nestedList = [['A', 'B', 'C'], ['D', 'E', 'F']]

print('Nested List:\n', nestedList)

 

print("Flattened List:\n", flattenList(nestedList))  
  
---  
  
 __

 __

 **Output:**

    
    
    Nested List:
     [['A', 'B', 'C'], ['D', 'E', 'F']]
    Flattened List:
     ['A', 'B', 'C', 'D', 'E', 'F']

 **Example 3:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to flatten a nested list

 

# explict function to flatten a

# nested list

def flattenList(nestedList):

 

 # check if list is empty

 if not(bool(nestedList)):

 return nestedList

 

 # to check instance of list is empty or not

 if isinstance(nestedList[0], list):

 

 # call function with sublist as argument

 return flattenList(*nestedList[:1]) +
flattenList(nestedList[1:])

 

 # call function with sublist as argument

 return nestedList[:1] + flattenList(nestedList[1:])

 

 

# Driver Code

nestedList = [[1], [2], [3], [4], [5]]

print('Nested List:\n', nestedList)

 

print("Flattened List:\n", flattenList(nestedList))  
  
---  
  
 __

 __

 **Output:**

    
    
    Nested List:
     [[1], [2], [3], [4], [5]]
    Flattened List:
     [1, 2, 3, 4, 5]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

