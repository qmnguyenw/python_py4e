Reverse words in a given String in Python



We are given a string and we need to reverse words of a given string?

Examples:

    
    
    Input : str = geeks quiz practice code
    Output : str = code practice quiz geeks
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

This problem has existing solution please refer Reverse words in a given
String link. We will solve this problem in python. Given below are the steps
to be followed to solve this problem.

  * Separate each word in given string using split() method of string data type in python.
  * Reverse the word separated list.
  * Print words of list, in string form after joining each word with space using ” “.join() method in python.

 __

 __  
 __

 __

 __  
 __  
 __

# Function to reverse words of string

 

def rev_sentence(sentence): 

 

 # first split the string into words 

 words = sentence.split(' ') 

 

 # then reverse the split string list and join using space 

 reverse_sentence = ' '.join(reversed(words)) 

 

 # finally return the joined string 

 return reverse_sentence 

 

if __name__ == "__main__": 

 input = 'geeks quiz practice code'

 print (rev_sentence(input))  
  
---  
  
 __

 __

Output:

  

  

    
    
    code practice quiz geeks
    

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

