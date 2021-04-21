Python Program to Determine Whether a Given Number is Even or Odd Recursively



In this article, We will see how to write the program to find the given number
is Even or Odd Using the Recursion Method. If the number is even returned true
else false in Python.

For that, we use the Operator Called ******Modulus Operator** **.** This
operator used in the operation when we need to calculate the remainder of that
number when divided by any divisor.

  *  **Even Number** : A number Which is completely divisible by 2 Hence remainders is 0 
  * **Odd Number:** A number which is not divisible by 2 Hence remainders is 1

 **Examples:**

    
    
     **Input:** 2
    **Output:** True
    **Explanation :** 2 % 2==0 So True
    
    **Input:** 5
    **Ouput:** False 
    **Expalantion :** 2 % 2 != 0 So, False
    

**Methods #1:**

 **Approach :**

  

  

  * We use the concept of getting the remainder without using the modulus operator by subtracting the number by number-2
  * If at last, we get any remainder then that number is odd and return the False for that number
  * Else the number is even and return True for that number

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# defining the function having the one parameter as input

def evenOdd(n):

 

 #if remainder is 0 then num is even

 if(n==0):

 return True

 

 #if remainder is 1 then num is odd

 elif(n==1):

 return False

 else:

 return evenOdd(n-2)

 

# Input by geeks

num=3

if(evenOdd(num)):

 print(num,"num is even")

else:

 print(num,"num is odd")  
  
---  
  
 __

 __

 **Output:**

    
    
    3 num is odd
    

**Methods #2:**

We use the modulus operator to find the even or odd Like if num % 2 == 0 then
the remainder is 0 so the given number is even and return True

Else if num % 2 != 0 then the remainder is not zero so the given number is odd
and return False

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# defining the function having

# the one parameter as input

def evenOdd(n):

 

 #if remainder is 0 then num is even

 if(n % 2 == 0):

 return True

 

 #if remainder is 1 then num is odd

 elif(n %2 != 0):

 return False

 else:

 return evenOdd(n)

 

# Input by geeks

num = 3

if(evenOdd( num )):

 print(num ,"num is even")

else:

 print(num ,"num is odd")  
  
---  
  
 __

 __

 **Output:**

    
    
    3 num is odd
    

**Methods #3:** To print all the even number for the range (a, b)

Here We will print all the even number for the Given Range n in the Function
evenOdd(n)

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# writing the function having the range

# and printing the even in that range

def evenOdd(a,b):

 if(a>b):

 return

 print(a ,end=" ")

 return evenOdd(a+2,b)

 

# input by geeks

x=2

y=10

if(x % 2 ==0):

 x=x

 

else:

 

 # if the number x is odd then 

 # add 1 the number into it to

 # avoid any error to make it even

 x+=1

evenOdd(x,y)  
  
---  
  
 __

 __

 **Output:**

    
    
    2 4 6 8 10
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

