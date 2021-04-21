Python Regex: re.search() VS re.findall()



 **Prerequisite:** Regular Expression with Examples | Python

A Regular expression (sometimes called a Rational expression) is a sequence of
characters that define a search pattern, mainly for use in pattern matching
with strings, or string matching, i.e. “find and replace”-like operations.
Regular expressions are a generalized way to match patterns with sequences of
characters.

Module _Regular Expressions (RE)_ specifies a set of strings (pattern) that
matches it. To understand the RE analogy, MetaCharacters are useful,
important and will be used in functions of module re.

There are a total of 14 metacharacters and will be discussed as they follow
into functions:

    
    
    \   Used to drop the special meaning of character
        following it (discussed below)
    []  Represent a character class
    ^   Matches the beginning
    $   Matches the end
    .   Matches any character except newline
    ?   Matches zero or one occurrence.
    |   Means OR (Matches with any of the characters
        separated by it.
    *   Any number of occurrences (including 0 occurrences)
    +   One ore more occurrences
    {}  Indicate number of occurrences of a preceding RE 
        to match.
    ()  Enclose a group of REs
    

#### re.search()

re.search() method either returns None (if the pattern doesn’t match), or a
re.MatchObject that contains information about the matching part of the
string. This method stops after the first match, so this is best suited for
testing a regular expression more than extracting data.

  

  

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# A Python program to demonstrate working of re.match().

import re 

 

# Lets use a regular expression to match a date string 

# in the form of Month name followed by day number 

regex = r"([a-zA-Z]+) (\d+)"

 

match = re.search(regex, "I was born on June 24") 

 

if match != None: 

 

 # We reach here when the expression "([a-zA-Z]+) (\d+)" 

 # matches the date string. 

 

 # This will print [14, 21), since it matches at index 14 

 # and ends at 21. 

 print("Match at index % s, % s" % (match.start(), match.end()))

 

 # We us group() method to get all the matches and 

 # captured groups. The groups contain the matched values. 

 # In particular: 

 # match.group(0) always returns the fully matched string 

 # match.group(1) match.group(2), ... return the capture 

 # groups in order from left to right in the input string 

 # match.group() is equivalent to match.group(0) 

 

 # So this will print "June 24" 

 print("Full match: % s" % (match.group(0)))

 

 # So this will print "June" 

 print("Month: % s" % (match.group(1)))

 

 # So this will print "24" 

 print("Day: % s" % (match.group(2)))

 

else: 

 print("The regex pattern does not match.")  
  
---  
  
 __

 __

 **Output:**

    
    
    Match at index 14, 21
    Full match: June 24
    Month: June
    Day: 24
    

#### re.findall()

Return all non-overlapping matches of pattern in string, as a list of strings.
The string is scanned left-to-right, and matches are returned in the order
found.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# A Python program to demonstrate working of

# findall() 

import re 

 

# A sample text string where regular expression 

# is searched. 

string = """Hello my Number is 123456789 and 

 my friend's number is 987654321"""

 

# A sample regular expression to find digits. 

regex = '\d+'

 

match = re.findall(regex, string) 

print(match)   
  
---  
  
__

__

**Output:**

    
    
    ['123456789', '987654321']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

