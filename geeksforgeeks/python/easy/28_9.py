Pattern matching in Python with Regex



Prerequisite: Regular Expressions in Python

You may be familiar with searching for text by pressing ctrl-F and typing in
the words you’re looking for. Regular expressions go one step further: They
allow you to specify a pattern of text to search for.  
Regular expressions, called regexes for short, are descriptions for a pattern
of text. For example, a \d in a regex stands for a digit character — that is,
any single numeral 0 to 9.

  * Following regex is used in Python to match a string of three numbers, a hyphen, three more numbers, another hyphen, and four numbers.
    
        Any other string would not match the pattern.
    \d\d\d-\d\d\d-\d\d\d\d

  * Regular expressions can be much more sophisticated. For example, adding a 3 in curly brackets ({3}) after a pattern is like saying, “ Match this pattern three times.” So the slightly shorter regex
    
        \d{3}-\d{3}-\d{4}

(It matches the correct phone number format.)

 **Creating Regex object**

All the regex functions in Python are in the re module

    
    
    import re

To create a Regex object that matches the phone number pattern, enter the
following into the interactive shell.

  

  

    
    
    phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

Now the phoneNumRegex variable contains a Regex object.

 **Matching regex objects**

A Regex object’s search() method searches the string it is passed for any
matches to the regex. Match objects have a group() method that will return the
actual matched text from the searched string.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate

# Matching regex objects

import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = phoneNumRegex.search('My number is 415-555-4242.')

print('Phone number found: ' + mo.group())  
  
---  
  
 __

 __

Output:

    
    
    Phone number found: 415-555-4242

 **Steps of Regular Expression Matching**

While there are several steps to using regular expressions in Python, each
step is fairly simple.

  1. Import the regex module with import re.
  2. Create a Regex object with the re.compile() function. (Remember to use a raw string.)
  3. Pass the string you want to search into the Regex object’s search() method. This returns a Match object.
  4. Call the Match object’s group() method to return a string of the actual matched text.

 **Grouping with parentheses**

    1.  **Matching objects:** Say you want to separate the area code from the rest of the phone number. Adding parentheses will create groups in the regex: (\d\d\d)-(\d\d\d-\d\d\d\d). Then you can use the group() match object method to grab the matching text from just one group.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate

# Matching regex objects

# with grouping 

import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

mo = phoneNumRegex.search('My number is 415-555-4242.')

print(mo.group(1))  
  
---  
  
 __

 __

OUTPUT:

  

  

        
        
        '415'
        

    2. **Retrieve all the groups at once :** If you would like to retrieve all the groups at once, use the groups(), method—note the plural form for the name.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate

# Matching regex objects

# with groups 

import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

mo = phoneNumRegex.search('My number is 415-555-4242.')

print(mo.groups())  
  
---  
  
 __

 __

OUTPUT:

        
        
        ('415', '555-4242')

    3.  **Using mo.groups :** mo.groups() will return a tuple of multiple values, you can use the multiple-assignment trick to assign each value to a separate variable, as in the following areaCode, mainNumber = mo.groups() line.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate

# Matching regex objects

# with mo.groups() 

import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

mo = phoneNumRegex.search('My number is 415-555-4242.')

areaCode, mainNumber = mo.groups()

print(mainNumber)  
  
---  
  
 __

 __

OUTPUT:

        
        
        '555-4242'

    4.  **Match a parenthesis :** Parentheses have a special meaning in regular expressions, but what do you do if you need to match a parenthesis in your text. For instance, maybe the phone numbers you are trying to match have the area code set in parentheses. In this case, you need to escape the ( and ) characters with a backslash. Enter the following into the interactive shell:

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate

# Matching regex objects

# with grouping 

import re

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')

mo = phoneNumRegex.search('My phone number is (415) 555-4242.')

print(mo.group(1))  
  
---  
  
 __

 __

OUTPUT:

        
        
        '(415)'

The \\( and \\) escape characters in the raw string passed to re.compile()
will match actual parenthesis characters.

 **Matching Multiple Groups with the Pipe**

The | character is called a pipe. You can use it anywhere you want to match
one of many expressions. For example, the regular expression r’Batman|Tina
Fey’ will match either ‘Batman’ or ‘Tina Fey’.

When both Batman and Tina Fey occur in the searched string, the first
occurrence of matching text will be returned as the Match object. Enter the
following into the interactive shell:

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate

# Matching regex objects

# with multiple Groups with the Pipe

import re

heroRegex = re.compile (r'Batman|Tina Fey')

mo1 = heroRegex.search('Batman and Tina Fey.')

print(mo1.group())  
  
---  
  
 __

 __

OUTPUT:

    
    
    'Batman'

 **Matching Specific Repetitions with Curly Brackets**

If you have a group that you want to repeat a specific number of times, follow
the group in your regex with a number in curly brackets. For example, the
regex (Ha){3} will match the string ‘HaHaHa’, but it will not match ‘HaHa’,
since the latter has only two repeats of the (Ha) group.

Instead of one number, you can specify a range by writing a minimum, a comma,
and a maximum in between the curly brackets. For example, the regex (Ha){3, 5}
will match ‘HaHaHa’, ‘HaHaHaHa’, and ‘HaHaHaHaHa’.

