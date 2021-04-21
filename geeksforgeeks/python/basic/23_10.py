Python | Program to convert String to a List



In this program, we will try to convert a given string to a list, where spaces
or any other special characters, according to the users choice, are
encountered. To do this we use the split() method.  
 **Syntax:**

    
    
     **string.split("delimiter")**

Examples:

    
    
    Input : "Geeks for Geeks"
    Output : ['Geeks', 'for', 'Geeks']
    
    Input : "Geeks-for-Geeks"
    Output : ['Geeks', 'for', 'Geeks']
    

The split method is used to split the strings and store them in the list. The
built-in method returns a list of the words in the string, using the
“delimiter” as the delimiter string. If a delimiter is not specified or is
None, a different splitting algorithm is applied: runs of consecutive
whitespace are regarded as a single separator, and the result will contain no
empty strings at the start or end if the string has leading or trailing
whitespace.  
Example 1:

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to convert string to list

 

def Convert(string):

 li = list(string.split(" "))

 return li

 

# Driver code 

str1 = "Geeks for Geeks"

print(Convert(str1))  
  
---  
  
 __

 __

Output:

    
    
    ['Geeks', 'for', 'Geeks']
    

Example 2:

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to convert string to list

def Convert(string):

 li = list(string.split("-"))

 return li

 

# Driver code 

str1 = "Geeks-for-Geeks"

print(Convert(str1))  
  
---  
  
 __

 __

Output:

    
    
    ['Geeks', 'for', 'Geeks']
    

Example 3:

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to convert string to list character-wise

def Convert(string):

 list1=[]

 list1[:0]=string

 return list1

# Driver code

str1="ABCD"

print(Convert(str1))  
  
---  
  
 __

 __

Output:

    
    
    ['A','B','C','D']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

