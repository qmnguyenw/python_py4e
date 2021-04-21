loops in python



Python programming language provides following types of loops to handle
looping requirements. Python provides three ways for executing the loops.
While all the ways provide similar basic functionality, they differ in their
syntax and condition checking time.

  1.  **While Loop:**
  2. In python, while loop is used to execute a block of statements repeatedly until a given a condition is satisfied. And when the condition becomes false, the line immediately after the loop in program is executed. 

**Syntax** :

    
    
    while expression:
        statement(s)
    

3\. All the statements indented by the same number of character spaces after a
programming construct are considered to be part of a single block of code.
Python uses indentation as its method of grouping statements.  
Example:

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate

# while loop

count = 0

while (count < 3): 

 count = count + 1

 print("Hello Geek")  
  
---  
  
 __

 __

 **Output:**

    
    
    Hello Geek
    Hello Geek
    Hello Geek
    
    

  * **Using else statement with while loops:** As discussed above, while loop executes the block until a condition is satisfied. When the condition becomes false, the statement immediately after the loop is executed.   
The else clause is only executed when your while condition becomes false. If
you break out of the loop, or if an exception is raised, it won’t be executed.  
**If else like this:**

## Python

  

  

 __

 __  
 __

 __

 __  
 __  
 __

if condition:

 # execute these statements

else:

 # execute these statements  
  
---  
  
 __

 __

