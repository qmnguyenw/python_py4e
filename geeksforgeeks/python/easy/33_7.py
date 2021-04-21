String Template Class in Python



In the String module, Template Class allows us to create simplified syntax for
output specification. The format uses placeholder names formed by $ with valid
Python identifiers (alphanumeric characters and underscores). Surrounding the
placeholder with braces allows it to be followed by more alphanumeric letters
with no intervening spaces. Writing $$ creates a single escaped $.  

### Python String Template:

The Python string Template is created by passing the template string to its
constructor. It supports $-based substitutions. This class has 2 key methods:

  * **substitute(mapping, **kwds):** This method performs substitutions using a dictionary with a process similar to key-based mapping objects. keyword arguments can also be used for the same purpose. In case the key-based mapping and the keyword arguments have the same key, it throws a _**TypeError**_. If keys are missing it returns a _**KeyError**_. 
  * **safe_substitute(mapping, **kwds):** The behavior of this method is similar to that of the substitute method but it doesn’t throw a _**KeyError**_ if a key is missing, rather it returns a placeholder in the result string.   

The substitute() method raises a KeyError when a placeholder is not supplied
in a dictionary or a keyword argument. For mail-merge style applications,
user-supplied data may be incomplete and the safe_substitute() method may be
more appropriate — it will leave placeholders unchanged if data is missing:

Below are a few simple examples.  
 **Example 1:**  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# A Simple Python template example

from string import Template

# Create a template that has placeholder for value of x

t = Template('x is $x')

# Substitute value of x in above template

print (t.substitute({'x' : 1}))  
  
---  
  
 __

 __

 **Output:**  

  

  

    
    
    x is 1

Following is another example where we import names and marks of students from
a list and print them using template.  
 **Example 2:**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# A Python program to demonstrate the

# working of the string template

from string import Template

# List Student stores the name and marks of three students

Student = [('Ram',90), ('Ankit',78), ('Bob',92)]

# We are creating a basic structure to print the name and

# marks of the students.

t = Template('Hi $name, you have got $marks marks')

for i in Student:

 print (t.substitute(name = i[0], marks = i[1]))  
  
---  
  
 __

 __

 **Output:**  

    
    
    Hi Ram, you have got 90 marks
    
    Hi Ankit, you have got 78 marks
    
    Hi Bob, you have got 92 marks

The below example shows the implementation of the safe_substitute method.  
**Example 3:**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from string import Template

template = Template('$name is the $job of $company')

string = template.safe_substitute(name='Raju Kumar',

 job='TCE')

print(string)  
  
---  
  
 __

 __

 **Output:**  

    
    
    Raju Kumar is the TCE of $company

Notice that we have not provided the “$company” placeholder any data, but it
won’t throw an error, rather will return the placeholder as a string as
discussed above.  

### Printing the template String

The “template” attribute of the Template object can be used to return the
template string as shown below:  
**Example:**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

t= Template('I am $name from $city')

print('Template String =', t.template)  
  
---  
  
 __

 __

 **Output:**  

    
    
    Template String = I am $name from $city

  

  

### Escaping $ Sign

The **$$** can be used to escape **$** and treat as part of the string.  
**Example:**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

template= Template('$$ is the symbol for $name')

string = template.substitute(name='Dollar')

print(string)  
  
---  
  
 __

 __

 **Output:**  

    
    
    $ is the symbol for Dollar

### The ${Identifier}

The ${Identifer} works similar to that of $Identifier. It comes in handy when
valid identifier characters follow the placeholder but are not part of the
placeholder.  
**Example:**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

template= Template( 'That $noun looks ${noun}y')

string = template.substitute(noun='Fish')

print(string)  
  
---  
  
 __

 __

 **Output:**  

    
    
    That Fish looks Fishy

Another application for the template is separating program logic from the
details of multiple output formats. This makes it possible to substitute
custom templates for XML files, plain text reports, and HTML web reports.  
Note that there are other ways also to print formatted output like %d for
integer, %f for float, etc (Refer this for details)  
Reference: https://docs.python.org/3.3/tutorial/stdlib2.html  

This article is contributed by **Siddharth Lalwani.** If you like
GeeksforGeeks and would like to contribute, you can also write an article and
mail your article to contribute@geeksforgeeks.org. See your article appearing
on the GeeksforGeeks main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

