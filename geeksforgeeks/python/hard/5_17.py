Python Program to swap two numbers without using third variable



Given two variables n1 and n2. The task is to swap the values of both the
variables without using third variable.  
 **Examples:**  

    
    
    **X :** 10
    **Y :** 20
     
    After swapping X and Y, we get :
    
    **X :** 20
    **Y :** 10
    
    
    
    
    
    **A :** 'Hello'
    **B :** 'World'
      
    After swapping A and B, we get : 
    
    **A :** 'World'
    **B :** 'Hello'
    
    
    

**Method 1 :- Using simple built-in method**  

    
    
    left , right = right , left 
    
    
    

This method works for any data type values like string, int, float and is easy
to use.  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to swap two numbers

# without using another variable

x = 5

y = 7

print ("Before swapping: ")

print("Value of x : ", x, " and y : ", y)

# code to swap 'x' and 'y'

x, y = y, x

print ("After swapping: ")

print("Value of x : ", x, " and y : ", y)  
  
---  
  
 __

 __

 **Output:**  

  

  

    
    
    Before swapping: 
    Value of x :  5  and y :  7
    After swapping: 
    Value of x :  7  and y :  5    
    
    
    

**Method 2 :- Using Bitwise XOR operator**  

    
    
    x ^= y
    y ^= x
    x ^= y
    
    
    

This method only works for integers and works faster because this method uses
bit operation (for same values, output = 0 and for different values, output =
1) .  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to swap two numbers

# using Bitwise XOR method

x = 5 # x = 0101

y = 10 # y = 1010

print ("Before swapping: ")

print("Value of x : ", x, " and y : ", y)

# Swap code

x ^= y # x = 1111, y = 1010

y ^= x # y = 0101, x = 1111

x ^= y # x = 1010, y = 0101

print ("After swapping: ")

print("Value of x : ", x, " and y : ", y)  
  
---  
  
 __

 __

 **Output:**  

    
    
    Before swapping: 
    Value of x :  5  and y :  10
    After swapping: 
    Value of x :  10  and y :  5
    
    
    

**Method 3 :- Using Addition and Subtraction Operators**  

    
    
    x = x + y 
    y = x - y
    x = x - y
    
    
    

This method works for variables that have numeric values.  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to swap two numbers

# using + and - operators

x = 5.4

y = 10.3

print ("Before swapping: ")

print("Value of x : ", x, " and y : ", y)

# Swap code

x = x + y # x = 15.7, y = 10.3

y = x - y # x = 15.7, y = 5.4

x = x - y # x = 10.3, y = 5.4

print ("After swapping: ")

print("Value of x : ", x, " and y : ", y)  
  
---  
  
 __

 __

 **Output:**  

    
    
    Before swapping: 
    Value of x :  5.4  and y :  10.3
    After swapping: 
    Value of x :  10.3  and y :  5.4
    
    
    

**Method 4 :- Using Division and Multiplication Operators**  

    
    
    x = x * y
    y = x / y
    x = x / y
    
    
    

This method works for variables that have numeric values other than 0 .  

  

  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to swap two numbers

# using / and * operators

x = 5.4

y = 10.3

print ("Before swapping: ")

print("Value of x : ", x, " and y : ", y)

# Swap code

x = x * y # x = 55.62, y = 10.3

y = x / y # x = 55.62, y = 5.4

x = x / y # x = 10.3, y = 5.4

print ("After swapping: ")

print("Value of x : ", x, " and y : ", y)  
  
---  
  
 __

 __

 **Output:**  

    
    
    Before swapping: 
    Value of x :  5.4  and y :  10.3
    After swapping: 
    Value of x :  10.3  and y :  5.4
    
    
    

**Method 4: Using both bitwise operators and arithmetic operators:**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# python program to swap two numbers

# using bitwise addition for swapping

 

x = 5;

y = 10;

 

print ("Before swapping: ") ;

print("Value of x : ", x, " and y : ", y) ;

 

# same as x = x + y

x = (x & y) + (x|y) ;

 

#vsame as y = x - y

y = x + (~y) + 1 ;

 

# same as x = x - y

x = x + (~y) + 1 ;

 

print ("After swapping: ")

print("Value of x : ", x, " and y : ", y)

# This code is contributed by bunnyram19  
  
---  
  
 __

 __

 **Output:**

    
    
    Before swapping: 
    Value of x :  5  and y :  10
    After swapping: 
    Value of x :  10  and y :  5
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

