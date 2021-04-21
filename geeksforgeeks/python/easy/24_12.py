Python Set | Check whether a given string is Heterogram or not



Given a string S of lower case characters. The task is to check whether a the
given string is Heterogram or not. A heterogram is a word, phrase, or sentence
in which no letter of the alphabet occurs more than once.

Examples:

    
    
    Input : S = "the big dwarf only jumps"
    Output : Yes
    Each alphabet in the string S is occurred
    only once.
    
    Input : S = "geeksforgeeks" 
    Output : No
    Since alphabet 'g', 'e', 'k', 's' occurred
    more than once.
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

We have existing solution for this problem please refer Check whether a given
string is Heterogram or not link. We can solve this problem quickly in python
using Set data structure. Approach is very simple,

  1. To check sentence is heterogram or not we only concern about alphabets not any other character, so we separate out list of all alphabets present in sentence.
  2. Convert list of alphabets into set because set contains unique values, if length of set is equal to number of alphabets that means each alphabet occured once then sentence is heterogram, otherwise not.

 __

 __  
 __

 __

 __  
 __  
 __

# Function to Check whether a given string is Heterogram or not

 

def heterogram(input):

 

 # separate out list of alphabets using list comprehension

 # ord function returns ascii value of character

 alphabets = [ ch for ch in input if ( ord(ch) >=
ord('a') and ord(ch) <= ord('z') )]

 

 # convert list of alphabets into set and 

 # compare lengths

 if len(set(alphabets))==len(alphabets):

 print ('Yes')

 else:

 print ('No')

 

# Driver program

if __name__ == "__main__":

 input = 'the big dwarf only jumps'

 heterogram(input)  
  
---  
  
 __

 __

Output:

    
    
    Yes
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

