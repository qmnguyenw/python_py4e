K’th Non-repeating Character in Python using List Comprehension and
OrderedDict



Given a string and a number k, find the k-th non-repeating character in the
string. Consider a large input string with lacs of characters and a small
character set. How to find the character by only doing only one traversal of
input string?

Examples:

    
    
    Input : str = geeksforgeeks, k = 3
    Output : r
    First non-repeating character is f,
    second is o and third is r.
    
    Input : str = geeksforgeeks, k = 2
    Output : o
    
    Input : str = geeksforgeeks, k = 4
    Output : Less than k non-repeating
             characters in input.
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

This problem has existing solution please refer link. We can solve this
problem quickly in python using List Comprehension and OrderedDict.

 __

 __  
 __

 __

 __  
 __  
 __

# Function to find k'th non repeating character

# in string 

from collections import OrderedDict 

 

def kthRepeating(input,k): 

 

 # OrderedDict returns a dictionary data 

 # structure having characters of input 

 # string as keys in the same order they 

 # were inserted and 0 as their default value 

 dict=OrderedDict.fromkeys(input,0) 

 

 # now traverse input string to calculate 

 # frequency of each character 

 for ch in input: 

 dict[ch]+=1

 

 # now extract list of all keys whose value 

 # is 1 from dict Ordered Dictionary 

 nonRepeatDict = [key for (key,value) in dict.items() if
value==1] 

 

 # now return (k-1)th character from above list 

 if len(nonRepeatDict) < k: 

 return 'Less than k non-repeating characters in input.'

 else: 

 return nonRepeatDict[k-1] 

 

# Driver function 

if __name__ == "__main__": 

 input = "geeksforgeeks"

 k = 3

 print (kthRepeating(input, k))   
  
---  
  
__

__

Output:

  

  

    
    
    r
    

This article is contributed by **Shashank Mishra (Gullu)**. If you like
GeeksforGeeks and would like to contribute, you can also write an article
using contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

