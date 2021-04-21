Python | Lemmatization with TextBlob



Lemmatization is the process of grouping together the different inflected
forms of a word so they can be analysed as a single item. Lemmatization is
similar to stemming but it brings context to the words. So it links words with
similar meaning to one word.

Text preprocessing includes both Stemming as well as Lemmatization. Many times
people find these two terms confusing. Some treat these two as same. Actually,
lemmatization is preferred over Stemming because lemmatization does
morphological analysis of the words.

 **Applications of lemmatization are:**

  * Used in comprehensive retrieval systems like search engines.
  * Used in compact indexing.

    
    
    Examples of lemmatization :
    
    -> rocks : rock
    -> corpora : corpus
    -> better : good
    

One major difference with stemming is that lemmatize takes a part of speech
parameter, “pos” If not supplied, the default is “noun.”

Below is the implementation of lemmatization words using TextBlob:

 __

 __  
 __

 __

 __  
 __  
 __

# from textblob lib import Word method

from textblob import Word

 

# create a Word object.

u = Word("rocks")

 

# apply lemmatization.

print("rocks :", u.lemmatize())

 

# create a Word object.

v = Word("corpora")

 

# apply lemmatization.

print("corpora :", v.lemmatize())

 

# create a Word object.

w = Word("better")

 

# apply lemmatization with 

# parameter "a", "a" denotes adjective.

print("better :", w.lemmatize("a"))  
  
---  
  
 __

 __

 **Output :**

    
    
    rocks : rock
    corpora : corpus
    better : good
    

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save

