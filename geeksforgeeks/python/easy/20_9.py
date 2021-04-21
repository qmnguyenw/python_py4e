Python | NLP analysis of Restaurant reviews



 **Natural language processing (NLP)** is an area of computer science and
artificial intelligence concerned with the interactions between computers and
human (natural) languages, in particular how to program computers to process
and analyze large amounts of natural language data. It is the branch of
machine learning which is about analyzing any text and handling predictive
analysis.

 **Scikit-learn** is a free software machine learning library for Python
programming language. Scikit-learn is largely written in Python, with some
core algorithms written in Cython to achieve performance. Cython is a superset
of the Python programming language, designed to give C-like performance with
code that is written mostly in Python.

Let’s understand the various steps involved in text processing and the flow of
NLP.

This algorithm can be easily applied to any other kind of text like classify
book into like Romance, Friction, but for now, let’s use a restaurant review
dataset to review negative or positive feedback.

#### Steps involved:

 **Step 1:** Import dataset with setting delimiter as ‘\t’ as columns are
separated as tab space. Reviews and their category(0 or 1) are not separated
by any other symbol but with tab space as most of the other symbols are is the
review (like $ for price, ….!, etc) and the algorithm might use them as
delimiter, which will lead to strange behavior (like errors, weird output) in
output.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Importing Libraries

import numpy as np 

import pandas as pd 

 

# Import dataset

dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter =
'\t')   
  
---  
  
__

__

To download the Restaurant_Reviews.tsv dataset used, clickhere.

 **Step 2:** Text Cleaning or Preprocessing

  *  **Remove Punctuations, Numbers** : Punctuations, Numbers doesn’t help much in processong the given text, if included, they will just increase the size of bag of words that we will create as last step and decrase the efficency of algorithm.
  *  **Stemming** : Take roots of the word  
![](https://media.geeksforgeeks.org/wp-content/uploads/stemming.png)

  *  **Convert each word into its lower case** : For example, it useless to have same words in different cases (eg ‘good’ and ‘GOOD’).

 __

 __  
 __

 __

 __  
 __  
 __

# library to clean data

import re 

 

# Natural Language Tool Kit

import nltk 

 

nltk.download('stopwords')

 

# to remove stopword

from nltk.corpus import stopwords

 

# for Stemming propose 

from nltk.stem.porter import PorterStemmer

 

# Initialize empty array

# to append clean text 

corpus = [] 

 

# 1000 (reviews) rows to clean

for i in range(0, 1000): 

 

 # column : "Review", row ith

 review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i]) 

 

 # convert all cases to lower cases

 review = review.lower() 

 

 # split to array(default delimiter is " ")

 review = review.split() 

 

 # creating PorterStemmer object to

 # take main stem of each word

 ps = PorterStemmer() 

 

 # loop for stemming each word

 # in string array at ith row 

 review = [ps.stem(word) for word in review

 if not word in set(stopwords.words('english'))] 

 

 # rejoin all string array elements

 # to create back into a string

 review = ' '.join(review) 

 

 # append each string to create

 # array of clean text 

 corpus.append(review)   
  
---  
  
__

__

**Examples:** Before and after applying above code (reviews = > before, corpus
=> after)

![](https://media.geeksforgeeks.org/wp-content/uploads/data_cleaning.png)

 **Step 3:** Tokenization

