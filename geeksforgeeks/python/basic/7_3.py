Ways to increment Iterator from inside the For loop in Python



 **For loops**, in general, are used for sequential traversal. It falls under
the category of definite iteration. Definite iterations mean the number of
repetitions is specified explicitly in advance. But have you ever wondered,
what happens, if you try to increment the value of the iterator from inside
the for loop. Let’s see with the help of the below example.  
 **Example:**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

lis= [1, 2, 3, 4, 5]

for i in range(len(lis)):

 

 print(lis[i])

 i += 2  
  
---  
  
 __

 __

 **Output:**  

    
    
    1
    2
    3
    4
    5

The above example shows this odd behavior of the for loop because the for loop
in Python is not a convention C style for loop, i.e., for (i=0; i<n; i++)
rather it is a for in loop which is similar to for each loop in other
languages. However, there are few methods by which we can control the
iteration in the for loop. Some of them are –  

  * **Using While loop:** We can’t directly increase/decrease the iteration value inside the body of the for loop, we can use while loop for this purpose.  
 **Example:**  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Using while loop

lis = [1, 2, 3, 4, 5]

i = 0

while(i < len(lis)):

 print(lis[i], end = " ")

 

 # Changing the value of

 # i inside the loop will

 # change it's value at the

 # time of checking condition

 i += 2

   
  
---  
  
__

__

  * **Output:**  

    
    
    1 3 5

  *   * **Using another variable:** We can use another variable for the same purpose because after every iteration the value of loop variable is re-initialized.  
 **Example:**  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Using for loop

lis = [1, 2, 3, 4, 5]

i = 0

for j in range(len(lis)):

 # Terminating condition for i

 if(i >= len(lis)):

 break

 

 print(lis[i], end = " ") 

 i += 2  
  
---  
  
 __

 __

  *  **Output:**  

    
    
    1 3 5

  *   * **Using Range Function:** We can use the range function as the third parameter of this function specifies the step.  
 **Note:** For more information, refer to Python range() Function.  
 **Example:**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Using for loop

lis = [1, 2, 3, 4, 5]

for i in range(0, len(lis), 2):

 

 print(lis[i], end = " ")   
  
---  
  
__

__

  * **Output:**  

    
    
    1 3 5

  * 

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

