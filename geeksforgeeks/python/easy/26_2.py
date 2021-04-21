Possible Words using given characters in Python



Given a dictionary and a character array, print all valid words that are
possible using characters from the array.  
 **Note:** Repetitions of characters is not allowed.  
Examples:

    
    
    Input : Dict = ["go","bat","me","eat","goal","boy", "run"]
            arr = ['e','o','b', 'a','m','g', 'l']
    Output : go, me, goal. 
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

This problem has existing solution please refer Print all valid words that are
possible using Characters of Array link. We will this problem in python very
quickly using Dictionary Data Structure. Approach is very simple :

  1. Traverse list of given strings one by one and convert them into dictionary using Counter(input) method of **collections** module.
  2. Check if all keys of any string lies within given set of characters that means this word is possible to create.

 __

 __  
 __

 __

 __  
 __  
 __

# Function to print words which can be created

# using given set of characters

 

 

 

def charCount(word):

 dict = {}

 for i in word:

 dict[i] = dict.get(i, 0) + 1

 return dict

 

 

def possible_words(lwords, charSet):

 for word in lwords:

 flag = 1

 chars = charCount(word)

 for key in chars:

 if key not in charSet:

 flag = 0

 else:

 if charSet.count(key) != chars[key]:

 flag = 0

 if flag == 1:

 print(word)

 

if __name__ == "__main__":

 input = ['goo', 'bat', 'me', 'eat', 'goal',
'boy', 'run']

 charSet = ['e', 'o', 'b', 'a', 'm', 'g',
'l']

 possible_words(input, charSet)  
  
---  
  
 __

 __

Output:

    
    
    go 
    me
    goal
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

