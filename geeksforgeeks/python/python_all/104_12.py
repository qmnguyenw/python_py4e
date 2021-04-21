Python Program to Swap Two Variables



Given two variables x and y, write a Python program to swap their values.
Let’s see different methods in Python to do this task.

![python-swap-two-variable](https://media.geeksforgeeks.org/wp-
content/uploads/20200110142212/python-swap-two-variable.png)

 **Method 1:** Using Naive approach

The most naive approach is to store the value of one variable(say x) in a
temporary variable, then assigning the variable x with the value of variable
y. Finally, assign the variable y with the value of the temporary variable.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# swapping of two variables

 

x = 10

y = 50

 

# Swapping of two variables

# Using third variable

temp = x

x = y

y = temp

 

print("Value of x:", x)

print("Value of y:", y)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Value of x: 50
    Value of y: 10
    

**Method 2:** Using comma operator

Using the comma operator the value of variables can be swapped without using a
third variable.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# swapping of two variables

 

 

x = 10

y = 50

 

# Swapping of two variables 

# without using third variable

x, y = y, x

 

print("Value of x:", x)

print("Value of y:", y)  
  
---  
  
 __

 __

 **Output:**

    
    
    Value of x: 50
    Value of y: 10
    

**Method 3:** Using XOR

The bitwise XOR operator can be used to swap two variables. The XOR of two
numbers x and y returns a number which has all the bits as 1 wherever bits of
x and y differ. For example XOR of 10 (In Binary 1010) and 5 (In Binary 0101)
is 1111 and XOR of 7 (0111) and 5 (0101) is (0010).

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# Swapping of two variables

 

x = 10

y = 50

 

# Swapping using xor

x = x ^ y

y = x ^ y

x = x ^ y

 

print("Value of x:", x)

print("Value of y:", y)  
  
---  
  
 __

 __

 **Output:**

    
    
    Value of x: 50
    Value of y: 10
    

**Method 4:** Using arithmetic operators

The idea is to get sum in one of the two given numbers. The numbers can then
be swapped using the sum and subtraction from sum.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# swapping of two variables

 

x = 10

y = 50

 

# Swapping of two variables

# using arithmetic operations

x = x + y 

y = x - y 

x = x - y 

 

print("Value of x:", x)

print("Value of y:", y)  
  
---  
  
 __

 __

 **Output:**

    
    
    Value of x: 50
    Value of y: 10
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

