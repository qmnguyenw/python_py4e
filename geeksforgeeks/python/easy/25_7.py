Sort the words in lexicographical order in Python



Given a strings, we need to sort the words in lexicographical order
(dictionary order).

Examples :

    
    
    Input :  "hello python program how are you"
    Output :  are
              hello
              how
              program
              python
              you
    
    Input :   "Coders loves the algorithms"
    Output :  Coders
              algorithms
              loves
              the
    

Note: The words which have first letter is capital letter they will print
according alphabetical manner.

 **Approach :**  
Approach used in this program is very simple. Split the strings using split()
function. After that sort the words in lexicographical order using sort().
Iterate the words through loop and print each word, which are already sorted.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to sort the words in lexicographical

# order

 

def sortLexo(my_string):

 

 # Split the my_string till where space is found.

 words = my_string.split()

 

 # sort() will sort the strings.

 words.sort()

 

 # Iterate i through 'words' to print the words

 # in alphabetical manner.

 for i in words:

 print( i ) 

 

# Driver code 

if __name__ == '__main__':

 

 my_string = "hello this is example how to sort " \

 "the word in alphabetical manner"

 # Calling function

 sortLexo(my_string)  
  
---  
  
 __

 __

Output :

    
    
    alphabetical
    example
    hello
    how
    in
    is
    manner
    sort
    the
    this
    to
    word
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

