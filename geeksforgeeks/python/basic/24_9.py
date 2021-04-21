isupper(), islower(), lower(), upper() in Python and their applications



 **isupper()**

In Python, isupper() is a built-in method used for string handling.  
The isupper() methods returns “True” if all characters in the string are
uppercase, Otherwise, It returns “False”.  
This function is used to check if the argument contains any uppercase
characters such as :

    
    
    ABCDEFGHIJKLMNOPQRSTUVWXYZ 

**Syntax :**

    
    
    **string.isupper()**
    **Parameters:**
    isupper() does not take any parameters
    **Returns :**
    1.True- If all characters in the string are uppercase.
    2.False- If the string contains 1 or more non-uppercase characters.
    

Examples:

    
    
    Input : string = 'GEEKSFORGEEKS'
    Output : True
    
    Input : string = 'GeeksforGeeks'
    Output : False
    

**Errors And Exceptions**

  

  

  1. It returns “True” for whitespaces
  2. It does not take any arguments, Therefore, It returns an error if a parameter is passed.
  3. Digits and symbols return “True”, Only an uppercase letter returns “false”.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code for implementation of isupper()

 

# checking for uppercase characters

string = 'GEEKSFORGEEKS'

print(string.isupper())

 

string = 'GeeksforGeeks'

print(string.isupper())  
  
---  
  
 __

 __

Output:

    
    
    True
    False
    

**islower()**

In Python, islower() is a built-in method used for string handling.  
The islower() methods returns “True” if all characters in the string are
lowercase, Otherwise, It returns “False”.  
This function is used to check if the argument contains any lowercase
characters such as :

    
    
    abcdefghijklmnopqrstuvwxyz 

**Syntax :**

    
    
    **string.islower()**
    **Parameters:**
    islower() does not take any parameters
    **Returns :**
    1.True- If all characters in the string are lower.
    2.False- If the string contains 1 or more non-lowercase characters.
    

Examples:

    
    
    Input : string = 'geeksforgeeks'
    Output : True
    
    Input : string = 'GeeksforGeeks'
    Output : False
    

**Errors And Exceptions**

  1. It returns “True” for whitespaces
  2. It does not take any arguments, Therefore, It returns an error if a parameter is passed.
  3. Digits and symbols return “True”, Only a lowercase letter returns “false”.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code for implementation of isupper()

 

# checking for lowercase characters

string = 'geeksforgeeks'

print(string.islower())

 

string = 'GeeksforGeeks'

print(string.islower())  
  
---  
  
 __

 __

Output:

    
    
    True
    False
    

**lower()**

  

  

In Python, lower() is a built-in method used for string handling.  
The lower() methods returns the lowercased string from the given string. It
converts all uppercase characters to lowercase. If no uppercase characters
exist, it returns the original string.

 **Syntax :**

    
    
    **string.lower()**
    **Parameters:**
    lower() does not take any parameters
    **Returns :**
    It converts the given string in into lowercase and returns the string.
    

Examples:

    
    
    Input : string = 'GEEKSFORGEEKS'
    Output : geeksforgeeks
    
    Input : string = 'GeeksforGeeks'
    Output : geeksforgeeks
    

**Errors And Exceptions**

  1. It does not take any arguments, Therefore, It returns an error if a parameter is passed.
  2. Digits and symbols return are returned as it is, Only an uppercase letter is returned after converting to lowercase.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code for implementation of lower()

 

# Checking for lowercase characters

string = 'GEEKSFORGEEKS'

print(string.lower())

 

string = 'GeeksforGeeks'

print(string.lower())  
  
---  
  
 __

 __

Output:

    
    
    geeksforgeeks
    geeksforgeeks
    

**upper()**

In Python, upper() is a built-in method used for string handling.  
The upper() methods returns the uppercased string from the given string. It
converts all lowercase characters to uppercase.If no lowercase characters
exist, it returns the original string.

 **Syntax :**

    
    
    **string.upper()**
    **Parameters:**
    upper() does not take any parameters
    **Returns :**
    It converts the given string in into uppercase and returns the string.
    

Examples:

    
    
    Input : string = 'geeksforgeeks'
    Output : GEEKSFORGEEKS
    
    Input : string = 'My name is ayush'
    Output : MY NAME IS AYUSH
    

**Errors And Exceptions**

  1. It does not take any arguments, Therefore, It returns an error if a parameter is passed.
  2. Digits and symbols return are returned as it is, Only a lowercase letter is returned after converting to uppercase.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code for implementation of upper()

 

# checking for uppercase characters

string = 'geeksforgeeks'

print(string.upper())

 

string = 'My name is ayush'

print(string.upper())  
  
---  
  
 __

 __

Output:

    
    
    GEEKSFORGEEKS
    MY NAME IS AYUSH
    

**Application :** Given a string in python, count number of uppercase letters,
lowercase letters and spaces in a string and toggle case the given string
(convert lowercase to uppercase and vice versa).

 **Examples:**

    
    
    Input : string = 'GeeksforGeeks is a computer Science portal for Geeks'
    Output : Uppercase - 4
             Lowercase - 41
             spaces - 7
             gEEKSFORGEEKS IS A COMPUTER sCIENCE PORTAL FOR gEEKS
    
    Input : string = 'My name is Ayush'
    Output : Uppercase - 2
             Lowercase - 11
             spaces - 3
             mY NAME IS aYUSH
    

**Algorithm**  
1\. Traverse the given string character by character upto its length, check if
character is in lowercase or uppercase using built in methods.  
2\. If lowercase, increment its respective counter, convert it to uppercase
using upper() function and add it to a new string, if uppercase, increment its
respective counter, convert it to lowercase using lower() function and add it
to the new string.  
3\. If space, increment its respective counter and add it to a new string  
4\. Print the new string.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code for implementation of upper()

# Given string and new string 

 

string ='GeeksforGeeks is a computer Science portal for Geeks'

newstring ='' 

count1 = 0

count2 = 0

count3 = 0

 

for a in string: 

# Checking for lowercase letter and 

# converting to uppercase. 

 if (a.isupper()) == True: 

 count1+= 1

 newstring+=(a.lower()) 

# Checking for uppercase letter and

# converting to lowercase. 

 elif (a.islower()) == True: 

 count2+= 1

 newstring+=(a.upper()) 

# Checking for whitespace letter and

# adding it to the new string as it is. 

 elif (a.isspace()) == True: 

 count3+= 1

 newstring+= a 

print("In original String : ") 

print("Uppercase -", count1) 

print("Lowercase -", count2) 

print("Spaces -", count3) 

 

print("After changing cases:") 

print(newstring)   
  
---  
  
__

__

**Output:**

    
    
    In original String : 
    Uppercase - 4
    Lowercase - 41
    Spaces - 7
    After changing cases:
    gEEKSFORgEEKS IS A COMPUTER sCIENCE PORTAL FOR gEEKS
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

