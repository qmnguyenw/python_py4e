Python | Sort words of sentence in ascending order



Given a sentence, sort it alphabetically in ascending order.

Examples:

    
    
    Input : to learn programming refer geeksforgeeks
    Output : geeksforgeeks learn programming refer to
    
    Input : geeks for geeks
    Output : for geeks geeks
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

We will use built in library function to sort the words of the sentence in
ascending order.  
 **Prerequisites:**  
1\. split()  
2\. sort() in Python  
3\. join()

  * Split the Sentence in words.
  * Sort the words alphabetically
  * Join the sorted words alphabetically to form a new Sentence.

 **Below is the implementation of above idea.**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Function to sort the words

# in ascending order

def sortedSentence(Sentence):

 

 # Splitting the Sentence into words

 words = Sentence.split(" ")

 

 # Sorting the words

 words.sort()

 

 # Making new Sentence by 

 # joining the sorted words

 newSentence = " ".join(words)

 

 # Return newSentence

 return newSentence

 

# Driver's Code

 

Sentence = "to learn programming refer geeksforgeeks"

# Print the sortedSentence

print(sortedSentence(Sentence))

 

Sentence = "geeks for geeks"

# Print the sortedSentence

print(sortedSentence(Sentence))  
  
---  
  
 __

 __

Output:

    
    
    geeksforgeeks learn programming refer to
    for geeks geeks
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

