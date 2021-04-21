Python – Substituting patterns in text using regex



Regular Expression (regex) is meant for pulling out the required information
from any text which is based on patterns. They are also widely used for
manipulating the pattern-based texts which leads to text preprocessing and are
very helpful in implementing digital skills like **Natural Language
Processing(NLP)**.

This article demonstrates how to use regex to substitute patterns by providing
multiple examples where each example is a unique scenario in its own. It is
very necessary to understand the re.sub() method of re (regular
expression) module to understand the given solutions.

The re.sub() method performs global search and global replace on the given
string. It is used for substituting a specific pattern in the string. There
are in total 5 arguments of this function.

>  **Syntax:** re.sub(pattern, repl, string, count=0, flags=0)
>
>  **Parameters:**  
>  pattern – the pattern which is to be searched and substituted  
> repl – the string with which the pattern is to be replaced  
> string – the name of the variable in which the pattern is stored  
> count – number of characters up to which substitution will be performed  
> flags – it is used to modify the meaning of the regex pattern
>
>  
>
>
>  
>
>
>  **count** and **flags** are optional arguments.

 **Example 1: Substitution of a specific text pattern**  
In this example, a given text pattern will be searched and substituted in a
string. The idea is to use the very normal form of the re.sub() method with
only the first 3 arguments.

Below is the implementation.

 __

 __  
 __

 __

 __  
 __  
 __

# Python implementation of substituting a

# specific text pattern in a string using regex

 

# importing regex module

import re

 

# Function to perform

# operations on the strings

def substitutor():

 

 # a string variable

 sentence1 = "It is raining outside."

 

 # replacing text 'raining' in the string 

 # variable sentence1 with 'sunny' thus

 # passing first parameter as raining

 # second as sunny, third as the 

 # variable name in which string is stored

 # and printing the modified string

 print(re.sub(r"raining", "sunny", sentence1))

 

 # a string variable

 sentence2 = "Thank you very very much."

 

 # replacing text 'very' in the string 

 # variable sentence2 with 'so' thus 

 # passing parameters at their 

 # appropriate positions and printing 

 # the modified string

 print(re.sub(r"very", "so", sentence2))

 

# Driver Code: 

substitutor()  
  
---  
  
 __

 __

 **Output:**

    
    
    It is sunny outside.
    Thank you so so much.
    

> No matter how many time the required pattern is present in the string, the
> re.sub() function replaces all of them with the given pattern. That’s why
> both the ‘very’ are replaced by ‘so’ in the above example.

**Example 2: Substituting a character set with a specific character**  
The task is to replace a character set with a given character. A character set
means a range of characters. In the re.sub() method a character set is
written inside [ ](square brackets).

In this example, the lower case character set i.e., [a-z] will be replaced by
the digit 0. Below is the implementation.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python implementation of substituting

# a character set with a specific character

 

# importing regex module

import re

 

# Function to perform

# operations on the strings

def substitutor():

 

 # a string variable

 sentence = "22 April is celebrated as Earth Day."

 

 # replacing every lower case characters 

 # in the variable sentence with 0 and 

 # printing the modified string

 print(re.sub(r"[a-z]", "0", sentence))

 

# Driver Code: 

substitutor()  
  
---  
  
 __

 __

 **Output:**

    
    
    22 A0000 00 0000000000 00 E0000 D00.
    

> If there is a need to substitute both lowercase and uppercase character set
> then we have to introduce the uppercase character set in this way: [a-zA-Z]
> or the **effective** way to do is by using flags.

**Example 3: Case-insensitive substitution of a character set with a specific
character**  
In this example, both lowercase and uppercase characters will be replaced by
the given character. With the use of **flags** , this task can be carried out
very easily.

The re.I flag stands for re. **IGNORECASE**. By introducing this flag in the
re.sub() method and mentioning any one character set i.e., lowercase or
uppercase the task can be completed.

Below is the implementation.

 __

 __  
 __

 __

 __  
 __  
 __

# Python implementation of case-insensitive substitution

# of a character set with a specific character

 

# importing regex module

import re

 

# Function to perform

# operations on the strings

