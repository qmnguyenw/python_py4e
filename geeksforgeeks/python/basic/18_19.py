Python | Check if a given string is binary string or not



Given a string str. The task is to check whether it is a binary string or not.

 **Examples:**

    
    
    Input: str = "01010101010"
    Output: Yes
    
    Input: str = "geeks101"
    Output: No
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach 1** : Using Set

  1. Insert the given string in a set
  2. Check if the set characters consist of 1 and/or 0 only.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to check

# if a string is binary or not

 

# function for checking the

# string is accepted or not

def check(string) :

 

 # set function convert string

 # into set of characters .

 p = set(string)

 

 # declare set of '0', '1' .

 s = {'0', '1'}

 

 # check set p is same as set s

 # or set p contains only '0'

 # or set p contains only '1'

 # or not, if any one condition

 # is true then string is accepted

 # otherwise not .

 if s == p or p == {'0'} or p ==
{'1'}:

 print("Yes")

 else :

 print("No")

 

 

 

# driver code

if __name__ == "__main__" :

 

 string = "101010000111"

 

 # function calling

 check(string)  
  
---  
  
 __

 __

 **Output:**

    
    
    Yes
    

**Approach 2:** Simple Iteration

  

  

  1. Iterate for every character and check if the character is 0 or 1.
  2. If it is not then set a counter and break.
  3. After iteration check whether the counter is set or not.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to check

# if a string is binary or not

 

# function for checking the

# string is accepted or not

def check2(string) :

 

 # initialize the variable t

 # with '01' string

 t = '01'

 

 # initialize the variable count

 # with 0 value

 count = 0

 

 # looping through each character

 # of the string .

 for char in string :

 

 # check the character is present in

 # string t or not.

 # if this condition is true

 # assign 1 to the count variable

 # and break out of the for loop

 # otherwise pass

 if char not in t :

 count = 1

 break

 else :

 pass

 

 # after coming out of the loop

 # check value of count is non-zero or not

 # if the value is non-zero the en condition is true

 # and string is not accepted

 # otherwise string is accepted

 if count :

 print("No")

 else :

 print("Yes")

 

 

 

# driver code

if __name__ == "__main__" :

 

 string = "001021010001010"

 

 # function calling

 check2(string)  
  
---  
  
 __

 __

 **Output:**

    
    
    No
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

