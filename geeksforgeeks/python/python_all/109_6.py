Spelling checker in Python



For any type of text processing or analysis, checking the spelling of the word
is one of the basic requirements. This article discusses various ways that you
can check the spellings of the words and also can correct the spelling of the
respective word.  

## Using textblob library

First, you need to install the library **textblob** using pip in command
prompt.

    
    
    pip install textblob
    

You can also install this library in Jupyter Notebook as:  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import sys

!{sys.executable} - m pip install textblob  
  
---  
  
 __

 __

  
**Program for Spelling checker –**  

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from textblob import TextBlob

a = "cmputr" # incorrect spelling

print("original text: "+str(a))

b = TextBlob(a)

# prints the corrected spelling

print("corrected text: "+str(b.correct()))  
  
---  
  
 __

 __

 **Output:**  

    
    
    original text: cmputr
    corrected text: computer
    
    
    

## Using pyspellchecker library

You can install this library as below:  
 **Using pip:**

    
    
    pip install pyspellchecker
    
    
    

**In Jupyter Notebook:**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import sys

!{sys.executable} - m pip install pyspellchecker  
  
---  
  
 __

 __

  
**Spelling Checker program using pyspellchecker –**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from spellchecker import SpellChecker

spell = SpellChecker()

# find those words that may be misspelled

misspelled = spell.unknown(["cmputr", "watr", "study",
"wrte"])

for word in misspelled:

 # Get the one most likely answer

 print(spell.correction(word))

 # Get a list of likely options

 print(spell.candidates(word))  
  
---  
  
 __

 __

 **Output:**  

  

  

    
    
    computer
    {'caput', 'caputs', 'compute', 'computor', 'impute', 'computer'}
    water
    {'water', 'watt', 'warr', 'wart', 'war', 'wath', 'wat'}
    write
    {'wroe', 'arte', 'wre', 'rte', 'wrote', 'write'}
    
    
    

## Using JamSpell

To achieve the best quality while making spelling corrections dictionary-based
methods are not enough. You need to consider the word surroundings. JamSpell
is a python spell checking library based on a language model. It makes
different corrections for a different context.

1) Install swig3

    
    
    apt-get install swig3.0   # for linux
    brew install swig@3       # for mac
    
    

2) Install jamspell

    
    
    pip install jamspell
    
    

3) Download a language model for your language

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Create a corrector

corrector = jamspell.TSpellCorrector()

# Load Language model -

# argument is a downloaded model file path

corrector.LoadLangModel('Downloads/en_model.bin')

# To fix text automatically run FixFragment:

print(corrector.FixFragment('I am the begt spell cherken!'))

# To get a list of possible candidates

# pass a splitted sentence, and a word position

print(corrector.GetCandidates(['i', 'am', 'the', 'begt',
'spell', 'cherken'], 3))

print(corrector.GetCandidates(['i', 'am', 'the', 'begt',
'spell', 'cherken'], 5))  
  
---  
  
 __

 __

 **Output:**

    
    
    u'I am the best spell checker!'
    (u'best', u'beat', u'belt', u'bet', u'bent')
    (u'checker', u'chicken', u'checked', u'wherein', u'coherent', ...)
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

