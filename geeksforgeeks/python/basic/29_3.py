Returning Multiple Values in Python



In Python, we can return multiple values from a function. Following are
different ways

 **1)** **Using Object:** This is similar to C/C++ and Java, we can create a
class (in C, struct) to hold multiple values and return an object of the
class.

 __

 __  
 __

 __

 __  
 __  
 __

# A Python program to return multiple

# values from a method using class

class Test:

 def __init__(self):

 self.str = "geeksforgeeks"

 self.x = 20

 

# This function returns an object of Test

def fun():

 return Test()

 

# Driver code to test above method

t = fun() 

print(t.str)

print(t.x)  
  
---  
  
 __

 __

Output:

    
    
    geeksforgeeks
    20

Below are interesting methods for somebody shifting C++/Java world.

  

  

**2) Using Tuple:** A Tuple is a comma separated sequence of items. It is
created with or without (). Tuples are immutable. See this for details of
tuple and list.

 __

 __  
 __

 __

 __  
 __  
 __

# A Python program to return multiple

# values from a method using tuple

 

# This function returns a tuple

def fun():

 str = "geeksforgeeks"

 x = 20

 return str, x; # Return tuple, we could also

 # write (str, x)

 

# Driver code to test above method

str, x = fun() # Assign returned tuple

print(str)

print(x)  
  
---  
  
 __

 __

Output:

    
    
    geeksforgeeks
    20

**3) Using a list:** A list is like an array of items created using square
brackets. They are different from arrays as they can contain items of
different types. Lists are different from tuples as they are mutable.

 __

 __  
 __

 __

 __  
 __  
 __

# A Python program to return multiple

# values from a method using list

 

# This function returns a list

def fun():

 str = "geeksforgeeks"

 x = 20

 return [str, x]; 

 

# Driver code to test above method

list = fun() 

print(list)  
  
---  
  
 __

 __

Output:

    
    
    ['geeksforgeeks', 20]

**4) Using a Dictionary:** A Dictionary is similar to hash or map in other
languages. See this for details of dictionary.

 __

 __  
 __

 __

 __  
 __  
 __

# A Python program to return multiple

# values from a method using dictionary

 

# This function returns a dictionary

def fun():

 d = dict(); 

 d['str'] = "GeeksforGeeks"

 d['x'] = 20

 return d

 

# Driver code to test above method

d = fun() 

print(d)  
  
---  
  
 __

 __

Output:

  

  

    
    
    {'x': 20, 'str': 'GeeksforGeeks'}

  
**5) Using Data Class (Python 3.7+):** In Python 3.7 and above the Data Class
can be used to return a class with automatically added unique methods. The
Data Class module has a decorator and functions for automatically adding
generated special methods such as __init__() and __repr__() in the user-
defined classes.

 __

 __  
 __

 __

 __  
 __  
 __

from dataclasses import dataclass

 

@dataclass

class Book_list:

 name: str

 perunit_cost: float

 quantity_available: int = 0

 

 # function to calculate total cost 

 def total_cost(self) -> float:

 return self.perunit_cost * self.quantity_available

 

book = Book_list("Introduction to programming.", 300, 3)

x = book.total_cost()

 

# print the total cost

# of the book

print(x)

 

# print book details

print(book)

 

# 900

Book_list(name='Python programming.',

 perunit_cost=200,

 quantity_available=3)  
  
---  
  
 __

 __

Output:

    
    
    900
    Book_list(name='Introduction to programming.', perunit_cost=300, quantity_available=3)
    Book_list(name='Python programming.', perunit_cost=200, quantity_available=3)

 **Reference:**  
http://stackoverflow.com/questions/354883/how-do-you-return-multiple-values-
in-python

This article is contributed by **Shubham Agrawal**. If you like GeeksforGeeks
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

