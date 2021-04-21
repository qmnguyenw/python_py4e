Check if Binary representation is Palindrome in Python



Given an integer ‘n’, write a Python function that returns true if binary
representation of x is palindrome else return false.

Examples:

    
    
    Input : n = 9
    Output : True
    Binary representation of n=9 is 1001 which 
    is palindrome as well.
    
    Input : n = 10
    Output : False
    Binary representation of n=10 is 1010 which 
    is not palindrome.
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

We have existing solution for this problem please refer Check if binary
representation of a number is palindrome link. We can solve this problem in
python very quickly. Approach is very simple,

  1. Convert given number into it’s binary representation using bin(num) function.
  2. Now reverse binary representation string of number and compare it with original binary represented string, if both are equal that means binary representation of number is pallindrome else not.
  3. 

 ** _Note :_** We can use other approach of checking a string is palindrome or
not.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Function to check if binary representation of

# a number is pallindrome or not

 

def binaryPallindrome(num):

 

 # convert number into binary

 binary = bin(num)

 

 # skip first two characters of string

 # because bin function appends '0b' as 

 # prefix in binary representation of

 # a number

 binary = binary[2:]

 

 # now reverse binary string and compare

 # it with original

 return binary == binary[-1::-1]

 

# Driver program

if __name__ == "__main__":

 num = 9

 print binaryPallindrome(num)  
  
---  
  
 __

 __

Output:

    
    
    True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

