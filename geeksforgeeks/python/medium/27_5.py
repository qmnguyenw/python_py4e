Removing stop words with NLTK in Python



The process of converting data to something a computer can understand is
referred to as **pre-processing.** One of the major forms of pre-processing is
to filter out useless data. In natural language processing, useless words
(data), are referred to as stop words.

 **What are Stop words?**

 **Stop Words:** A stop word is a commonly used word (such as “the”, “a”,
“an”, “in”) that a search engine has been programmed to ignore, both when
indexing entries for searching and when retrieving them as the result of a
search query.

We would not want these words to take up space in our database, or taking up
valuable processing time. For this, we can remove them easily, by storing a
list of words that you consider to stop words. NLTK(Natural Language Toolkit)
in python has a list of stopwords stored in 16 different languages. You can
find them in the nltk_data directory.
_home/pratima/nltk_data/corpora/stopwords_ is the directory address.(Do not
forget to change your home directory name)![Stop word removal using
NLTK](https://media.geeksforgeeks.org/wp-content/cdn-uploads/Stop-word-
removal-using-NLTK.png)

 **To check the list of stopwords you can type the following commands in the
python shell.**

  

  

    
    
    import nltk
    from nltk.corpus import stopwords
    print(stopwords.words('english'))

{‘ourselves’, ‘hers’, ‘between’, ‘yourself’, ‘but’, ‘again’, ‘there’, ‘about’,
‘once’, ‘during’, ‘out’, ‘very’, ‘having’, ‘with’, ‘they’, ‘own’, ‘an’, ‘be’,
‘some’, ‘for’, ‘do’, ‘its’, ‘yours’, ‘such’, ‘into’, ‘of’, ‘most’, ‘itself’,
‘other’, ‘off’, ‘is’, ‘s’, ‘am’, ‘or’, ‘who’, ‘as’, ‘from’, ‘him’, ‘each’,
‘the’, ‘themselves’, ‘until’, ‘below’, ‘are’, ‘we’, ‘these’, ‘your’, ‘his’,
‘through’, ‘don’, ‘nor’, ‘me’, ‘were’, ‘her’, ‘more’, ‘himself’, ‘this’,
‘down’, ‘should’, ‘our’, ‘their’, ‘while’, ‘above’, ‘both’, ‘up’, ‘to’,
‘ours’, ‘had’, ‘she’, ‘all’, ‘no’, ‘when’, ‘at’, ‘any’, ‘before’, ‘them’,
‘same’, ‘and’, ‘been’, ‘have’, ‘in’, ‘will’, ‘on’, ‘does’, ‘yourselves’,
‘then’, ‘that’, ‘because’, ‘what’, ‘over’, ‘why’, ‘so’, ‘can’, ‘did’, ‘not’,
‘now’, ‘under’, ‘he’, ‘you’, ‘herself’, ‘has’, ‘just’, ‘where’, ‘too’, ‘only’,
‘myself’, ‘which’, ‘those’, ‘i’, ‘after’, ‘few’, ‘whom’, ‘t’, ‘being’, ‘if’,
‘theirs’, ‘my’, ‘against’, ‘a’, ‘by’, ‘doing’, ‘it’, ‘how’, ‘further’, ‘was’,
‘here’, ‘than’}

 **Note:** You can even modify the list by adding words of your choice in the
english .txt. file in the stopwords directory.

 **Removing stop words with NLTK**

The following program removes stop words from a piece of text:

 __

 __  
 __

 __

 __  
 __  
 __

from nltk.corpus import stopwords 

from nltk.tokenize import word_tokenize 

 

example_sent = """This is a sample sentence,

 showing off the stop words filtration."""

 

stop_words = set(stopwords.words('english')) 

 

word_tokens = word_tokenize(example_sent) 

 

filtered_sentence = [w for w in word_tokens if not w in
stop_words] 

 

filtered_sentence = [] 

 

for w in word_tokens: 

 if w not in stop_words: 

 filtered_sentence.append(w) 

 

print(word_tokens) 

print(filtered_sentence)   
  
---  
  
__

__

Output:

    
    
    ['This', 'is', 'a', 'sample', 'sentence', ',', 'showing', 
    'off', 'the', 'stop', 'words', 'filtration', '.']
    ['This', 'sample', 'sentence', ',', 'showing', 'stop',
    'words', 'filtration', '.']

 **Performing the Stopwords operations in a file**

In the code below, text.txt is the original input file in which stopwords are
to be removed. filteredtext.txt is the output file. It can be done using
following code:

 __

 __  
 __

 __

 __  
 __  
 __

import io 

from nltk.corpus import stopwords 

from nltk.tokenize import word_tokenize 

 

# word_tokenize accepts

# a string as an input, not a file. 

stop_words = set(stopwords.words('english')) 

file1 = open("text.txt") 

 

# Use this to read file content as a stream: 

line = file1.read()

words = line.split() 

for r in words: 

 if not r in stop_words: 

 appendFile = open('filteredtext.txt','a') 

 appendFile.write(" "+r) 

 appendFile.close()   
  
---  
  
__

__

This is how we are making our processed content more efficient by removing
words that do not contribute to any future operations.

This article is contributed by **Pratima Upadhyay**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save

