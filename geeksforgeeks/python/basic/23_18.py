Zip function in Python to change to a new character set



Given a 26 letter character set, which is equivalent to character set of
English alphabet i.e. (abcd….xyz) and act as a relation. We are also given
several sentences and we have to translate them with the help of given new
character set.

Examples:

    
    
    New character set : qwertyuiopasdfghjklzxcvbnm
    Input : "utta"
    Output : geek
    
    Input : "egrt"
    Output : code
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

We have existing solution for this problem please refer Change string to a new
character set link. We will solve this problem in python using Zip() method
and Dictionary data structures. Approach is simple,

  1. Create a dictionary data structure where we will map original character set in english language with new given character set, **zip(newCharSet,origCharSet)** does it for us. It will map each character of original character set onto each given character of new character set sequentially and return list of tuples of pairs, now we convert it into dictionary using **dict()**.
  2. Now iterate through original string and convert it into new string.

 __

 __  
 __

 __

 __  
 __  
 __

# Function to change string to a new character

 

def newString(charSet,input):

 

 # map original character set of english

 # onto new character set given

 origCharSet = 'abcdefghijklmnopqrstuvwxyz'

 mapChars = dict(zip(charSet,origCharSet))

 

 # iterate through original string and get

 # characters of original character set

 changeChars = [mapChars[chr] for chr in input] 

 

 # join characters without space to get new string

 print (''.join(changeChars))

 

# Driver program

if __name__ == "__main__":

 charSet = 'qwertyuiopasdfghjklzxcvbnm'

 input = 'utta'

 newString(charSet,input)  
  
---  
  
 __

 __

Output:

    
    
    geek
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

