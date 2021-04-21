Implement your own word2vec(skip-gram) model in Python



Prerequisite: Introduction to word2vec

Natural language processing (NLP) is a subfield of computer science and
artificial intelligence concerned with the interactions between computers and
human (natural) languages.  
In NLP techniques, we map the words and phrases (from vocabulary or corpus) to
vectors of numbers to make the processing easier. These types of **language
modeling** techniques are called **word embeddings**.

In 2013, Google announched **word2vec** , a group of related models that are
used to produce word embeddings.

Let’s implement our own skip-gram model (in Python) by deriving the
backpropagation equations of our neural network.

In **skip gram** architecture of word2vec, the input is the **center word**
and the predictions are the context words. Consider an array of words W, if
W(i) is the input (center word), then W(i-2), W(i-1), W(i+1), and W(i+2) are
the context words, if the _sliding window size_ is 2.  
![](https://media.geeksforgeeks.org/wp-content/uploads/word2vec_diagram-1.jpg)

  

  

    
    
    Let's define some variables :
    
    **V**    Number of unique words in our corpus of text ( **V** ocabulary )
    **x**    Input layer (One hot encoding of our input word ). 
    **N**    Number of neurons in the hidden layer of neural network
    **W**    Weights between input layer and hidden layer
    **W'**   Weights between hidden layer and output layer
    **y**    A softmax output layer having probabilities of every word in our vocabulary
    

![Skip gram architecture ](https://media.geeksforgeeks.org/wp-
content/uploads/Skip-gram-architecture-2.jpg)

Skip gram architecture

Our neural network architecture is defined, now let’s do some math to derive
the equations needed for gradient descent.

### Forward Propagation:

Multiplying one hot encoding of centre word (denoted by **x** ) with the first
weight matrix **W** to get hidden layer matrix **h** (of size N x 1).  
![  h = W^T.x ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-94256012589a5b5900ba6ed998ebda55_l3.png)  
 ** _( Vx1 ) ( NxV ) ( Vx1 )_**  
  
Now we multiply the hidden layer vector **h** with second weight matrix **W’**
to get a new matrix **u**

![ u = W'^T.h ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-ec39e1aac1fcd0443e5862b0ff6b35ed_l3.png)  
 ** _( Vx1 ) ( VxN ) ( Nx1 )_**  
Note that we have to apply a softmax> to _layer u_ to get our _output layer
y_.

Let **u j** be jth neuron of layer **u**  
Let **w j** be the jth word in our vocabulary where j is any index  
Let **V wj** be the jth column of matrix **W’** (column corresponding to a
**word w j**)

