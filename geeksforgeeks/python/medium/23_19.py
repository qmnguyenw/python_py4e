Readability Index in Python(NLP)



Readability is the ease with which a reader can understand a written text. In
natural language, the readability of text depends on its content (the
complexity of its vocabulary and syntax). It focuses on the words we choose,
and how we put them into sentences and paragraphs for the readers to
comprehend.  
Our main objective in writing is to pass along information that both the
writer and the reader think is worthwhile. If we fail to convey that
information, our efforts are wasted. In order to engage the reader, it’s
critical to present information to them that they’ll gladly keep reading and
be able to understand clearly. So, it is required that the content be easy
enough to read and understand thus is as readable as possible.There are
various available Difficulty Scales with their own difficulty determining
formulae.

This article illustrates various traditional readability formulae available
for readability score evaluation. In Natural Language Processing, sometimes it
is required to analyse words and sentences to determine the difficulty of the
text. Readability Scores are generally grade levels on particular scales,
which rates the text as to whats the difficulty of that particular text. It
assists the writer in improving the text to make it understandable for a
larger audience, thus making content engaging.

Various available Readabilty Score Determination Methods/Formaulae:-

1) The Dale–Chall formula  
2) The Gunning fog formula  
3) Fry readability graph  
4) McLaughlin’s SMOG formula  
5) The FORCAST formula  
6) Readability and newspaper readership  
7) Flesch Scores  
Read about more available Readability Formulae from here.

The implementation of the readability formulae is shown below.  
 **The Dale Chall Formula**

  

  

To apply the formula:

Select several 100-word samples throughout the text.  
Compute the average sentence length in words (divide the number of words by
the number of sentences).  
Compute the percentage of words NOT on the Dale–Chall word list of 3, 000 easy
words.  
Compute this equation

    
    
     Raw score = 0.1579*(PDW) + 0.0496*(ASL) + 3.6365
    Here,
    PDW = Percentage of difficult words not on the Dale–Chall word list.
    ASL = Average sentence length
    

**The Gunning fog Formula**

    
    
    Grade level= 0.4 * ( (average sentence length) + (percentage of Hard Words) )
    Here, Hard Words = words with more than two syllables.
    

**Smog Formula**

    
    
    SMOG grading = 3 + √(polysyllable count).
    Here, polysyllable count = number of words of more than two syllables in a 
    sample of 30 sentences.
    

**Flesch Formula**

    
    
    Reading Ease score = 206.835 - (1.015 × ASL) - (84.6 × ASW)
    Here,
    ASL = average sentence length (number of words divided by number of sentences)
    ASW = average word length in syllables (number of syllables divided by number of words)
    

**Advantages** of Readability Formulae:

1\. Readability formulas measure the grade-level readers must have to be to
read a given text. Thus provides the writer of the text with much needed
information to reach his target audience.

2\. Know Before hand if the target audience can understand your content.

  

  

3\. Easy-to-use.

4\. A readable text attracts more audience.

 **Disadvantages** of Readability Formulae:

1\. Due to many readability formulas, there is an increasing chance of getting
wide variations in results of a same text.

2\. Applies Mathematics to Literature which isn’t always a good idea.

3\. Cannot measure the complexity of a word or phrase to pinpoint where you
need to correct it.

 __

 __  
 __

 __

 __  
 __  
 __

import spacy

from textstat.textstat import textstatistics, easy_word_set,
legacy_round

 

# Splits the text into sentences, using 

# Spacy's sentence segmentation which can 

# be found at https://spacy.io/usage/spacy-101

def break_sentences(text):

 nlp = spacy.load('en')

 doc = nlp(text)

 return doc.sents

 

# Returns Number of Words in the text

def word_count(text):

 sentences = break_sentences(text)

 words = 0

 for sentence in sentences:

 words += len([token for token in sentence])

 return words

 

# Returns the number of sentences in the text

def sentence_count(text):

 sentences = break_sentences(text)

 return len(sentences)

 

