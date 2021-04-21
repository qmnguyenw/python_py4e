Python Bin | Count total bits in a number



Given a positive number n, count total bit in it.  

**Examples:**  

    
    
    Input : 13
    Output : 4
    Binary representation of 13 is 1101
    
    Input  : 183
    Output : 8
    
    Input  : 4096
    Output : 13
    
    
    

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

We have existing solution for this problem please refer Count total bits in a
number link. We can solve this problem quickly in Python using bin() function.
Convert number into it’s binary using **bin()** function and remove starting
two characters ‘0b’ of output binary string because bin function appends ‘0b’
as prefix in output string. Now print length of binary string that will be the
count of bits in binary representation of input number.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Function to count total bits in a number

def countTotalBits(num):

 

 # convert number into it's binary and

 # remove first two characters 0b.

 binary = bin(num)[2:]

 print(len(binary))

# Driver program

if __name__ == "__main__":

 num = 13

 countTotalBits(num)  
  
---  
  
 __

 __

 **Output:**  

  

  

    
    
    4
    
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

