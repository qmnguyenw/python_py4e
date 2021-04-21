Python Map | Length of the Longest Consecutive 1’s in Binary Representation of
a given integer



Given a number n, find length of the longest consecutive 1s in its binary
representation.

Examples:

    
    
    Input : n = 14
    Output : 3
    The binary representation of 14 is **111** 0.
    
    Input : n = 222
    Output : 4
    The binary representation of 222 is 110 **1111** 0.
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

We have existing solution for this problem please refer Length of the Longest
Consecutive 1s in Binary Representation link. We can solve this problem
quickly in python. Approach is very simple,

  1. Convert decimal number into it’s binary using bin() function and remove starting first two characters ‘0b’ because **bin()** function returns binary representattion of number in string form and appends ‘0b’ as prefix.
  2. Separate all sub-strings of consecutive 1’s separated by zeros using **split()** method of string.
  3. Print maximum length of splitted sub-strings of 1’s.

 __

 __  
 __

 __

 __  
 __  
 __

# Function to find Length of the Longest Consecutive

# 1's in Binary Representation

 

def maxConsecutive1(input):

 # convert number into it's binary

 input = bin(input)

 

 # remove first two characters of output string

 input = input[2:]

 

 # input.split('0') --> splits all sub-strings of 

 # consecutive 1's separated by 0's, output will 

 # be like ['11','1111']

 # map(len,input.split('0')) --> map function maps

 # len function on each sub-string of consecutive 1's

 # max() returns maximum element from a list

 print (max(map(len, input.split('0'))))

 

# Driver program

if __name__ == '__main__':

 input = 222

 maxConsecutive1(input)  
  
---  
  
 __

 __

Output:

    
    
    4
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

