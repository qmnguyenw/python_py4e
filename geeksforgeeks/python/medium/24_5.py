Python | Reverse each word in a sentence



Given a long sentence, reverse each word of the sentence individually in the
sentence itself.  
Examples:

    
    
    Input : Geeks For Geeks is good to learn
    Output : skeeG roF skeeG si doog ot nrael
    
    Input : Split Reverse Join
    Output : tilpS esreveR nioJ
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

We shall use Python’s built in library function to reverse each word
individually in the string itself.

 **Prerequisites :**  
1\. split()  
2\. Reversing Techniques in Python  
3\. List Comprehension Method in python  
4\. join()

  * First split the sentence into list of words.
  * Reverse each word of the string in the list individually.
  * Join the words in the list to form a new sentence.

 **Below is the implementation of above idea.**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to Reverse each word

# of a Sentence individually

 

# Function to Reverse words

def reverseWordSentence(Sentence):

 

 # Splitting the Sentence into list of words.

 words = Sentence.split(" ")

 

 # Reversing each word and creating

 # a new list of words

 # List Comprehension Technique

 newWords = [word[::-1] for word in words]

 

 # Joining the new list of words

 # to for a new Sentence

 newSentence = " ".join(newWords)

 

 return newSentence

 

# Driver's Code 

Sentence = "GeeksforGeeks is good to learn"

# Calling the reverseWordSentence 

# Function to get the newSentence

print(reverseWordSentence(Sentence))  
  
---  
  
 __

 __

Output:

    
    
    skeeGrofskeeG si doog ot nrael
    

Python is well known for its short codes. We shall do the same task but with
lesser line of codes.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to Reverse each word

# of a Sentence individually

 

# Function to Reverse words

def reverseWordSentence(Sentence):

 

 # All in One line

 return ' '.join(word[::-1] for word in
Sentence.split(" "))

 

# Driver's Code 

Sentence = "Geeks for Geeks"

print(reverseWordSentence(Sentence))   
  
---  
  
__

__

Output:

    
    
    skeeG rof skeeG
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

