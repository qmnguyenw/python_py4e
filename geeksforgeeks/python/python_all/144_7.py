Python program to convert camel case string to snake case



Given a string in camel case, write a Python program to convert the given
string from camel case to snake case.  
 **Examples:**

    
    
    **Input :** GeeksForGeeks
    **Output :** geeks_for_geeks
    
    **Input :** ThisIsInCamelCase
    **Output :** this_is_in_camel_case

Let’s see the different ways we can do this task.  
**Method #1 :** Naive Approach  
This is a naive implementation to convert camel case to snake case. First, we
initialize a variable ‘res’ with an empty list and append first character (in
lower case) to it. Now, Each time we encounter a Capital alphabet, we append
‘_’ and the alphabet (in lower case) to ‘res’, otherwise, just append the
alphabet only.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to convert string

# from camel case to snake case

def change_case(str):

 res = [str[0].lower()]

 for c in str[1:]:

 if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):

 res.append('_')

 res.append(c.lower())

 else:

 res.append(c)

 

 return ''.join(res)

 

# Driver code

str = "GeeksForGeeks"

print(change_case(str))  
  
---  
  
 __

 __

 **Output:**

    
    
    geeks_for_geeks

  
**Method #2 :** List comprehension

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to convert string

# from camel case to snake case

def change_case(str):

 

 return ''.join(['_'+i.lower() if i.isupper()

 else i for i in str]).lstrip('_')

 

# Driver code

str = "GeeksForGeeks"

print(change_case(str))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    geeks_for_geeks

