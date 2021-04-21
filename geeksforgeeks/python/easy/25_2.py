Python | Check for URL in a String



 **Prerequisite :** Pattern matching with Regular Expression

In this article, we will need to accept a string and we need to check if the
string contains any URL in it. If the URL is present in the string, we will
say URL’s been found or not and print the respective URL present in the
string. We will use the concept of Regular Expression of Python to solve the
problem.

Examples:

    
    
    Input : string = 'My Profile: 
    https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles 
    in the portal of http://www.geeksforgeeks.org/'
    
    Output : URLs :  ['https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles',
    'http://www.geeksforgeeks.org/']
    
    Input : string = 'I am a blogger at https://geeksforgeeks.org'
    Output : URL :  ['https://geeksforgeeks.org']
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

To find the URLs in a given string we have used the findall() function from
the regular expression module of Python. This return all non-overlapping
matches of pattern in string, as a list of strings. The string is scanned
left-to-right, and matches are returned in the order found.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to find the URL from an input string

# Using the regular expression

import re

 

def Find(string):

 

 # findall() has been used 

 # with valid conditions for urls in string

 regex =
r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s!()\[\]{};:'\".,<>?«»“”‘’]))"

 url = re.findall(regex,string) 

 return [x[0] for x in url]

 

# Driver Code

string = 'My Profile:
https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of
http://www.geeksforgeeks.org/'

print("Urls: ", Find(string))  
  
---  
  
 __

 __

Output:

    
    
    Urls:  ['https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles',
    'http://www.geeksforgeeks.org/']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

