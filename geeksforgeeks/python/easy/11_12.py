Python | Words extraction from set of characters using dictionary



Given the words, the task is to extract different words from a set of
characters using the defined dictionary.  
 **Approach:**  
Python in its language defines an inbuilt module enchant which handles
certain operations related to words. In the approach mentioned, following
methods are used.

  *  **check() :** It checks if a string is a word or not and returns true if a string is a word, else returns false.
  *  **permutations(str_arr, str_len) :**It provides the combination of a string as per the mentioned string length.

There is a chance that enchant() module might not be present, so it can be
installed using _pip3 install enchant_.

 **Below is the Python code implementation of the above approach.**

 __

 __  
 __

 __

 __  
 __  
 __

# importing libraries

import keyword

import enchant

from itertools import permutations 

 

d = enchant.Dict("en_US")

 

words = []

perm_word = []

 

# character combination to 

# list down all the words

str_arr = "star"

 

# Getting the string length to use it in the loop. 

str_len = 4

print("Length of the string is : ", str_len )

 

while str_len > 1 :

 

 if str_len == len(str_arr):

 perm = list(permutations(str_arr))

 str_len = str_len -1

 

 for i in list(perm):

 words =''.join(i)

 

 if d.check(words):

 perm_word.append(words)

 print ( words + " is an English words")

 print ("perm_word", perm_word)

 

 elif str_len > 1:

 perm = list(permutations(str_arr, str_len))

 str_len = str_len -1

 

 for i in list(perm):

 words =''.join(i)

 

 if d.check(words):

 perm_word.append(words)

 print ( words + " is an English word")

 print ("perm_word", perm_word)

 

 else:

 str_len = 0  
  
---  
  
 __

 __

 **Output :**

    
    
    star is an English words
    tars is an English words
    arts is an English words
    rats is an English words
    perm_word [‘star’, ‘tars’, ‘arts’, ‘rats’]
    sat is an English word
    tar is an English word
    art is an English word
    rat is an English word
    perm_word [‘star’, ‘tars’, ‘arts’, ‘rats’, ‘sat’, ‘tar’, ‘art’, ‘rat’]
    st is an English word
    ts is an English word
    tr is an English word
    as is an English word
    at is an English word
    rs is an English word
    rt is an English word
    perm_word [‘star’, ‘tars’, ‘arts’, ‘rats’, ‘sat’, ‘tar’, ‘art’, ‘rat’, 
    ‘st’, ‘ts’, ‘tr’, ‘as’, ‘at’, ‘rs’, ‘rt’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

