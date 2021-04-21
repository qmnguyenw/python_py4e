Interesting Fact about Python Multi-line Comments



 **Multi-line comments** (comments block) are used for description of large
text of code or comment out chunks of code at the time of **debugging
application**.

 **Does Python Support Multi-line Comments(like c/c++…)?**  
Actually in many online tutorial and webstie you will find that
multiline_comments are avilable in python(“”” or ”’). but let’s first look at
what python creator, “Guido van Rossum” said about fake block commenting style
:

 **Python tip:** You can use multi-line strings as multi-line comments. Unless
used as docstring, they generate no code!.  
source_file

  * if writing a text in a single line then use double quotes or single quotes in python.
  * if writing a poem or songs or multi-line text then to use triple quotes(“”” or ”’).
    
    
    **both two points do not give any error because text within single quotes or 
    double quotes or tripple quotes can be considered as text-constant**

  * if printing these lines or text then simply insert it in print() function.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Write Python3 code here

#this is only valid for single line

 

"this is a text constant for single line you"

"can't use multi-line within single or double quotes"

 

'this is also text-constant for single line'

 

#this is valid for multiline.

"""this is text constant for multi

or single line this will not

give any error"""

 

#you can also print both look at below..

print('this is also text-constant for single line')

print("""this is text constant for mult-line

or single line this will not

give any error""")  
  
---  
  
 __

 __

The above technique does not create true comments. It simply inserts Text
constant that does not change anything or say that this is a regular single
line string somewhere in your code. Always keep in mind to indent the first (
**“”” or ”’** ) match correctly, otherwise a SyntaxError is generated.

  

  

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Write Python3 code here

def check_syntax():

 """

 look at your first ident

 below"""

print("after this line interpreter gives error because your first ident
doesnot match")

 """ <---- here first ident starts with 2nd column hence gives identation
error you must remember that your first ident must be correctly matched.

"""  
  
---  
  
 __

 __

 **How we comment out chunks of code easily?**  
Simply select those lines(it means when to copy the text then first select
those lines) and then press (cntrl+#) otherwise consecutive # in every lines
is the only way.  
 **Summary:**

* Unlike other programming languages (c, c++, …) “python” does not support multi-line comment blocks out of the box.
* One can consider triple quote “”” as multi-line comments but this is not a good idea because this type of comments lines may turn into accidental docstrings.
* consecutive # is the only way to comments lines in python(if you want to comment more than one lines then you can select those lines and press (ctrl+#) in python3.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