def substitutor():

 

 # a string variable

 sentence = "22 April is celebrated as Earth Day."

 

 # replacing both lowercase and

 # uppercase characters with 0 in 

 # the variable sentence by using 

 # flag and printing the modified string 

 print(re.sub(r"[a-z]", "0", sentence, flags = re.I))

 

# Driver Code: 

substitutor()  
  
---  
  
 __

 __

 **Output:**

    
    
    22 00000 00 0000000000 00 00000 000.
    

**Example 4: Perform substitution up to a certain number of character**  
In this example, substitution will be up to a specific number of characters
and not on the whole string. To perform this type of substitution the
re.sub() method has an argument count.

By providing a numeric value to this argument, the number of characters on
which substitution will occur can be controlled. Below is the implementation.

 __

 __  
 __

 __

 __  
 __  
 __

# Python implementation to perform substitution

# up to a certain number of characters

 

# importing regex module

import re

 

# Function to perform

# operations on the strings

def substitutor():

 

 # a string variable

 sentence = "Follow your Passion."

 

 # case-insensitive substitution

 # on variable sentence upto 

 # eight characters and printing

 # the modified string

 print(re.sub(r"[a-z]", "0", sentence, 8, flags = re.I))

 

# Driver Code: 

substitutor()  
  
---  
  
 __

 __

 **Output:**

    
    
    000000 00ur Passion.
    

**Example 5: Substitution using shorthand character class and preprocessing of
text**  
Regex module provides many shorthand character class for those character sets
which are very common during preprocessing of text. Usage of shorthand
character class results in writing efficient code and lessen the need to
remember the range of every character set.

To get a detail explanation of shorthand character class and how to write
regular expression in python for preprocessing of text click here. Following
are some of the commonly used shorthand character classes:

> \w: matches alpha numeric characters  
> \W: matches non-alpha numeric characters like @, #, ‘, +, %, –  
> \d: matches digit characters  
> \s: matches white space characters
>
>  **Meaning of some syntax:**  
>  adding a plus(+) symbol after a character class or set: repetition of
> preceding character class or set for at least 1 or more times.
>
> adding an asterisk(*) symbol after a character class or set: repetition of
> preceding character class or set for at least 0 or more times.
>
> adding a caret(^) symbol before a character class or set: matching position
> is determined for that character class or set at the beginning of the
> string.
>
> adding a dollar($) symbol after a character class or set: matching position
> is determined for that character class or set at the end of the string.

This example demonstrates the use of mentioned shorthand character classes for
the substitution and preprocessing of text to get clean and error-free
strings. Below is the implementation.

 __

 __  
 __

 __

 __  
 __  
 __

# Python implementation of Substitution using

# shorthand character class and preprocessing of text

 

# importing regex module

import re

 

# Function to perform

# operations on the strings

def substitutor():

 

 # list of strings

 S = ["2020 Olympic games have @# been cancelled",

 "Dr Vikram Sarabhai was +%--the ISRO’s first chairman",

 "Dr Abdul Kalam, the father of India's missile programme"]

 

 # loop to iterate every element of list

 for i in range(len(S)):

 

 # replacing every non-word character with a white space

 S[i] = re.sub(r"\W", " ", S[i])

 

 # replacing every digit character with a white space

 S[i] = re.sub(r"\d", " ", S[i])

 

 # replacing one or more white space with a single white space

 S[i] = re.sub(r"\s+", " ", S[i])

 

 # replacing alphabetic characters which have one or more 

 # white space before and after them with a white space

 S[i] = re.sub(r"\s+[a-z]\s+", " ", S[i], flags = re.I)

 

 # substituting one or more white space which is at 

 # beginning of the string with an empty string

 S[i] = re.sub(r"^\s+", "", S[i])

 

 # substituting one or more white space which is at

 # end of the string with an empty string

 S[i] = re.sub(r"\s+$", "", S[i])

 

 # loop to iterate every element of list

 for i in range(len(S)):

 

 # printing each modified string

 print(S[i])

 

# Driver Code: 

substitutor()   
  
---  
  
__

__

**Output:**

    
    
    Olympic games have been cancelled
    Dr Vikram Sarabhai was the ISRO first chairman
    Dr Abdul Kalam the father of India missile programme
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