# Returns average sentence length

def avg_sentence_length(text):

 words = word_count(text)

 sentences = sentence_count(text)

 average_sentence_length = float(words / sentences)

 return average_sentence_length

 

# Textstat is a python package, to calculate statistics from 

# text to determine readability, 

# complexity and grade level of a particular corpus.

# Package can be found at https://pypi.python.org/pypi/textstat

def syllables_count(word):

 return textstatistics().syllable_count(word)

 

# Returns the average number of syllables per

# word in the text

def avg_syllables_per_word(text):

 syllable = syllables_count(text)

 words = word_count(text)

 ASPW = float(syllable) / float(words)

 return legacy_round(ASPW, 1)

 

# Return total Difficult Words in a text

def difficult_words(text):

 

 # Find all words in the text

 words = []

 sentences = break_sentences(text)

 for sentence in sentences:

 words += [str(token) for token in sentence]

 

 # difficult words are those with syllables >= 2

 # easy_word_set is provide by Textstat as 

 # a list of common words

 diff_words_set = set()

 

 for word in words:

 syllable_count = syllables_count(word)

 if word not in easy_word_set and syllable_count >= 2:

 diff_words_set.add(word)

 

 return len(diff_words_set)

 

# A word is polysyllablic if it has more than 3 syllables

# this functions returns the number of all such words 

# present in the text

def poly_syllable_count(text):

 count = 0

 words = []

 sentences = break_sentences(text)

 for sentence in sentences:

 words += [token for token in sentence]

 

 

 for word in words:

 syllable_count = syllables_count(word)

 if syllable_count >= 3:

 count += 1

 return count

 

 

def flesch_reading_ease(text):

 """

 Implements Flesch Formula:

 Reading Ease score = 206.835 - (1.015 × ASL) - (84.6 × ASW)

 Here,

 ASL = average sentence length (number of words 

 divided by number of sentences)

 ASW = average word length in syllables (number of syllables 

 divided by number of words)

 """

 FRE = 206.835 - float(1.015 * avg_sentence_length(text))
-\

 float(84.6 * avg_syllables_per_word(text))

 return legacy_round(FRE, 2)

 

 

def gunning_fog(text):

 per_diff_words = (difficult_words(text) / word_count(text) *
100) + 5

 grade = 0.4 * (avg_sentence_length(text) + per_diff_words)

 return grade

 

 

def smog_index(text):

 """

 Implements SMOG Formula / Grading

 SMOG grading = 3 + ?polysyllable count.

 Here, 

 polysyllable count = number of words of more

 than two syllables in a sample of 30 sentences.

 """

 

 if sentence_count(text) >= 3:

 poly_syllab = poly_syllable_count(text)

 SMOG = (1.043 * (30*(poly_syllab /
sentence_count(text)))**0.5) \

 + 3.1291

 return legacy_round(SMOG, 1)

 else:

 return 0

 

 

def dale_chall_readability_score(text):

 """

 Implements Dale Challe Formula:

 Raw score = 0.1579*(PDW) + 0.0496*(ASL) + 3.6365

 Here,

 PDW = Percentage of difficult words.

 ASL = Average sentence length

 """

 words = word_count(text)

 # Number of words not termed as difficult words

 count = word_count - difficult_words(text)

 if words > 0:

 

 # Percentage of words not on difficult word list

 

 per = float(count) / float(words) * 100

 

 # diff_words stores percentage of difficult words

 diff_words = 100 - per

 

 raw_score = (0.1579 * diff_words) + \

 (0.0496 * avg_sentence_length(text))

 

 # If Percentage of Difficult Words is greater than 5 %, then;

 # Adjusted Score = Raw Score + 3.6365,

 # otherwise Adjusted Score = Raw Score

 

 if diff_words > 5: 

 

 raw_score += 3.6365

 

 return legacy_round(score, 2)  
  
---  
  
 __

 __

 **  
Source :**  
https://en.wikipedia.org/wiki/Readability

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

