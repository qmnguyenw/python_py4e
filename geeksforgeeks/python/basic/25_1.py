Execute a String of Code in Python



Given few lines of code inside a string variable and execute the code inside
the string.

Examples:

    
    
    Input:
    code = """ a = 6+5
               print(a)"""
    Output:
    11
    Explanation:
    Mind it that "code" is a variable and
    not python code. It contains another code, 
    which we need to execute.
    
    Input:
    code = """ def factorial(num):
                   for i in range(1,num+1):
                       fact = fact*i
                   return fact
               print(factorial(5))"""
    Output:
    120
    Explanation:
    On executing the program cantoning the 
    variable in Python we must get the result 
    after executing the content of the variable.
    

Here we use the **exec()** function to solve the code contained inside a
variable. exec() function is used for the dynamic execution of Python code. It
can take a block of code containing Python statements like loops, class,
function/method definitions and even try/except block. This function doesn’t
return anything. The code below solves the problem and explains the exec()
function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate use of exec to

# execute a given code as string.

 

# function illustrating how exec() functions.

def exec_code():

 LOC = """

def factorial(num):

 fact=1

 for i in range(1,num+1):

 fact = fact*i

 return fact

print(factorial(5))

"""

 exec(LOC)

 

# Driver Code

exec_code()  
  
---  
  
 __

 __

Output:

    
    
    120
    

This article is contributed by **Chinmoy Lenka**. If you like GeeksforGeeks
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

