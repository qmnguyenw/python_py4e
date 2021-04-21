Python Regex to extract maximum numeric value from a string



Given an alphanumeric string, extract maximum numeric value from that string.
Alphabets will only be in lower case.

Examples:

    
    
    Input : 100klh564abc365bg
    Output : 564
    Maximum numeric value among 100, 564 
    and 365 is 564.
    
    Input : abchsd0sdhs
    Output : 0
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

This problem has existing solution please refer Extract maximum numeric value
from a given string | Set 1 (General approach) link. We will solve this
problem quickly in python using Regex. Approach is very simple,

  1. Find list of all integer numbers in string separated by lower case characters using re.findall(expression,string) method.
  2. Convert each number in form of string into decimal number and then find max of it.

 __

 __  
 __

 __

 __  
 __  
 __

# Function to extract maximum numeric value from

# a given string

import re

 

def extractMax(input):

 

 # get a list of all numbers separated by 

 # lower case characters 

 # \d+ is a regular expression which means

 # one or more digit

 # output will be like ['100','564','365']

 numbers = re.findall('\d+',input)

 

 # now we need to convert each number into integer

 # int(string) converts string into integer

 # we will map int() function onto all elements 

 # of numbers list

 numbers = map(int,numbers)

 

 print max(numbers)

 

# Driver program

if __name__ == "__main__":

 input = '100klh564abc365bg'

 extractMax(input)  
  
---  
  
 __

 __

Output:

    
    
    564
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

