Corona HelpBot



This is a chatbot that will give answers to most of your corona related
questions/FAQ. The chatbot will give you answers from the data given by
WHO(https://www.who.int/). This will help those who need information or help
to know more about this virus.

It uses a neural network with two hidden layers(enough for these QnA) that
predicts which pattern matches with the user’s question and sends toward that
node. More patterns can be added from user’s questions to train it for more
improved results and add more info about coronavirus in the JSON file. The
more you train this chatbot the more it gets precise. The advantage of using
deep learning is that you don’t have to ask the same question as written in
JSON file cause stemmed words from the pattern are matched with user question

 **Prerequsites:**

    
    
    Python 3
    NumPy
    nltk
    TensorFlow v.1.15 (no GPU required)
    tflearn

 **Training Data:**  
To feed the data to chatbot I have used json with possible question patterns
and our desired answers.  
The JSON file used for the project is WHO  
For this project, I have named my JSON file as WHO.json  
In the JSON file tag is the category in which all those responses fall.  
patterns are used for listing all possible question patterns.  
responses contains all the responses with respect to the patterned questions

 __

 __  
 __

 __

 __  
 __  
 __

import nltk

import numpy

import tflearn

import tensorflow

import pickle

import random

import json

nltk.download('punkt')

 

from nltk.stem.lancaster import LancasterStemmer

stemmer = LancasterStemmer()

 

 #loading the json data

with open("WHO.json") as file: 

 data = json.load(file)

 

#print(data["intents"])

try:

 with open("data.pickle", "rb") as f:

 words, l, training, output = pickle.load(f)

except:

 

 # Extracting Data

 words = []

 l = []

 docs_x = []

 docs_y = []

 

 # converting each pattern into list of words using nltk.word_tokenizer 

 for i in data["intents"]: 

 for p in i["patterns"]:

 wrds = nltk.word_tokenize(p)

 words.extend(wrds)

 docs_x.append(wrds)

 docs_y.append(i["tag"])

 

 if i["tag"] not in l:

 l.append(i["tag"])

 # Word Stemming 

 words = [stemmer.stem(w.lower()) for w in words if w !=
"?"] 

 words = sorted(list(set(words)))

 l = sorted(l) 

 

 # This code will simply create a unique list of stemmed 

 # words to use in the next step of our data preprocessing

 training = []

 output = []

 out_empty = [0 for _ in range(len(l))]

 for x, doc in enumerate(docs_x):

 bag = []

 

 wrds = [stemmer.stem(w) for w in doc]

 

 for w in words:

 if w in wrds:

 bag.append(1)

 else:

 bag.append(0)

 output_row = out_empty[:]

 output_row[l.index(docs_y[x])] = 1

 

 training.append(bag)

 output.append(output_row)

 

 # Finally we will convert our training data and output to numpy arrays 

 training = numpy.array(training) 

 output = numpy.array(output)

 with open("data.pickle", "wb") as f:

 pickle.dump((words, l, training, output), f)

 

 

# Developing a Model 

tensorflow.reset_default_graph() 

 

net = tflearn.input_data(shape=[None, len(training[0])])

net = tflearn.fully_connected(net, 8)

net = tflearn.fully_connected(net, 8)

net = tflearn.fully_connected(net, len(output[0]),
activation="softmax")

net = tflearn.regression(net)

 

 

# remove comment to not train model after you satisfied with the accuracy

model = tflearn.DNN(net)

"""try: 

 model.load("model.tflearn")

except:"""

 

# Training & Saving the Model

model.fit(training, output, n_epoch=1000, batch_size=8,
show_metric=True) 

model.save("model.tflearn")

 

# making predictions

def bag_of_words(s, words): 

 bag = [0 for _ in range(len(words))]

 

 s_words = nltk.word_tokenize(s)

 s_words = [stemmer.stem(word.lower()) for word in s_words]

 

 for se in s_words:

 for i, w in enumerate(words):

 if w == se:

 bag[i] = 1

 

 return numpy.array(bag)

 

 

def chat():

 print("""Start talking with the bot and ask your

 queries about Corona-virus(type quit to stop)!""")

 

 while True:

 inp = input("You: ")

 if inp.lower() == "quit":

 break

 

 results = model.predict([bag_of_words(inp, words)])[0]

 results_index = numpy.argmax(results)

 

 #print(results_index)

 tag = l[results_index]

 if results[results_index] > 0.7:

 for tg in data["intents"]:

 if tg['tag'] == tag:

 responses = tg['responses']

 

 print(random.choice(responses))

 else:

 print("I am sorry but I can't understand")

 

chat()  
  
---  
  
 __

 __

 **Bag of Words:**  
As we know neural networks and machine learning algorithms require numerical
input. So out list of strings won’t cut it. We need some way to represent our
sentences with numbers and this is where a bag of words comes in.What we are
going to do is represent each sentence with a list the length of the number of
words in our model vocabulary. Each position in the list will represent a word
from our vocabulary.f the position in the list is a 1 then that will mean that
the word exists in our sentence, if it is a 0 then the word is nor present.

  

  

 **Developing a Model:**

    
    
    model = tflearn.DNN(net)
    model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True) 
    model.save("model.tflearn")

Our chat-bot will predict the answers based on the model we train. Here we
will use the neural networks to build the model. The goal of our network will
be to look at a bag of words and give a class that they belong too (one of our
tags from the JSON file).

    
    
    **Input:** what is coronavirus ?
    **Output:** COVID-19 is an infectious disease caused by the most recently discovered coronavirus. This new virus and disease were unknown before the outbreak began in Wuhan, China, in December 2019.
    
    **Input:** what are the symptoms of COVID 19?
    **Output:** He most common symptoms of COVID-19 are fever, tiredness, and dry cough. Some patients may have aches and pains, nasal congestion, runny nose, sore throat or diarrhea. These symptoms are usually mild and begin gradually. Some people become infected but don’t develop any symptoms and don't feel unwell. Most people (about 80%) recover from the disease without needing special treatment.
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

