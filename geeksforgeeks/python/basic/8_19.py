Python – Convert simple lines to bulleted lines using the Pyperclip module



 **Pyperclip** is the cross-platform Python module which is used for copying
and pasting the text to the clipboard. Let’s suppose you want to automate the
task of copying the text and then convert them to the bulleted points. This
can be done using the pyperclip module. Consider the below examples for
better understanding.

 **Examples:**

>  **Clipboard Content :**  
>  United we stand, divided we fall.  
> Where there is a will, there is a way.  
> Rome was not built in a day.
>
>  **New clipboard Content :**  
>  * United we stand, divided we fall.  
> * Where there is a will, there is a way.  
> * Rome was not built in a day.

 **Approach:** First, you need to copy whatever text you want to convert to
bulleted text then you need to run the program and after its successful
execution when you paste the contents of clipboard you can see that the
contents have been already modified. Two methods of this module have been used
i.e. paste() method which is used to paste as well as return the copied
string and copy() which is used to pass the string to the clipboard.

  

  

Below is the implementation.

 __

 __  
 __

 __

 __  
 __  
 __

import pyperclip

 

 

# saves text copied to clipboard

# in variable text

text = pyperclip.paste()

print("Before Modification:")

print(text)

 

# stores different lines of text

# in a list named lines

lines = text.split("\n")

 

# adds * to every line stored

# in list

for i in range(len(lines)):

 lines[i] = "*" + lines[i]

 

# converts the list of different

# lines to single text

text = "\n".join(lines)

 

# copies new modified text

# to the clipboard

pyperclip.copy(text)

print("\nAfter Modification:") 

print(pyperclip.paste())  
  
---  
  
 __

 __

 **Output:**

    
    
    Before Modification:
    United we stand, divided we fall.
    Where there is a will, there is a way.
    Rome was not built in a day.
    
    After Modification:
    *United we stand, divided we fall.
    *Where there is a will, there is a way.
    *Rome was not built in a day.
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

