Keywords in Python – Set 1



Python Keywords – Introduction

This article aims at providing a detailed insight into these keywords.

 **1\. True** : This keyword is used to represent a boolean true. If a
statement is true, “True” is printed.

 **2\. False** : This keyword is used to represent a boolean false. If a
statement is false, “False” is printed.  
True and False in python are same as 1 and 0. Example:

 __

 __  
 __

 __

 __  
 __  
 __

print (False == 0)

print (True == 1)

 

print (True + True + True)

print (True + False + False)  
  
---  
  
 __

 __

 **3\. None** : This is a special constant used to **denote a null value or a
void**. **Its important to remember, 0, any empty container(e.g empty list) do
not compute to None**.  
It is an object of its datatype – NoneType. It is not possible to create
multiple None objects and can assign them to variables.

  

  

 **4\. and** : This a logical operator in python. “and” **Return the first
false value .if not found return last**. The truth table for “and” is depicted
below.

![and](https://media.geeksforgeeks.org/wp-content/uploads/and1-249x300.png)

3 and 0 **returns 0**  
3 and 10 **returns 10**  
10 or 20 or 30 or 10 or 70 returns **10**

The above statements might be a bit confusing to a programmer coming from a
language like **C** where the logical operators always return boolean values(0
or 1). Following lines are straight from the python docs explaining this:

> The expression x and y first evaluates x; if x is false, its value is
> returned; otherwise, y is evaluated and the resulting value is returned.
>
> The expression x or y first evaluates x; if x is true, its value is
> returned; otherwise, y is evaluated and the resulting value is returned.

 **Note** that neither and nor or restrict the value and type they return to
False and True, but rather return the last evaluated argument. This is
sometimes useful, e.g., if s is a string that should be replaced by a default
value if it is empty, the expression s or ‘foo’ yields the desired value.
Because not has to create a new value, it returns a boolean value regardless
of the type of its argument (for example, not ‘foo’ produces False rather than
”.)

 **5\. or** : This a logical operator in python. “or” **Return the first True
value.if not found return last**.The truth table for “or” is depicted below.

  

  

![or](https://media.geeksforgeeks.org/wp-content/uploads/or1-250x300.png)

3 or 0 **returns 3**  
3 or 10 **returns 3**  
0 or 0 or 3 or 10 or 0 returns **3**

 **6\. not** : This logical operator **inverts the truth value**. The truth
table for “not” is depicted below.

![not](https://media.geeksforgeeks.org/wp-content/uploads/not1.png)

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# True, False, None, and, or , not

 

# showing that None is not equal to 0

# prints False as its false.

print (None == 0)

 

# showing objective of None

# two None value equated to None

# here x and y both are null

# hence true

x = None

y = None

print (x == y)

 

# showing logical operation 

# or (returns True)

print (True or False)

 

# showing logical operation 

# and (returns False)

print (False and True)

 

# showing logical operation 

# not (returns False)

print (not True)  
  
---  
  
 __

 __

Output:

    
    
    False
    True
    True
    False
    False
    

**7\. assert** : This function is used for **debugging purposes**. Usually
used to check the correctness of code. If a statement evaluated to true,
nothing happens, but when it is false, “ **AssertionError** ” is raised . One
can also **print a message with the error, separated by a comma**.

 **8\. break** : “break” is used to control the flow of the loop. The
statement is used to **break out of the loop and passes the control to the
statement following immediately after loop.**

 **9\. continue** : “continue” is also used to control the flow of code. The
keyword **skips the** **current iteration of the loop** , but **does not end
the loop**.

Illustrations of break and continue keywords can be seen in the article below.

Loops and Control Statements (continue, break and pass) in Python  
 **10\. class** : This keyword is used to **declare user defined classes**.
For more info. click here.

 **11\. def** : This keyword is used to **declare user defined functions**.
For more info. click here.

 **12\. if** : It is a control statement for decision making. **Truth
expression forces control to go in “if” statement block.**

 **13\. else** : It is a control statement for decision making. **False
expression forces control to go in “else” statement block.**

 **14\. elif** : It is a control statement for decision making. It is short
for “ **else if** ”

 **if, else and elif** conditional statements are explained in detail here
article.

 **15\. del** : del is used to **delete a reference to an object**. Any
variable or list value can be deleted using del.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# del and assert

 

# initialising list 

a = [1, 2, 3]

 

# printing list before deleting any value

print ("The list before deleting any value")

print (a)

 

# using del to delete 2nd element of list

del a[1]

 

# printing list after deleting 2nd element

print ("The list after deleting 2nd element")

print (a)

 

# demonstrating use of assert

# prints AssertionError

assert 5 < 3, "5 is not smaller than 3"  
  
---  
  
 __

 __

Output:

    
    
    The list before deleting any value
    [1, 2, 3]
    The list after deleting 2nd element
    [1, 3]
    

Runtime Error:

    
    
    Traceback (most recent call last):
      File "9e957ae60b718765ec2376b8ab4225ab.py", line 19, in 
        assert 5<3, "5 is not smaller than 3"
    AssertionError: 5 is not smaller than 3
    

Next Article – Keywords in Python | Set 2

This article is contributed by **Manjeet Singh(S. Nandini)**. If you like
GeeksforGeeks and would like to contribute, you can also write an article
using contribute.geeksforgeeks.org or mail your article to
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

