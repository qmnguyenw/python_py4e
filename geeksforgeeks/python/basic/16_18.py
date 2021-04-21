Structuring Python Programs



In this article, you would come to know about proper structuring and
formatting your python programs.

 **Python Statements** In general, the interpreter reads and executes the
statements line by line i.e sequentially. Though, there are some statements
that can alter this behavior like conditional statements.  
Mostly, python statements are written in such a format that one statement is
only written in a single line. The interpreter considers the ‘new line
character’ as the terminator of one instruction. But, writing multiple
statements per line is also possible that you can find below.  
Examples:

 __

 __  
 __

 __

 __  
 __  
 __

# Example 1

 

print('Welcome to Geeks for Geeks')   
  
---  
  
__

__

**Output:**

    
    
    Welcome to Geeks for Geeks
    

__

__  
__

__

__  
__  
__

# Example 2

 

x = [1, 2, 3, 4]

 

# x[1:3] means that start from the index 

# 1 and go upto the index 2

print(x[1:3]) 

 

""" In the above mentioned format, the first 

index is included, but the last index is not

included."""  
  
---  
  
 __

 __

 **Output:**

    
    
    [2, 3]
    

**Multiple Statements per Line** We can also write multiple statements per
line, but it is not a good practice as it reduces the readability of the code.
Try to avoid writing multiple statements in a single line. But, still you can
write multiple lines by terminating one statement with the help of ‘;’. ‘;’ is
used as the terminator of one statement in this case.  
For Example, consider the following code.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Example

 

a = 10; b = 20; c = b + a

 

print(a); print(b); print(c)  
  
---  
  
 __

 __

 **Output:**

    
    
    10
    20
    30
    

**Line Continuation to avoid left and right scrolling**  
Some statements may become very long and may force you to scroll the screen
left and right frequently. You can fit your code in such a way that you do not
have to scroll here and there. Python allows you to write a single statement
in multiple lines, also known as line continuation. Line continuation enhances
readability as well.

    
    
    # Bad Practice as width of this code is too much.
     
    #code
    x = 10
    y = 20
    z = 30
    no_of_teachers = x
    no_of_male_students = y
    no_of_female_students = z
     
    if (no_of_teachers == 10 and no_of_female_students == 30 and no_of_male_students == 20 and (x + y) == 30):
        print('The course is valid')
     
    # This could be done instead:
     
    if (no_of_teachers == 10 and no_of_female_students == 30
        and no_of_male_students == 20 and x + y == 30):
        print('The course is valid')

 **Types of Line Continuation**  
In general, there are two types of line continuation

  *  **Implicit Line Continuation**  
This is the most straightforward technique in writing a statement that spans
multiple lines.  
Any statement containing opening parentheses (‘(‘), brackets (‘[‘), or curly
braces (‘{‘) is presumed to be incomplete until all matching parentheses,
square brackets, and curly braces have been encountered. Until then, the
statement can be implicitly continued across lines without raising an error.  
Examples:

 __

 __  
 __

 __

 __  
 __  
 __

# Example 1

 

# The following code is valid

a = [

 [1, 2, 3],

 [3, 4, 5],

 [5, 6, 7]

 ]

 

print(a)  
  
---  
  
 __

 __

 **Output:**

    
    
    [[1, 2, 3], [3, 4, 5], [5, 6, 7]]
    

__

__  
__

__

__  
__  
__

# Example 2

# The following code is also valid

 

person_1 = 18

person_2 = 20

person_3 = 12

 

if (

 person_1 >= 18 and

 person_2 >= 18 and

 person_3 < 18

 ):

 print('2 Persons should have ID Cards')  
  
---  
  
 __

 __

 **Output:**

    
    
    2 Persons should have ID Cards
    

  * **Explicit Line Continuation**  
Explicit Line joining is used mostly when implicit line joining is not
applicable. In this method, you have to use a character that helps the
interpreter to understand that the particular statement is spanning more than
one lines.  
Backslash (\\) is used to indicate that a statement spans more than one line.
The point is to be noted that ” must be the last character in that line, even
white-space is not allowed.  
See the following example for clarification

 __

 __  
 __

 __

 __  
 __  
 __

# Example

 

x = \

 1 + 2 \

 + 5 + 6 \

 + 10

 

print(x)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    24
    

