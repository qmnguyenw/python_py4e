Loops and Control Statements (continue, break and pass) in Python



Python programming language provides following types of loops to handle
looping requirements.

 **While Loop**  
Syntax :

    
    
    while expression:
        statement(s)
    

In Python, all the statements indented by the same number of character spaces
after a programming construct are considered to be part of a single block of
code. Python uses indentation as its method of grouping statements.

 __

 __  
 __

 __

 __  
 __  
 __

# prints Hello Geek 3 Times

count = 0

while (count < 3): 

 count = count+1

 print("Hello Geek")  
  
---  
  
 __

 __

Output:

    
    
    Hello Geek
    Hello Geek
    Hello Geek
    

See this for an example where while loop is used for iterators. As mentioned
in the article, it is not recommended to use while loop for iterators in
python.

  

  

**For in Loop**  
In Python, there is no C style for loop, i.e., for (i=0; i<n; i++). There is
“for in” loop which is similar to for each loop in other languages.

Syntax:

    
    
    for iterator_var in sequence:
        statements(s)

It can be used to iterate over iterators and a range.

 __

 __  
 __

 __

 __  
 __  
 __

# Iterating over a list

print("List Iteration")

l = ["geeks", "for", "geeks"]

for i in l:

 print(i)

 

# Iterating over a tuple (immutable)

print("\nTuple Iteration")

t = ("geeks", "for", "geeks")

for i in t:

 print(i)

 

# Iterating over a String

print("\nString Iteration") 

s = "Geeks"

for i in s :

 print(i)

 

# Iterating over dictionary

print("\nDictionary Iteration") 

d = dict() 

d['xyz'] = 123

d['abc'] = 345

for i in d :

 print("%s %d" %(i, d[i]))  
  
---  
  
 __

 __

Output:

    
    
    List Iteration
    geeks
    for
    geeks
    
    Tuple Iteration
    geeks
    for
    geeks
    
    String Iteration
    G
    e
    e
    k
    s
    
    Dictionary Iteration
    xyz  123
    abc  345
    

We can use for in loop for user defined iterators. See this for example.

**Nested Loops**  
Python programming language allows to use one loop inside another loop.
Following section shows few examples to illustrate the concept.  
Syntax:

  

  

    
    
    for iterator_var in sequence:
        for iterator_var in sequence:
            statements(s)
            statements(s)
    

The syntax for a nested while loop statement in Python programming language is
as follows:

    
    
    while expression:
        while expression: 
            statement(s)
            statement(s)
    

A final note on loop nesting is that we can put any type of loop inside of any
other type of loop. For example a for loop can be inside a while loop or vice
versa.

 __

 __  
 __

 __

 __  
 __  
 __

from __future__ import print_function

for i in range(1, 5):

 for j in range(i):

 print(i, end=' ')

 print()  
  
---  
  
 __

 __

Output:

    
    
    1
    2 2
    3 3 3
    4 4 4 4

 **Loop Control Statements**  
Loop control statements change execution from its normal sequence. When
execution leaves a scope, all automatic objects that were created in that
scope are destroyed. Python supports the following control statements.

 **Continue Statement**  
It returns the control to the beginning of the loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Prints all letters except 'e' and 's'

for letter in 'geeksforgeeks': 

 if letter == 'e' or letter == 's':

 continue

 print 'Current Letter :', letter

 var = 10  
  
---  
  
 __

 __

Output:

    
    
    Current Letter : g
    Current Letter : k
    Current Letter : f
    Current Letter : o
    Current Letter : r
    Current Letter : g
    Current Letter : k
    

**Break Statement**  
It brings control out of the loop

 __

 __  
 __

 __

 __  
 __  
 __

for letter in 'geeksforgeeks': 

 

 # break the loop as soon it sees 'e' 

 # or 's'

 if letter == 'e' or letter == 's':

 break

 

print 'Current Letter :', letter  
  
---  
  
 __

 __

Output:

    
    
    Current Letter : e

 **Pass Statement**  
We use pass statement to write empty loops. Pass is also used for empty
control statement, function and classes.

 __

 __  
 __

 __

 __  
 __  
 __

# An empty loop

for letter in 'geeksforgeeks':

 pass

print 'Last Letter :', letter  
  
---  
  
 __

 __

Output:

    
    
    Last Letter : s

 **Exercise:**  
How to print a list in reverse order (from last to first item) using while and
for in loops.

This article is contributed by **Ashirwad Kumar.** If you like GeeksforGeeks
and would like to contribute, you can also write an article and mail your
article to contribute@geeksforgeeks.org. See your article appearing on the
GeeksforGeeks main page and help other Geeks.  
Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

