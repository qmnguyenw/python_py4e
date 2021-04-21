Python program to check if a word is a noun



Given a word, the task is to write a Python program to find if the word is a
noun or not using Python.

 **Examples:**

    
    
     **Input:** India
    **Output:** India is noun.
    
    **Input:** Writing
    **Output:** Writing is not a noun.

There are various libraries that can be used to solve this problem.

 **Approach 1** : PoS tagging using NLTK

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# import required modules

import nltk

nltk.download('averaged_perceptron_tagger')

 

# taking input text as India

text = "India"

ans = nltk.pos_tag()

 

# ans returns a list of tuple

val = ans[0][1]

 

# checking if it is a noun or not

if(val == 'NN' or val == 'NNS' or val == 'NNPS'
or val == 'NNP'):

 print(text, " is a noun.")

else:

 print(text, " is not a noun.")  
  
---  
  
 __

 __

