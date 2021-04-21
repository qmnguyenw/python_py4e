Python | Part of Speech Tagging using TextBlob



TextBlob module is used for building programs for text analysis. One of the
more powerful aspects of the TextBlob module is the Part of Speech tagging.

Install TextBlob run the following commands:

    
    
    $ pip install -U textblob
    $ python -m textblob.download_corpora
    

This will install TextBlob and download the necessary NLTK corpora.

The above installation will take quite some time due to the massive amount of
tokenizers, chunkers, other algorithms, and all of the corpora to be
downloaded.

> Let’s knock out some quick vocabulary:
>
>  
>
>
>  
>
>
>  **Corpus :** Body of text, singular. Corpora is the plural of this.  
>  **Lexicon :** Words and their meanings.  
>  **Token :** Each “entity” that is a part of whatever was split up based on
> rules.

In corpus linguistics, part-of-speech tagging (POS tagging or PoS tagging or
POST), also called **Grammatical tagging** or **Word-category
disambiguation.**

    
    
    **Input:** Everything is all about money.
    **Output:** [('Everything', 'NN'), ('is', 'VBZ'), 
                  ('all', 'DT'), ('about', 'IN'), 
                                 ('money', 'NN')] 
    

Here’s a list of the tags, what they mean, and some examples:

    
    
    CC coordinating conjunction
    CD cardinal digit
    DT determiner
    EX existential there (like: “there is” … think of it like “there exists”)
    FW foreign word
    IN preposition/subordinating conjunction
    JJ adjective ‘big’
    JJR adjective, comparative ‘bigger’
    JJS adjective, superlative ‘biggest’
    LS list marker 1)
    MD modal could, will
    NN noun, singular ‘desk’
    NNS noun plural ‘desks’
    NNP proper noun, singular ‘Harrison’
    NNPS proper noun, plural ‘Americans’
    PDT predeterminer ‘all the kids’
    POS possessive ending parent‘s
    PRP personal pronoun I, he, she
    PRP$ possessive pronoun my, his, hers
    RB adverb very, silently,
    RBR adverb, comparative better
    RBS adverb, superlative best
    RP particle give up
    TO to go ‘to‘ the store.
    UH interjection errrrrrrrm
    VB verb, base form take
    VBD verb, past tense took
    VBG verb, gerund/present participle taking
    VBN verb, past participle taken
    VBP verb, sing. present, non-3d take
    VBZ verb, 3rd person sing. present takes
    WDT wh-determiner which
    WP wh-pronoun who, what
    WP$ possessive wh-pronoun whose
    WRB wh-abverb where, when
    

__

__  
__

__

__  
__  
__

# from textblob lib import TextBlob method

from textblob import TextBlob

 

text = ("Sukanya, Rajib and Naba are my good friends. " +

 "Sukanya is getting married next year. " +

 "Marriage is a big step in one’s life." +

 "It is both exciting and frightening. " +

 "But friendship is a sacred bond between people." +

 "It is a special kind of love between us. " +

 "Many of you must have tried searching for a friend "+

 "but never found the right one.")

 

# create a textblob object

blob_object = TextBlob(text)

 

# Part-of-speech tags can be accessed 

# through the tags property of blob object.'

 

# print word with pos tag.

print(blob_object.tags)  
  
---  
  
 __

 __

 **Output :**

    
    
    [('Sukanya', 'NNP'),
     ('Rajib', 'NNP'),
     ('and', 'CC'),
     ('Naba', 'NNP'),
     ('are', 'VBP'),
     ('my', 'PRP$'),
     ('good', 'JJ'),
     ('friends', 'NNS'),
     ('Sukanya', 'NNP'),
     ('is', 'VBZ'),
     ('getting', 'VBG'),
     ('married', 'VBN'),
     ('next', 'JJ'),
     ('year', 'NN'),
     ('Marriage', 'NN'),
     ('is', 'VBZ'),
     ('a', 'DT'),
     ('big', 'JJ'),
     ('step', 'NN'),
     ('in', 'IN'),
     ('one', 'CD'),
     ('’', 'NN'),
     ('s', 'NN'),
     ('life.It', 'NN'),
     ('is', 'VBZ'),
     ('both', 'DT'),
     ('exciting', 'VBG'),
     ('and', 'CC'),
     ('frightening', 'NN'),
     ('But', 'CC'),
     ('friendship', 'NN'),
     ('is', 'VBZ'),
     ('a', 'DT'),
     ('sacred', 'JJ'),
     ('bond', 'NN'),
     ('between', 'IN'),
     ('people.It', 'NN'),
     ('is', 'VBZ'),
     ('a', 'DT'),
     ('special', 'JJ'),
     ('kind', 'NN'),
     ('of', 'IN'),
     ('love', 'NN'),
     ('between', 'IN'),
     ('us', 'PRP'),
     ('Many', 'JJ'),
     ('of', 'IN'),
     ('you', 'PRP'),
     ('must', 'MD'),
     ('have', 'VB'),
     ('tried', 'VBN'),
     ('searching', 'VBG'),
     ('for', 'IN'),
     ('a', 'DT'),
     ('friend', 'NN'),
     ('but', 'CC'),
     ('never', 'RB'),
     ('found', 'VBD'),
     ('the', 'DT'),
     ('right', 'JJ'),
     ('one', 'NN')]
    

Basically, the goal of a POS tagger is to assign linguistic (mostly
grammatical) information to sub-sentential units. Such units are called tokens
and, most of the time, correspond to words and symbols (e.g. punctuation).

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save

