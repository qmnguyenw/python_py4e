Python program to print the substrings that are prefix of the given string



Given a string, print all the possible substrings which are also the prefix of
the given string.

 **Examples:**

    
    
     **Input :** ababc         
    **Output :** a, ab, aba, abab, ababc, a, ab
              
    **Input :** abdabc          
    **Output :** a, ab, abd, abda, abdab, abdabc, a, ab          
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**  
We use two variables: **start** and **end** to keep track of the current
substring and follow the below conditions until start < len(string):

  * If the current substring is also the prefix of the given string, print it and increment _end_. If end == len(string), increment _start_ and end = start
  * Else increment _start_ and end = start

Logic to check if the current substring is a prefix of the given string:

    
    
    string[end] == string[end-start]

This makes use of the fact that if a substring of length _L_ is a prefix of
the given string, then the substring of length _L+1_ obtained after including
the next character _ch_ in the sequence is also a prefix of the given string
if the character at _(L+1)_ index in the string is equal to _ch_.

  

  

Below is the implementation of the above approach:

 __

 __  
 __

 __

 __  
 __  
 __



# Python3 code to find all possible substrings that 

# are also the prefix of the given string

 

# Function to print all the special substrings

def func(string):

 

 # Used to store the starting and

 # ending index of the substrings

 start, end = 0, 0

 

 while start < len(string):

 

 # If substring is also the prefix

 if string[end] == string[end-start]:

 

 # Print the substring

 print(string[start:end + 1], end= " ")

 end += 1

 

 if end == len(string):

 start += 1

 end = start

 

 # Increment the starting 

 # index of the substring 

 else:

 start += 1

 end = start

 

if __name__ == "__main__":

 

 string = "ababc"

 func(string)  
  
---  
  
 __

 __

 **Output:**

    
    
    a ab aba abab ababc a ab
    

**Time Complexity:** ![O\(n^2\)](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-d3c2f213cefe3af64dbf1dacd22ec5ce_l3.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

