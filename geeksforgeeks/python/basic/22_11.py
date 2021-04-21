Python | Find all close matches of input string from a list



We are given a list of pattern strings and a single input string. We need to
find all possible close good enough matches of input string into list of
pattern strings.

Examples:

    
    
    Input : patterns = ['ape', 'apple', 
                      'peach', 'puppy'], 
              input = 'appel'
    Output : ['apple', 'ape']
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

We can solve this problem in python quickly using in built function
**difflib.get_close_matches()**.

### How does difflib.get_close_matches() function work in Python ?

 **difflib.get_close_matches(word, possibilities, n, cutoff)** accepts four
parameters in which **n, cutoff** are optional. **word** is a sequence for
which close matches are desired, **possibilities** is a list of sequences
against which to match word. Optional argument **n (default 3)** is the
maximum number of close matches to return, n must be greater than 0. Optional
argument **cutoff (default 0.6)** is a float in the range [0, 1].
Possibilities that don’t score at least that similar to word are ignored.  
The best (no more than n) matches among the possibilities are returned in a
list, sorted by similarity score, most similar first.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Function to find all close matches of

# input string in given list of possible strings

from difflib import get_close_matches

 

def closeMatches(patterns, word):

 print(get_close_matches(word, patterns))

 

# Driver program

if __name__ == "__main__":

 word = 'appel'

 patterns = ['ape', 'apple', 'peach', 'puppy']

 closeMatches(patterns, word)  
  
---  
  
 __

 __

 ** _References :_** https://docs.python.org/2/library/difflib.html

Output:

    
    
    ['apple', 'ape']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

