Programs for printing pyramid patterns in Python



Patterns can be printed in python using simple for loops. **First outer loop**
is used to handle **number of rows** and **Inner nested loop** is used to
handle the **number of columns**. Manipulating the print statements, different
number patterns, alphabet patterns or star patterns can be printed.  
Some of the Patterns are shown in this article.

  * **Simple pyramid pattern**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern

def pypart(n):

 

 # outer loop to handle number of rows

 # n in this case

 for i in range(0, n):

 

 # inner loop to handle number of columns

 # values changing acc. to outer loop

 for j in range(0, i+1):

 

 # printing stars

 print("* ",end="")

 

 # ending line after each row

 print("\r")

# Driver Code

n = 5

pypart(n)  
  
---  
  
 __

 __

 **Output**

    
    
    * 
    * * 
    * * * 
    * * * * 
    * * * * * 
    

  * **Another Approach:**   
Using List in Python 3, this could be done in a simpler way

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern

def pypart(n):

 myList = []

 for i in range(1,n+1):

 myList.append("*"*i)

 print("\n".join(myList))

# Driver Code

n = 5

pypart(n)  
  
---  
  
 __

 __

 **Output**

    
    
    *
    **
    ***
    ****
    *****
    

  * **After 180 degree rotation**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern

def pypart2(n):

 

 # number of spaces

 k = 2*n - 2

 # outer loop to handle number of rows

 for i in range(0, n):

 

 # inner loop to handle number spaces

 # values changing acc. to requirement

 for j in range(0, k):

 print(end=" ")

 

 # decrementing k after each loop

 k = k - 2

 

 # inner loop to handle number of columns

 # values changing acc. to outer loop

 for j in range(0, i+1):

 

 # printing stars

 print("* ", end="")

 

 # ending line after each row

 print("\r")

# Driver Code

n = 5

pypart2(n)  
  
---  
  
 __

 __

 **Output**

    
    
            * 
          * * 
        * * * 
      * * * * 
    * * * * * 
    

  * **Printing Triangle**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern triangle

def triangle(n):

 

 # number of spaces

 k = n - 1

 # outer loop to handle number of rows

 for i in range(0, n):

 

 # inner loop to handle number spaces

 # values changing acc. to requirement

 for j in range(0, k):

 print(end=" ")

 

 # decrementing k after each loop

 k = k - 1

 

 # inner loop to handle number of columns

 # values changing acc. to outer loop

 for j in range(0, i+1):

 

 # printing stars

 print("* ", end="")

 

 # ending line after each row

 print("\r")

# Driver Code

n = 5

triangle(n)  
  
---  
  
 __

 __

 **Output**

