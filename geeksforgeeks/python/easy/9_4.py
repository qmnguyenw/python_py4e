Benefits of Double Division Operator over Single Division Operator in Python



The Double Division operator in Python returns the floor value for both
integer and floating-point arguments after division.

 __

 __  
 __

 __

 __  
 __  
 __

# A Python program to demonstrate use of

# "//" for both integers and floating points

 

print(5//2)

print(-5//2)

print(5.0//2)  
  
---  
  
 __

 __

 **Output:**

    
    
    2
    -3
    2.0

The single division operator behaves abnormally generally for very large
numbers. Consider the following example.

 **Examples 1:**

 __

 __  
 __

 __

 __  
 __  
 __

# single division

print(1000000002/2)

 

# Gives wrong output

print(int(((10 ** 17) + 2)/2))

 

# Gives Correct output

print(((10 ** 17) + 2)//2)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    500000001.0
    50000000000000000
    50000000000000001
    

**Example 2:**

 __

 __  
 __

 __

 __  
 __  
 __

x= 10000000000000000000006

if int(x / 2) == x // 2:

 print("Hello")

else:

 print("World")  
  
---  
  
 __

 __

 **Output:**

    
    
    World
    

The Output should have been Hello if the single division operator behaved
normally because 2 properly divides x. But the output is World because The
results after Single Division Operator and Double Division Operator **ARE NOT
THE SAME**.

This fact can be used for programs such as finding the sum of first n numbers
for a large n.

 __

 __  
 __

 __

 __  
 __  
 __

n= 10000000000

 

s1 = int(n * (n + 1) / 2)

s2 = n * (n + 1) // 2

 

print("Sum using single division operator : ", s1)

print("Sum using double division operator : ", s2)  
  
---  
  
 __

 __

 **Output:**

    
    
    Sum using single division operator :  50000000005000003584
    Sum using double division operator :  50000000005000000000
    

Thus the result found by using the single division operator is Wrong, while
the result found by using the double division operator is Correct. This is a
huge benefit of Double Division Operator over Single Division Operator in
Python.  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

