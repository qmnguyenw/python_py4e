Python | Remove the given substring from end of string



Sometimes we need to manipulate our string to remove extra information from
string for better understanding and faster processing. Given a task in which
substring needs to be removed from the end of the string. Given below are a
few methods to solve the given task.  

**Method #1: Using Naive Method**

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to remove a substring from end of the string

 

# Initialising string

ini_string = 'xbzefdgstb'

 

# initializing string

sstring = 'stb'

 

# printing initial string and substring

print ("initial_strings : ", ini_string, "\nsubstring : ",
sstring)

 

# removing substring from end

# of string using Naive Method

if ini_string.endswith(sstring):

 res = ini_string[:-(len(sstring))]

 

# printing result

print ("resultant string", res)  
  
---  
  
 __

 __

 **Output:**

    
    
    initial_strings :  xbzefdgstb 
    substring :  stb
    resultant string xbzefdg
    

  
**Method #2: Usingsub() method**

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to remove a substring from end of string

 

import re

 

# Initialising string

ini_string = 'xbzefdgstb'

 

# initializing string

sstring = 'stb'

 

# printing initial string and substring

print ("initial_strings : ", ini_string, "\nsubstring : ",
sstring)

 

# removing substring from end

# of string using sub Method

if ini_string.endswith(sstring):

 res = re.sub(sstring, '', ini_string)

 

# printing result

print ("resultant string", res)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    initial_strings :  xbzefdgstb 
    substring :  stb
    resultant string xbzefdg
    

