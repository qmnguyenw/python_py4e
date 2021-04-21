Python program to split and join a string



Python program to Split a string based on a delimiter and join the string
using another delimiter.

Split a string can be quite useful sometimes, especially when you need only
certain parts of strings. A simple yet effective example is splitting the
First-name and Last-name of a person. Another application is CSV(Comma
Separated Files). We use split to get data from CSV and join to write data to
CSV.

In Python, we can use the function **_split()_** to split a string and
**_join()_** to join a string. For detailed article on split() and join()
functions, refer these : split() in Python and join() in Python.

Examples :

    
    
    **Split the string into list of strings**
    
    Input : Geeks for Geeks
    Output : ['Geeks', 'for', 'Geeks']
    
    
    **Join the list of strings into a string based on delimiter ('-')**
    
    Input :  ['Geeks', 'for', 'Geeks']
    Output : Geeks-for-Geeks
    

  

  

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

Below is Python code to Split and Join the string based on a delimiter :

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to split a string and

# join it using different delimiter

 

def split_string(string):

 

 # Split the string based on space delimiter

 list_string = string.split(' ')

 

 return list_string

 

def join_string(list_string):

 

 # Join the string based on '-' delimiter

 string = '-'.join(list_string)

 

 return string

 

# Driver Function

if __name__ == '__main__':

 string = 'Geeks for Geeks'

 

 # Splitting a string

 list_string = split_string(string)

 print(list_string)

 

 # Join list of strings into one

 new_string = join_string(list_string)

 print(new_string)  
  
---  
  
 __

 __

Output :

    
    
    ['Geeks', 'for', 'Geeks']
    Geeks-for-Geeks
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

