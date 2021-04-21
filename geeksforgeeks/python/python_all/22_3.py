Python program to find the factorial of a number using recursion



A factorial is positive integer **n** , and denoted by **n!**. Then the
product of all positive integers less than or equal to _**n**._

![n! = n*\(n-1\)*\(n-2\)*\(n-3\)*....*1](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-9600161e571be0a77f1c076474549eb4_l3.png)

 **For example:**

![5! = 5*4*3*2*1 = 120](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-20dc0cd7d81ec89dd4032f424f9be70d_l3.png)

In this article, we are going to calculate the factorial of a number using
recursion.

  

  

 **Examples:**

    
    
     **Input:** 5
    **Output:** 120
    
    **Input:** 6
    **Output:** 720
    

**Implementation:**

If fact(5) is called, it will call fact(4), fact(3), fact(2) and fact(1). So
it means keeps calling itself by reducing value by one till it reaches 1.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 program to find

# factorial of given number 

def factorial(n): 

 

 # Checking the number

 # is 1 or 0 then

 # return 1

 # other wise return

 # factorial

 if (n==1 or n==0):

 

 return 1

 

 else:

 

 return (n * factorial(n - 1)) 

 

# Driver Code 

num = 5; 

print("number : ",num)

print("Factorial : ",factorial(num))  
  
---  
  
 __

 __

 **Output:**

    
    
    Number :  5
    Factorial :  120
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

