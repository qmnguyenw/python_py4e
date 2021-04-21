Sentiments in Text – Word Based Encodings



 **Sentimental analysis** is the processing of describing whether a particular
feeling or an opinion is positive, negative, or neutral. For example, ” I hate
my Lunch”, “I love my Lunch” and “I am fine with my Lunch”.There is a
negative, positive, and neutral tone in each of these sentences. On a large
scale, Sentimental Analysis is used in determining the customer’s feedback
through comments. These comments help in building recommendation systems for
future reference.

## How to get the meaning of a word in a sentence?

We could have taken ASCII values of a character, but would that help us
understand the semantics of a word?. Let us take the word “binary” into
consideration, it can also be written as “brainy”. Clearly, both of these
words share the same ASCII value but has a different meaning altogether. It is
a tough task to train a neural network with words. The solution to all of this
is if we could give words value and use them in the training model

Consider this sentence ” I love my lunch” let us give some random number to
it. Let’s say the values are 1, 2, 3, and 4 respectively. Let’s say we have
another sentence which is “I love my cat”, we can reuse the previous values
and give a new token to the word “cat”. Let’s say the value of the cat is 5.
There is a similarity of 4 values in both of those sentences. It’s a start on
how to train a neural network. Fortunately, we have API’s like **Tensorflow**.
Follow the below steps to train your model

  *  **Step1:** Importing required Libraries

*  **Step2:** Create a List of sentences

  

  

*  **Step3:** Create a Tokenizer object

