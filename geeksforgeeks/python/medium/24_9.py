Python Counter to find the size of largest subset of anagram words



Given an array of n string containing lowercase letters. Find the size of
largest subset of string which are anagram of each others. An anagram of a
string is another string that contains same characters, only the order of
characters can be different. For example, “abcd” and “dabc” are anagram of
each other.

Examples:

    
    
    Input: 
    ant magenta magnate tan gnamate
    Output: 3
    Explanation
    Anagram strings(1) - ant, tan
    Anagram strings(2) - magenta, magnate,
                         gnamate
    Thus, only second subset have largest
    size i.e., 3
    
    Input: 
    cars bikes arcs steer 
    Output: 2
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

We have existing solution for this problem please refer Find the size of
largest subset of anagram words link. We can solve this problem quickly in
python using Counter() method. Approach is very simple,

  1. Split input string separated by space into words.
  2. As we know two strings are anagram to each other if they contain same character set. So to get all those strings together first we will sort each string in given list of strings.
  3. Now create a dictionary using **Counter** method having strings as keys and their frequencies as value.
  4. Check for maximum value of frequencies, that will be the largest sub-set of anagram strings.

 __

 __  
 __

 __

 __  
 __  
 __

# Function to find the size of largest subset

# of anagram words

from collections import Counter

 

def maxAnagramSize(input):

 

 # split input string separated by space

 input = input.split(" ")

 

 # sort each string in given list of strings

 for i in range(0,len(input)):

 input[i]=''.join(sorted(input[i]))

 

 # now create dictionary using counter method

 # which will have strings as key and their 

 # frequencies as value

 freqDict = Counter(input)

 

 # get maximum value of frequency

 print (max(freqDict.values()))

 

# Driver program

if __name__ == "__main__":

 input = 'ant magenta magnate tan gnamate'

 maxAnagramSize(input)  
  
---  
  
 __

 __

Output:

    
    
    3
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

