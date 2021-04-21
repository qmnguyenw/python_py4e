Part of Speech Tagging with Stop words using NLTK in python



The Natural Language Toolkit (NLTK) is a platform used for building programs
for text analysis. One of the more powerful aspects of the NLTK module is the
Part of Speech tagging.

In order to run the below python program you must have to install NLTK. Please
follow the installation steps.

  * Open your terminal, run **pip install nltk**.
  * Write python in the command prompt so python Interactive Shell is ready to execute your code/Script.
  * Type **import nltk**
  *  **nltk.download()**

A GUI will pop up then choose to download “all” for all packages, and then
click ‘download’. This will give you all of the tokenizers, chunkers, other
algorithms, and all of the corpora, so that’s why installation will take quite
time.  
Examples:

    
    
    import nltk
    nltk.download()
    

let’s knock out some quick vocabulary:  
 **Corpus :** Body of text, singular. Corpora is the plural of this.  
 **Lexicon :** Words and their meanings.  
 **Token :** Each “entity” that is a part of whatever was split up based on
rules.

In corpus linguistics, **part-of-speech tagging** ( **POS tagging** or **PoS
tagging** or **POST** ), also called **grammatical tagging** or **word-
category disambiguation**.

  

  

    
    
    Input: Everything is all about money.
    Output: [('Everything', 'NN'), ('is', 'VBZ'), 
              ('all', 'DT'),('about', 'IN'), 
              ('money', 'NN'), ('.', '.')] 
    

Here’s a list of the tags, what they mean, and some examples:

> CC coordinating conjunction  
> CD cardinal digit  
> DT determiner  
> EX existential there

