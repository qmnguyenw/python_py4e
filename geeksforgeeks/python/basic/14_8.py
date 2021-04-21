Python | Get a list as input from user



We often encounter a situation when we need to take number/string as input
from the user. In this article, we will see how to get as input a list from
the user.

 **Examples:**

    
    
     **Input :** n = 4,  ele = 1 2 3 4
    **Output :**  [1, 2, 3, 4]
    
    **Input :** n = 6, ele = 3 4 1 7 9 6
    **Output :** [3, 4, 1, 7, 9, 6]
    

**Code #1:** Basic example

 __

 __  
 __

 __

 __  
 __  
 __

# creating an empty list

lst = []

 

# number of elemetns as input

n = int(input("Enter number of elements : "))

 

# iterating till the range

for i in range(0, n):

 ele = int(input())

 

 lst.append(ele) # adding the element

 

print(lst)  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/list_input1.png)

  
**Code #2:** With handling exception

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# try block to handle the exception

try:

 my_list = []

 

 while True:

 my_list.append(int(input()))

 

# if the input is not-integer, just print the list

except:

 print(my_list)  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/list_input2.png)  
  
**Code #3:** Using map()

 __

 __  
 __

 __

 __  
 __  
 __

# number of elements

n = int(input("Enter number of elements : "))

 

# Below line read inputs from user using map() function 

a = list(map(int,input("\nEnter the numbers :
").strip().split()))[:n]

 

print("\nList is - ", a)  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/list_input3.png)  
  
**Code #4:** List of lists as input

 __

 __  
 __

 __

 __  
 __  
 __

lst= [ ]

n = int(input("Enter number of elements : "))

 

for i in range(0, n):

 ele = [input(), int(input())]

 lst.append(ele)

 

print(lst)  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/list_input4.png)

 **Code #5:** Using List Comprehension and Typecasting

 __

 __  
 __

 __

 __  
 __  
 __

# For list of integers

lst1 = [] 

 

# For list of strings/chars

lst2 = [] 

 

lst1 = [int(item) for item in input("Enter the list items
: ").split()]

 

lst2 = [item for item in input("Enter the list items :
").split()]

 

print(lst1)

print(lst2)  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200429190208/2020-04-29-300x128.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

