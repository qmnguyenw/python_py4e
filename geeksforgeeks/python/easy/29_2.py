Textwrap – Text wrapping and filling in Python



The textwrap module can be used for wrapping and formatting of plain text.
This module provides formatting of text by adjusting the line breaks in the
input paragraph.

The TextWrapper instance attributes (and keyword arguments to the constructor)
are as follows:

  *  **width:** This refers to the maximum length allowed of the wrapped lines. It’s default value is set to 70.
  *  **expand_tabs:** It’s default value is set to TRUE. If the value is equal to true, then, all the tab characters in the sample input is expanded to spaces using this method.
  *  **tabsize:** It’s default value is set to 8. This method expands all tab characters in text to zero or more spaces, depending on the current column and the given tab size, if the value of expand_tabs is TRUE.
  *  **replace_whitespace:** It’s default value is set to TRUE. If the value is true, after tab expansion but before wrapping, the wrap() method replaces each whitespace character with a single space.These whitespace characters are replaced : tab, newline, vertical tab, formfeed, and carriage return (‘\t\n\v\f\r’).
  *  **drop_whitespace:** It’s default value is set to TRUE. The whitespaces at the beginning and ending of every line (after wrapping but before indenting) is dropped if the value is set to TRUE.
  *  **initial_indent:** It’s default value is set to’ ‘. This method prepends the given string to the first line of wrapped output.
  *  **subsequent_indent:** It’s default value is set to ‘ ‘. This method prepends the given string to all the lines of wrapped output except the first.
  *  **placeholder:** It’s default value is set to ‘ […]’. This method appends the string at the end of the output text if it has been truncated.
  *  **max_lines:** It’s default value is set to None. If the value is not None, then the output text contains at most max_lines lines, having placeholder at the end of the output.
  *  **break_long_words:** It’s default value is set to True. If TRUE, then words longer than width are broken to fit every line in the given width. If it is FALSE, long words will not be broken and will be put on a line by themselves, in order to minimize the amount by which width is exceeded.
  *  **break_on_hyphens:** It’s default value is set to True. If the value is equal to TRUE, wrapping occurs on whitespaces and right after hyphens in compound words. If the value is equal to FALSE, line breaks occur only on whitespaces, but you need to set break_long_words to FALSE if you want truly insecable words.

 **Functions provided by the Textwrap module :**

  1.  **textwrap.wrap(text, width=70, **kwargs)** : This function wraps the input paragraph such that each line in the paragraph is at most width characters long. The wrap method returns a list of output lines. The returned list is empty if the wrapped output has no content. Default width is taken as 70.

 __

 __  
 __

 __

 __  
 __  
 __

import textwrap

 

value = """This function wraps the input paragraph such that each line

in the paragraph is at most width characters long. The wrap method

returns a list of output lines. The returned list

is empty if the wrapped

output has no content."""

 

# Wrap this text.

wrapper = textwrap.TextWrapper(width=50)

 

word_list = wrapper.wrap(text=value)

 

# Print each line.

for element in word_list:

 print(element)  
  
---  
  
 __

 __

 **Output :**

    
    
    This function wraps the input paragraph such that
    each line in the paragraph is at most width
    characters long. The wrap method returns a list of
    output lines. The returned list is empty if the
    wrapped output has no content.
    

  2. **textwrap.fill(text, width=70, **kwargs):** The fill() convenience function works similar to textwrap.wrap except it returns the data joined into a single, newline-separated string. This function wraps the input single paragraph in text, and returns a single string containing the wrapped paragraph.

 __

 __  
 __

 __

 __  
 __  
 __

import textwrap

 

value = """This function returns the answer as STRING and not LIST."""

 

# Wrap this text.

wrapper = textwrap.TextWrapper(width=50)

 

string = wrapper.fill(text=value)

 

print (string)  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    This function returns the answer as STRING and not LIST.
    

  3. **textwrap.dedent(text)** : This function is used to remove any common leading whitespace from every line in the input text. This allows to use docstrings or embedded multi-line strings line up with the left edge of the display, while removing the formatting of the code itself.

 **Example :**

 __

 __  
 __

 __

 __  
 __  
 __

import textwrap

 

wrapper = textwrap.TextWrapper(width=50)

 

s = '''\

 hello

 world

 '''

print(repr(s)) # prints ' hello\n world\n '

 

text = textwrap.dedent(s)

print(repr(text)) # prints 'hello\n world\n'  
  
---  
  
 __

 __

 **Output :**

    
    
    '    hello\n      world\n    '
    'hello\n  world\n'
    

  4. **textwrap.shorten(text, width, **kwargs)** : This function truncates the input string so that the length of the string becomes equal to the given width. At first, all the whitespaces are collapsed in the string by removing the whitespaces with a single space. If the modified string fits in the given string, then it is returned otherwise, the characters from the end are dropped so that the remaining words plus the placeholder fit within width.

 __

 __  
 __

 __

 __  
 __  
 __

import textwrap

 

sample_text = """This function wraps the input paragraph such that each
line

n the paragraph is at most width characters long. The wrap method

returns a list of output lines. The returned list

is empty if the wrapped

output has no content."""

 

wrapper = textwrap.TextWrapper(width=50)

 

dedented_text = textwrap.dedent(text=sample_text)

original = wrapper.fill(text=dedented_text)

 

print('Original:\n')

print(original)

 

shortened = textwrap.shorten(text=original, width=100)

shortened_wrapped = wrapper.fill(text=shortened)

 

print('\nShortened:\n')

print(shortened_wrapped)  
  
---  
  
 __

 __

 **Output :**

    
    
    Original:
    
    This function wraps the input paragraph such that
    each line n the paragraph is at most width
    characters long. The wrap method returns a list of
    output lines. The returned list is empty if the
    wrapped output has no content.
    
    Shortened:
    
    This function wraps the input paragraph such that
    each line n the paragraph is at most width [...]
    

  5. **textwrap.indent(text, prefix, predicate=None)** : This function is used to add the given prefix to the beginning of the selected lines of the text. The predicate argument can be used to control which lines are indented.

 __

 __  
 __

 __

 __  
 __  
 __

import textwrap

 

s = 'hello\n\n \nworld'

s1 = textwrap.indent(text=s, prefix=' ')

 

print (s1)

print ("\n")

 

s2 = textwrap.indent(text=s, prefix='+ ', predicate=lambda
line: True)

print (s2)  
  
---  
  
 __

 __

 **Output :**

    
    
    hello
    
     
    world
    
    
    + hello
    + 
    +  
    + world
    

