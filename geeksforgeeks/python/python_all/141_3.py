Python | Named Entity Recognition (NER) using spaCy



 **Named Entity Recognition (NER)** is a standard NLP problem which involves
spotting named entities (people, places, organizations etc.) from a chunk of
text, and classifying them into a predefined set of categories. Some of the
practical applications of NER include:

  * Scanning news articles for the people, organizations and locations reported.
  * Providing concise features for search optimization: instead of searching the entire content, one may simply search for the major entities involved.
  * Quickly retrieving geographical locations talked about in Twitter posts.

 **NER with spaCy**  
spaCy is regarded as the fastest NLP framework in Python, with single
optimized functions for each of the NLP tasks it implements. Being easy to
learn and use, one can easily perform simple tasks using a few lines of code.

 **Installation :**

    
    
    pip install spacy
    python -m spacy download en_core_web_sm
    

**Code for NER using spaCy.**

 __

 __  
 __

 __

 __  
 __  
 __

import spacy

 

nlp = spacy.load('en_core_web_sm')

 

sentence = "Apple is looking at buying U.K. startup for $1 billion"

 

doc = nlp(sentence)

 

for ent in doc.ents:

 print(ent.text, ent.start_char, ent.end_char, ent.label_)  
  
---  
  
 __

 __

 **Output**

  

  

    
    
    Apple 0 5 ORG
    U.K. 27 31 GPE
    $1 billion 44 54 MONEY
    

In the output, the first column specifies the entity, the next two columns the
start and end characters within the sentence/document, and the final column
specifies the category.

Further, it is interesting to note that spaCy’s NER model uses capitalization
as one of the cues to identify named entities. The same example, when tested
with a slight modification, produces a different result.

 __

 __  
 __

 __

 __  
 __  
 __

import spacy

 

nlp = spacy.load('en_core_web_sm')

 

sentence = "apple is looking at buying U.K. startup for $1 billion"

 

doc = nlp(sentence)

 

for ent in doc.ents:

 print(ent.text, ent.start_char, ent.end_char, ent.label_)  
  
---  
  
 __

 __

 **Output**

    
    
    U.K. 27 31 GPE
    $1 billion 44 54 MONEY
    

The word “apple” no longer shows as a named entity. Therefore, it is important
to use NER before the usual normalization or stemming preprocessing steps.

One can also use their own examples to train and modify spaCy’s in-built NER
model. There are several ways to do this. The following code shows a simple
way to feed in new instances and update the model.

 __

 __  
 __

 __

 __  
 __  
 __

import spacy

from spacy.gold import GoldParse

from spacy.language import EntityRecognizer

 

nlp = spacy.load('en', entity = False, parser = False)

 

doc_list = []

doc = nlp('Llamas make great pets.')

doc_list.append(doc)

gold_list = []

gold_list.append(GoldParse(doc, [u'ANIMAL', u'O', u'O',
u'O']))

 

ner = EntityRecognizer(nlp.vocab, entity_types = ['ANIMAL'])

ner.update(doc_list, gold_list)  
  
---  
  
 __

 __

By adding a sufficient number of examples in the doc_list, one can produce a
customized NER using spaCy.

spaCy supports the following entity types:  
PERSON, NORP (nationalities, religious and political groups), FAC (buildings,
airports etc.), ORG (organizations), GPE (countries, cities etc.), LOC
(mountain ranges, water bodies etc.), PRODUCT (products), EVENT (event names),
WORK_OF_ART (books, song titles), LAW (legal document titles), LANGUAGE (named
languages), DATE, TIME, PERCENT, MONEY, QUANTITY, ORDINAL and CARDINAL.

 **References**

  * https://spacy.io/

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save

