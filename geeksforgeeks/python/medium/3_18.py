How to iterate through a nested List in Python?



In this article, we are going to see how to iterate through a nested List. A
list can be used to store multiple Data types such as Integers, Strings,
Objects, and also **another List within itself**. This **sub-list** which is
within the list is what is commonly known as the Nested List.

## Iterating through a Nested List

Lets us see how a typical nested list looks like :

![list=\[10, 20, 30, 40, \[ 80,60, 70 \] \]](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-262edd8187fe178ada23c5e6df0a2d7e_l3.png)

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201202205027/Screenshot20201202205006.png)

There are multiple ways to iterate through a Nested List:

  

  

 **Method 1:** Use of the index to iterate through the list

 **Use of Positive Index:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# code

list = [10, 20, 30, 40, [80, 60, 70]]

 

# Printing sublist at index 4

print(list[4])

 

# Printing 1st element of the sublist

print(list[4][0])

 

# Printing 2nd element of the sublist

print(list[4][1])

 

# Printing 3rd element of the sublist

print(list[4][2])  
  
---  
  
 __

 __

 **Output:**

    
    
    [80, 60, 70]
    80
    60
    70

 **Use of Negative Index**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# code

list = [10, 20, 30, 40, [80, 60, 70]]

 

# Printing sublist at index 4

print(list[-1])

 

# Printing 1st element of the sublist

print(list[-1][-3])

 

# Printing 2nd element of the sublist

print(list[-1][-2])

 

# Printing 3rd element of the sublist

print(list[-1][-1])  
  
---  
  
 __

 __

 **Output:**

    
    
    [80, 60, 70]
    80
    60
    70

 **Method 2:** Use of loop to iterate through the list

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201203054151/Screenshot20201203054119.png)  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# code

# LIST

list = [["Rohan", 60], ["Aviral", 21], 

 ["Harsh", 30], ["Rahul", 40],

 ["Raj", 20]]

 

# looping through nested list using indexes

for names in list:

 print(names[0], "is", names[1],

 "years old.")  
  
---  
  
 __

 __

 **Output:**

    
    
    Rohan is 60 years old.
    Aviral is 21 years old.
    Harsh is 30 years old.
    Rahul is 40 years old.
    Raj is 20 years old.

 **Use of Temporary Variables inside a loop.**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# code

# LIST

list = [["Rohan", 60], ["Aviral", 21], 

 ["Harsh", 30], ["Rahul", 40],

 ["Raj", 20]]

 

# looping through nested list using multiple 

# temporary variables

for name, age in list:

 print(name, "is",

 age, "years old.")  
  
---  
  
 __

 __

 **Output:**

    
    
    Rohan is 60 years old.
    Aviral is 21 years old.
    Harsh is 30 years old.
    Rahul is 40 years old.
    Raj is 20 years old.

 **Method 3:** Use of Slicing

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# code

# list

list = [10, 20, 30, 40,

 [80, 60, 70]]

 

# print the entire Sublist at index 4

print(list[4][:])

 

# printing first two element

print(list[4][0 : 2])  
  
---  
  
 __

 __

 **Output:**

    
    
    [80, 60, 70]
    [80, 60]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