You can also leave out the first or second number in the curly brackets to
leave the minimum or maximum unbounded. For example, (Ha){3, } will match
three or more instances of the (Ha) group, while (Ha){, 5} will match zero to
five instances. Curly brackets can help make your regular expressions shorter.
These two regular expressions match identical patterns:

    
        (Ha){3}
    (Ha)(Ha)(Ha)

And these two regular expressions also match identical patterns:

    
        (Ha){3, 5}
    ((Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha)(Ha))

Enter the following into the interactive shell:

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate

# Matching Specific Repetitions 

# with Curly Brackets

import re

haRegex = re.compile(r'(Ha){3}')

mo1 = haRegex.search('HaHaHa')

print(mo1.group())  
  
---  
  
 __

 __

OUTPUT:

    
    
    'HaHaHa'

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate

# Matching Specific Repetitions 

# with Curly Brackets

import re

haRegex = re.compile(r'(Ha){3}')

mo2 = haRegex.search('Ha')== None

print(mo2)  
  
---  
  
 __

 __

OUTPUT:

    
    
    True
    

Here, (Ha){3} matches ‘HaHaHa’ but not ‘Ha’. Since it doesn’t match ‘Ha’,
search() returns None.

 **Optional Matching with the Question Mark**

Sometimes there is a pattern that you want to match only optionally. That is,
the regex should find a match whether or not that bit of text is there. The
**?** character flags the group that precedes it as an optional part of the
pattern. For example, enter the following into the interactive shell:

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate

# optional matching

# with question mark(?)

import re

batRegex = re.compile(r'Bat(wo)?man')

mo1 = batRegex.search('The Adventures of Batman')

print(mo1.group())  
  
---  
  
 __

 __

OUTPUT:

    
    
    'Batman'

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate

# optional matching

# with question mark(?)

import re

batRegex = re.compile(r'Bat(wo)?man')

mo2 = batRegex.search('The Adventures of Batwoman')

print(mo2.group())  
  
---  
  
 __

 __

OUTPUT:

    
    
    'Batwoman'

The (wo)? part of the regular expression means that the pattern wo is an
optional group. The regex will match text that has zero instances or one
instance of wo in it. This is why the regex matches both ‘Batwoman’ and
‘Batman’.  
You can think of the ? as saying, **“Match zero or one of the group preceding
this question mark.”**  
If you need to match an actual question mark character, escape it with \?.

 **Matching Zero or More with the Star**

The * (called the star or asterisk) means “match zero or more”—the group that
precedes the star can occur any number of times in the text. It can be
completely absent or repeated over and over again. Let’s look at the Batman
example again.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate

# matching a regular expression

# with asterisk(*)

import re

batRegex = re.compile(r'Bat(wo)*man')

mo1 = batRegex.search('The Adventures of Batman')

print(mo1.group())  
  
---  
  
 __

 __

OUTPUT:

    
    
    'Batman'

 __

 __  
 __

 __

 __  
 __  
 __

#python program to illustrate

#matching a regular expression

#with asterisk(*)

import re

batRegex = re.compile(r'Bat(wo)*man')

mo2 = batRegex.search('The Adventures of Batwoman')

print(mo2.group())  
  
---  
  
 __

 __

OUTPUT:

    
    
    'Batwoman'

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate

# matching a regular expression

# with asterisk(*)

import re

batRegex = re.compile(r'Bat(wo)*man')

mo3 = batRegex.search('The Adventures of Batwowowowoman')

print(mo3.group())  
  
---  
  
 __

 __

OUTPUT:

    
    
    'Batwowowowoman'

For ‘Batman’, the (wo)* part of the regex matches zero instances of wo in the
string; for ‘Batwoman’, the (wo)* matches one instance of wo; and for
‘Batwowowowoman’, (wo)* matches four instances of wo.

If you need to match an actual star character, prefix the star in the regular
expression with a backslash, \\*.

 **Matching One or More with the Plus**

While * means “match zero or more, ” the + (or plus) means **“match one or
more.”** Unlike the star, which does not require its group to appear in the
matched string, the group preceding a plus must appear at least once. It is
not optional. Enter the following into the interactive shell, and compare it
with the star regexes in the previous section:

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate

# matching a regular expression

# with plus(+)

import re

batRegex = re.compile(r'Bat(wo)+man')

mo1 = batRegex.search('The Adventures of Batwoman')

print(mo1.group())  
  
---  
  
 __

 __

OUTPUT:

    
    
    'Batwoman'

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate

# matching a regular expression

# with plus(+)

import re

batRegex = re.compile(r'Bat(wo)+man')

mo2 = batRegex.search('The Adventures of Batwowowowoman')

print(mo2.group())  
  
---  
  
 __

 __

OUTPUT:

    
    
    'Batwowowowoman'

batRegex = re.compile(r’Bat(wo)+man’)

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate

# matching a regular expression

# with plus(+)

import re

batRegex = re.compile(r'Bat(wo)+man')

mo3 = batRegex.search('The Adventures of Batman')== None

print(mo3)  
  
---  
  
 __

 __

OUTPUT:

    
    
    True

The regex Bat(wo)+man will not match the string ‘The Adventures of Batman’
because at least one wo is required by the plus sign.

If you need to match an actual plus sign character, prefix the plus sign with
a backslash to escape it: \\+.

This article is contributed by **Shubham Machal**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
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

