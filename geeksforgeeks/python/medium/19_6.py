Python | Tokenize text using TextBlob



 **TextBlob** module is a Python library and offers a simple API to access
its methods and perform basic NLP tasks. It is built on the top of NLTK
module.

Install TextBlob using the following commands in terminal:

    
    
    pip install -U textblob
    python -m textblob.download_corpora
    

This will install TextBlob and download the necessary NLTK corpora. The above
installation will take quite some time due to the massive amount of
tokenizers, chunkers, other algorithms, and all of the corpora to be
downloaded.

Some terms that will be frequently used are :

  *  **Corpus** – Body of text, singular. Corpora is the plural of this.
  *  **Lexicon** – Words and their meanings.
  *  **Token** – Each “entity” that is a part of whatever was split up based on rules. For examples, each word is a token when a sentence is “tokenized” into words. Each sentence can also be a token, if you tokenized the sentences out of a paragraph.

 **So basically tokenizing involves splitting sentences and words from the
body of the text.**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# from textblob lib. import TextBlob method

from textblob import TextBlob

 

text = ("Natural language processing (NLP) is a field " +

 "of computer science, artificial intelligence " +

 "and computational linguistics concerned with " +

 "the interactions between computers and human " +

 "(natural) languages, and, in particular, " +

 "concerned with programming computers to " +

 "fruitfully process large natural language " +

 "corpora. Challenges in natural language " +

 "processing frequently involve natural " +

 "language understanding, natural language" +

 "generation frequently from formal, machine" +

 "-readable logical forms), connecting language " +

 "and machine perception, managing human-" +

 "computer dialog systems, or some combination " +

 "thereof.")

 

# create a TextBlob object

blob_object = TextBlob(text)

 

# tokenize paragraph into words.

print(" Word Tokenize :\n", blob_object.words)

 

# tokenize paragraph into sentences.

print("\n Sentence Tokenize :\n", blob_object.sentences)  
  
---  
  
 __

 __

 **Output :**

> Word Tokenize :  
> [‘Natural’, ‘language’, ‘processing’, ‘NLP’, ‘is’, ‘a’, ‘field’, ‘of’,
> ‘computer’, ‘science’, ‘artificial’, ‘intelligence’, ‘and’, ‘computational’,
> ‘linguistics’, ‘concerned’, ‘with’, ‘the’, ‘interactions’, ‘between’,
> ‘computers’, ‘and’, ‘human’, ‘natural’, ‘languages’, ‘and’, ‘in’,
> ‘particular’, ‘concerned’, ‘with’, ‘programming’, ‘computers’, ‘to’,
> ‘fruitfully’, ‘process’, ‘large’, ‘natural’, ‘language’, ‘corpora’,
> ‘Challenges’, ‘in’, ‘natural’, ‘language’, ‘processing’, ‘frequently’,
> ‘involve’, ‘natural’, ‘language’, ‘understanding’, ‘natural’,
> ‘languagegeneration’, ‘frequently’, ‘from’, ‘formal’, ‘machine-readable’,
> ‘logical’, ‘forms’, ‘connecting’, ‘language’, ‘and’, ‘machine’,
> ‘perception’, ‘managing’, ‘human-computer’, ‘dialog’, ‘systems’, ‘or’,
> ‘some’, ‘combination’, ‘thereof’]
>
> Sentence Tokenize :  
> [Sentence(“Natural language processing (NLP) is a field of computer science,
> artificial intelligence and computational linguistics concerned with the
> interactions between computers and human (natural) languages, and, in
> particular, concerned with programming computers to fruitfully process large
> natural language corpora.”), Sentence(“Challenges in natural language
> processing frequently involve natural language understanding, natural
> language generation frequently from formal, machine-readable logical forms),
> connecting language and machine perception, managing human-computer dialog
> systems, or some combination thereof.”)]

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save

