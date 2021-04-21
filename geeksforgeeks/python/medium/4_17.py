Emotion classification using NRC Lexicon in Python



Many a time, for real-world projects, emotion recognition is often just the
start of the project. That time writing a whole code on that will not only
increase time but also efficiency is hindered.

_NRCLexicon_ is an MIT-approved _pypi_ project by Mark M. Bailey which
predicts the sentiments and emotion of a given text. The package contains
approximately 27,000 words and is based on the National Research Council
Canada (NRC) affect lexicon and the _NLTK_ library’s _WordNet_ synonym sets.

###  **Installation:**

To install this module type the below command in the terminal.

    
    
    pip install NRCLex
    

Even after the installation of this module, _MissingCorpusError_ may occur
while running programs. So it is advised to also install
_textblob.download_corpora_ by using the below command on the command prompt.

    
    
    python -m textblob.download_corpora
    

**Approach:**

  

  

  * Import the module

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import required modules

from nrclex import NRCLex  
  
---  
  
 __

 __

  * Assign input text

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Assinging list of words

text = ['hate', 'lovely', 'person', 'worst']  
  
---  
  
 __

 __

  * Create _NRCLex_ object for each input text.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

for i in range(len(text)):

 

 # creating objects

 emotion = NRCLex(text[i])  
  
---  
  
 __

 __

  * Apply methods to classify emotions.

Sr.| Method| Description| 1|  _emotion.words_|  Return words list.| 2|
_emotion.sentences_|  Return sentences list.| 3|  _emotion.affect_list_|
Return affect list.| 4|  _emotion.affect_dict_|  Return affect dictionary.| 5|
_emotion.raw_emotion_scores_|  Return raw emotional counts.| 6|
_emotion.top_emotions_|  Return highest emotions.| 7|
_emotion.affect_frequencies_|  Return affect frequencies.  
---|---|---  
  
  * Emotional affects measured include the following:

  1. fear
  2. anger
  3. anticipation
  4. trust
  5. surprise
  6. positive
  7. negative
  8. sadness
  9. disgust
  10. joy

Below is the Implementation.

 **Example 1:**

Based on the above approach, the below example classifies various emotions
using _top_emotions._

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import module

from nrclex import NRCLex

 

# Assign list of strings

text = ['hate', 'lovely', 'person', 'worst']

 

# Iterate through list

for i in range(len(text)):

 

 # Create object

 emotion = NRCLex(text[i])

 

 # Classify emotion

 print('\n\n', text[i], ': ', emotion.top_emotions)  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201017142344/Screenshot560.png)

  

  

 **Example 2:**

Here a single emotion _love_ is classified using all the methods of _NCRLex_
module.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import module

from nrclex import NRCLex

 

# Assign emotion

text = 'love'

 

# Create object

emotion = NRCLex(text)

 

# Using methods to classigy emotion

print('\n', emotion.words)

print('\n', emotion.sentences)

print('\n', emotion.affect_list)

print('\n', emotion.affect_dict)

print('\n', emotion.raw_emotion_scores)

print('\n', emotion.top_emotions)

print('\n', emotion.affect_frequencies)  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201017143435/Screenshot561.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

