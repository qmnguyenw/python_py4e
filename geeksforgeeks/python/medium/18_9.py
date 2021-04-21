Python | Sentiment Analysis using VADER



 **Sentiment Analysis** is the process of ‘computationally’ determining
whether a piece of writing is positive, negative or neutral. It’s also known
as **opinion mining** , deriving the opinion or attitude of a speaker.

 **Why sentiment analysis?**

  *  **Business:** In marketing field companies use it to develop their strategies, to understand customers’ feelings towards products or brand, how people respond to their campaigns or product launches and why consumers don’t buy some products.
  *  **Politics:** In the political field, it is used to keep track of political view, to detect consistency and inconsistency between statements and actions at the government level. It can be used to predict election results as well! .
  *  **Public Actions:** Sentiment analysis also is used to monitor and analyse social phenomena, for the spotting of potentially dangerous situations and determining the general mood of the blogosphere.

Command to install **vaderSentiment** :

    
    
    pip install vaderSentiment

  
**VADER Sentiment Analysis :**

 **VADER (Valence Aware Dictionary and sEntiment Reasoner)** is a lexicon and
rule-based sentiment analysis tool that is specifically attuned to sentiments
expressed in social media. **VADER** uses a combination of A sentiment
lexicon is a list of lexical features (e.g., words) which are generally
labeled according to their semantic orientation as either positive or
negative. **VADER** not only tells about the Positivity and Negativity score
but also tells us about how positive or negative a sentiment is.

  

  

Below is the code:

 __

 __  
 __

 __

 __  
 __  
 __

# import SentimentIntensityAnalyzer class

# from vaderSentiment.vaderSentiment module.

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

 

# function to print sentiments

# of the sentence.

def sentiment_scores(sentence):

 

 # Create a SentimentIntensityAnalyzer object.

 sid_obj = SentimentIntensityAnalyzer()

 

 # polarity_scores method of SentimentIntensityAnalyzer

 # oject gives a sentiment dictionary.

 # which contains pos, neg, neu, and compound scores.

 sentiment_dict = sid_obj.polarity_scores(sentence)

 

 print("Overall sentiment dictionary is : ", sentiment_dict)

 print("sentence was rated as ", sentiment_dict['neg']*100,
"% Negative")

 print("sentence was rated as ", sentiment_dict['neu']*100,
"% Neutral")

 print("sentence was rated as ", sentiment_dict['pos']*100,
"% Positive")

 

 print("Sentence Overall Rated As", end = " ")

 

 # decide sentiment as positive, negative and neutral

 if sentiment_dict['compound'] >= 0.05 :

 print("Positive")

 

 elif sentiment_dict['compound'] <= - 0.05 :

 print("Negative")

 

 else :

 print("Neutral")

 

 

 

# Driver code

if __name__ == "__main__" :

 

 print("\n1st statement :")

 sentence = "Geeks For Geeks is the best portal for \

 the computer science engineering students."

 

 # function calling

 sentiment_scores(sentence)

 

 print("\n2nd Statement :")

 sentence = "study is going on as usual"

 sentiment_scores(sentence)

 

 print("\n3rd Statement :")

 sentence = "I am vey sad today."

 sentiment_scores(sentence)  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-content/uploads/sentiment_analysis.png)

The Compound score is a metric that calculates the sum of all the lexicon
ratings which have been normalized between -1(most extreme negative) and +1
(most extreme positive).

positive sentiment : (compound score >= 0.05)  
neutral sentiment : (compound score > -0.05) and (compound score < 0.05)  
negative sentiment : (compound score <= -0.05)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

