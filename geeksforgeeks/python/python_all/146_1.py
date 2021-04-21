Python | Check if given words appear together in a list of sentence



Given a list of sentences ‘sentence’ and a list of words ‘words’, write a
Python program to find which sentence in the list of sentences consist of all
words contained in ‘words’ and return them within a list.

 **Examples:**

    
    
    **Input :** sentence = ['I love tea', 'He hates tea', 'We love tea']
            words = ['love', 'tea']
    **Output :** ['I love tea', 'We love tea']
    
    **Input :** sentence = ['python coder', 'geeksforgeeks', 'coder in geeksforgeeks']
            words = ['coder', 'geeksforgeeks']
    **Output :** ['coder in geeksforgeeks']
    

  
**Approach #1 :** Using List comprehension

We first use list comprehension, to return a boolean value for each substring
of the list of sentence and store it in ‘res’. Finally, return a list
comprising of the desired sentences according to the boolean values in ‘res’.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Check if given words

# appear together in a list of sentence

 

def check(sentence, words):

 res = [all([k in s for k in words]) for s in
sentence]

 return [sentence[i] for i in range(0, len(res)) if
res[i]]

 

# Driver code

sentence = ['python coder', 'geeksforgeeks', 'coder in
geeksforgeeks']

words = ['coder', 'geeksforgeeks']

print(check(sentence, words))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    ['coder in geeksforgeeks']
    

