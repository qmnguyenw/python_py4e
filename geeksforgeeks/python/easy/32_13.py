Ternary Operator in Python



Ternary operators also known as conditional expressions are operators that
evaluate something based on a condition being true or false. It was added to
Python in version 2.5.  
It simply allows to test a condition in a **single line** replacing the
multiline if-else making the code compact.

Syntax :

    
    
    [on_true] if [expression] else [on_false] 

  1. **Simple Method to use ternary operator:**

 __

 __  
 __

 __

 __  
 __  
 __

# Program to demonstrate conditional operator

a, b = 10, 20

 

# Copy value of a in min if a < b else copy b

min = a if a < b else b

 

print(min)  
  
---  
  
 __

 __

    
        **Output:** 
    10
    

  2. **Direct Method by using tuples, Dictionary and lambda**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate ternary operator

a, b = 10, 20

 

# Use tuple for selecting an item

# (if_test_false,if_test_true)[test]

print( (b, a) [a < b] )

 

# Use Dictionary for selecting an item

print({True: a, False: b} [a < b])

 

# lamda is more efficient than above two methods

# because in lambda we are assure that

# only one expression will be evaluated unlike in

# tuple and Dictionary

print((lambda: b, lambda: a)[a < b]())  
  
---  
  
 __

 __

    
        Output:
    10
    10
    10

  3.  **Ternary operator can be written as nested if-else:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate nested ternary operator

a, b = 10, 20

 

print ("Both a and b are equal" if a == b else "a is
greater than b"

 if a > b else "b is greater than a")  
  
---  
  
 __

 __

 _Above approach can be written as:_

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate nested ternary operator

a, b = 10, 20

 

if a != b:

 if a > b:

 print("a is greater than b")

 else:

 print("b is greater than a")

else:

 print("Both a and b are equal")  
  
---  
  
 __

 __

    
        **Output:** b is greater than a
    

**  
Important Points:  
**

  * First the given condition is evaluated (a < b), then either a or b is returned based on the Boolean value returned by the condition
  * Order of the arguments in the operator is different from other languages like C/C++ (See C/C++ ternary operators).
  * Conditional expressions have the lowest priority amongst all Python operations.

 **Method used prior to 2.5 when ternary operator was not present**  
In an expression like the one given below , the interpreter checks for the
expression if this is true then on_true is evaluated, else the on_false is
evaluated.

  

  

 **Syntax :**

    
    
    '''When condition becomes true, expression [on_false]
       is not executed and value of "True and [on_true]"
       is returned.  Else value of "False or [on_false]"
       is returned.
       Note that "True and x" is equal to x. 
       And "False or x" is equal to x. '''
    [expression] and [on_true] or [on_false] 

**Example :**

 __

 __  
 __

 __

 __  
 __  
 __



# Program to demonstrate conditional operator

a, b = 10, 20

 

# If a is less than b, then a is assigned

# else b is assigned (Note : it doesn't 

# work if a is 0.

min = a < b and a or b

 

print(min)  
  
---  
  
 __

 __

    
    
    **Output:**
    10
    

Note : The only drawback of this method is that **on_true must not be zero or
False**. If this happens on_false will be evaluated always. The reason for
that is if expression is true, the interpreter will check for the on_true, if
that will be zero or false, that will force the interpreter to check for
on_false to give the final result of whole expression.

This article is contributed by **Mayank Rawat** and improved by Shubham
Bansal. If you like GeeksforGeeks and would like to contribute, you can also
write an article using contribute.geeksforgeeks.org or mail your article to
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

