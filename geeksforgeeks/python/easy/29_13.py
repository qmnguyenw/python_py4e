Vulnerability in input() function – Python 2.x



This article aims at explaining and exploring the vulnerability in the input()
function in Python 2.x. In Python 3, the raw_input() function was erased, and
it’s functionality was transferred to a new built-in function known as
input().

 **Ways to input data in Python 2.x**

There are two common methods to receive input in Python 2.x:

  1. Using the **input() function:** This function takes the value and type of the input you enter **as it is** without modifying any type.
  2. Using the **raw_input() function** : This function **explicitly converts** the input you give to type string,

Let us use the following program to determine the difference between the two:

 __

 __  
 __

 __

 __  
 __  
 __

# Python 2.x program to show differences between

# input() and rawinput()function 

 

# 3 inputs using raw_input() function, 

# after which data type of the value

# entered is displayed

s1 = raw_input("Enter input to test raw_input() function: ")

print type(s1)

 

s2 = raw_input("Enter input to test raw_input() function: ")

print type(s2)

 

s3 = raw_input("Enter input to test raw_input() function: ")

print type(s3)

 

# 3 inputs using input() function, 

# after which data type of the value

# entered is displayed

s4 = input("Enter input to test input() function: ")

print type(s4)

 

s5 = input("Enter input to test input() function: ")

print type(s5)

 

s6 = input("Enter input to test input() function: ")

print type(s6)  
  
---  
  
 __

 __

Input:

  

  

    
    
    Hello
    456
    [1,2,3]
    45
    "goodbye"
    [1,2,3]
    

Output:

    
    
    Enter input to test raw_input() function: <type 'str'>
    Enter input to test raw_input() function: <type 'str'>
    Enter input to test raw_input() function: <type 'str'>
    
    Enter input to test input() function: <type ' **int** '>
    Enter input totest input() function: <type ' **str** '>
    Enter input to test input() function: <type ' **list** '>
    

**  
Note:** While giving string input in the input() function, we have to enclose
to value in double quotes. This is not required in raw_input()

 **Vulnerability in input() method**

The vulnerability in input() method lies in the fact that the variable
accessing the value of input can be accessed by anyone just by using the name
of variable or method. Let’s explore these one by one:

  1.  **Variable name as input parameter:** The variable having the value of input variable is able to access the value of the input variable directly.

 __

 __  
 __

 __

 __  
 __  
 __

# Python 2.x program to show Vulnerabilities

# in input() function using a variable 

 

import random

secret_number = random.randint(1,500)

print "Pick a number between 1 to 500"

while True:

 res = input("Guess the number: ")

 if res==secret_number:

 print "You win"

 break

 else:

 print "You lose"

 continue  
  
---  
  
 __

 __

Input:

    
        15
    

Output:

    
    
    Pick a number between 1 to 500
    Guess the number: You lose
    Guess the number: 
    

Input:

    
        secret_number
    

Output:

  

  

    
    
    Pick a number between 1 to 500
    Guess the number: You win
    

As it can be seen, in second case the variable “secret_number” can be directly
given as input and answer is always “You won”. It evaluates the variable as if
a number was directly entered, by which means it returns a True Boolean
always. Using raw_input, it would not be possible as it disallows to read the
variable directly.

  2.  **Function name as parameter:** The vulnerability lies here as we can even provide the name of a function as input and access values that are otherwise not meant to be accessed.

 __

 __  
 __

 __

 __  
 __  
 __

# Python 2.x program to demonstrate input() function

# vulnerability by passing function name as parameter

secret_value = 500

 

# function that returns the secret value

def secretfunction():

 return secret_value

 

# using raw_input() to enter the number

input1 = raw_input("Raw_input(): Guess secret number: ")

 

# input1 will be explicitly converted to a string

if input1 == secret_value:

 print "You guessed correct"

else:

 print "wrong answer"

 

# using input() to enter the number

input2 = input("Input(): Guess the secret number: ")

 

#input2 is evaluated as it is entered

if input2 == secret_value:

 print "You guessed correct"

else:

 print "wrong answer"  
  
---  
  
 __

 __

Input:

    
    
    400
    secretfunction()
    

Output:

    
    
    Raw_input(): Guess secret number: wrong answer
    Input(): Guess the secret number: You guessed correct
    

In this set of input/output, we can see that when we use raw_input, we
necessarily have to input the correct number. However while using the input()
function, we can even provide the name of a function or variable, and the
interpreter will evaluate that.  
Here for example, the input for input() function has been given as the name of
a function ‘secretfunction()’. The interpreter evaluates this function call
and returns the secret number that we wish to find and hence our if condition
evaluates to be true, even though we did not enter the secret number

Input:

    
    
    secretfunction()
    secret_value
    

Output:

    
    
    Raw_input(): Guess secret number: wrong answer
    Input(): Guess the secret number: You guessed correct
    

As explained in first point, in this example also we were able to simply enter
the variable name ‘secret_number’ in the input for ‘input()’ function and we
were able to gain access to the secret value.  
However while trying to call secretfunction() in the input for the raw_input()
function, it gives us false as the interpreter converts our argument to
string, and doesn’t evaluate it as a function call.

 **Preventing input vulnerabilities**

It is always better to use raw_input() in python 2.x and then explicitly
convert the input to whatever type we require. For example, if we wish to take
input of an integer, we can do the following

    
    
    n = int(raw_input())
    

This prevents the malicious calling or evaluation of functions.

This article is contributed by **Deepak Srivatsav**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

