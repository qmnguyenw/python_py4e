Softmax Regression using TensorFlow



This article discusses the basics of Softmax Regression and its implementation
in Python using TensorFlow library.

 **What is Softmax Regression?**

 **Softmax regression** (or **multinomial logistic regression** ) is a
generalization of **logistic regression** to the case where we want to handle
multiple classes.

A gentle introduction to **linear regression** can be found here:  
Understanding Logistic Regression

In binary logistic regression we assumed that the labels were binary, i.e. for
![i^{th}](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-
fed8e1e15a62215e09e863591008fc5b_l3.png) observation,  
![y_{i} \\epsilon \\begin{Bmatrix} 0, 1
\\end{Bmatrix}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-566eeac28883e874149768934e168d7c_l3.png)

  

  

But consider a scenario where we need to classify an observation out of two or
more class labels. For example, digit classification. Here, the possible
labels are:  
![y_{i} \\epsilon \\begin{Bmatrix} 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
\\end{Bmatrix}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-02bc1b124c1341afc6ef533b28938703_l3.png)

In such cases, we can use **Softmax Regression**.

Let us first define our model:

  * Let the dataset have ‘m’ features and ‘n’ observations. Also, there are ‘k’ class labels, i.e every observation can be classified as one of the ‘k’ possible target values. For example, if we have a dataset of 100 handwritten digit images of vector size 28×28 for digit classification, we have, n = 100, m = 28×28 = 784 and k = 10.

  *  **Feature matrix  
** The feature matrix, ![X](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-5869604716aa86d49cd788029abbddab_l3.png), is represented
as:
![](https://latex.codecogs.com/gif.latex?%5Cmathbf%7BX%7D%20%3D%5Cbegin%7Bpmatrix%7D%201%20%26%20x_%7B11%7D%20%26%20%5Ccdots%20%26%20x_%7B1m%7D%20%5C%5C%201%20%26%20x_%7B21%7D%20%26%20%5Ccdots%20%26%20x_%7B2m%7D%20%5C%5C%20%5Cvdots%20%26%20%5Cvdots%20%26%20%5Cddots%20%26%20%5Cvdots%20%5C%5C%201%20%26%20x_%7Bn1%7D%20%26%20%5Ccdots%20%26%20x_%7Bnm%7D%20%5Cend%7Bpmatrix%7D)
Here, ![x_{ij}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-a45720ee1c29d58a039f138f424bf95f_l3.png) denotes the
values of ![j^{th}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-1887521be6b3b70e9e6b57a8e1846340_l3.png) feature for
![i^{th}](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-
fed8e1e15a62215e09e863591008fc5b_l3.png) observation. The matrix has
dimensions: ![n\\space X \\space \(m+1\)](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-95e80a077962b4b83cc166852a16a8a6_l3.png)

  * **Weight matrix  
** We define a weight matrix, ![W](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-c6e210274d17973952b9edf821c5ff9b_l3.png) as:
![](https://latex.codecogs.com/gif.latex?%5Cmathbf%7BW%7D%20%3D%5Cbegin%7Bpmatrix%7D%20w_%7B01%7D%20%26%20w_%7B02%7D%20%26%20%5Ccdots%20%26%20w_%7B0k%7D%20%5C%5C%20w_%7B11%7D%20%26%20w_%7B12%7D%20%26%20%5Ccdots%20%26%20w_%7B1k%7D%20%5C%5C%20%5Cvdots%20%26%20%5Cvdots%20%26%20%5Cddots%20%26%20%5Cvdots%20%5C%5C%20w_%7Bm1%7D%20%26%20w_%7Bm2%7D%20%26%20%5Ccdots%20%26%20w_%7Bmk%7D%20%5Cend%7Bpmatrix%7D)Here,
![w_{ij}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-0970592822294cf44e01dad49fba0d2c_l3.png) represents the
weight assigned to ![i^{th}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-fed8e1e15a62215e09e863591008fc5b_l3.png) feature for
![j^{th}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-1887521be6b3b70e9e6b57a8e1846340_l3.png) class label. The
matrix has dimensions:![\(m+1\)\\space X \\space
k](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-f41600ab45955fe83c51f61eca1469bd_l3.png). Initially,
weight matrix is filled using some normal distribution.

  *  **Logit score matrix  
** Then, we define our net input matrix(also called **logit score matrix** ),
![Z](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-a5ca1dd91339657388197faa50b79a6d_l3.png), as:
![](https://latex.codecogs.com/gif.latex?Z%20%3D%20XW) The matrix has
dimensions: ![n \\space X \\space k](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-87a377b4504bc1152497e4860436b82e_l3.png).

> Currently, we are taking an extra column in feature matrix,
> ![X](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-5869604716aa86d49cd788029abbddab_l3.png) and an extra
> row in weight matrix, ![W](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-c6e210274d17973952b9edf821c5ff9b_l3.png). These extra
> columns and rows correspond to the bias terms associated with each
> prediction. This could be simplified by defining an extra matrix for bias,
> ![b](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-84c9ca09709086867a3040914718f2bb_l3.png) of size ![n
> \\space X \\space k](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-87a377b4504bc1152497e4860436b82e_l3.png) where ![b_{ij}
> = w_{0j}](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-424c81639f1dc80af7ff1e927fba628d_l3.png). (In practice,
> all we need is a vector of size ![k](https://www.geeksforgeeks.org/wp-
> content/ql-cache/quicklatex.com-0be5415bdedad4aba541fa1cb6f7f64b_l3.png) and
> some broadcasting techniques for the bias terms!)
>
> So, the final score matrix, ![Z](https://www.geeksforgeeks.org/wp-
> content/ql-cache/quicklatex.com-a5ca1dd91339657388197faa50b79a6d_l3.png) is:
>
> ![](https://latex.codecogs.com/gif.latex?Z%20%3D%20XW+b)
>
> where ![X](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-5869604716aa86d49cd788029abbddab_l3.png) matrix has
> dimensions ![n\\space X \\space m](https://www.geeksforgeeks.org/wp-
> content/ql-cache/quicklatex.com-465147d7a53b6c71e9a8087f3a180cbe_l3.png)
> while ![W](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-c6e210274d17973952b9edf821c5ff9b_l3.png) has dimensions
> ![m\\space X \\space k](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-76050b209bac43196f008152c17bc3d9_l3.png). But
> ![Z](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-a5ca1dd91339657388197faa50b79a6d_l3.png) matrix still
> has same value and dimensions!
>
>  
>
>
>  
>

But what does matrix ![Z](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-a5ca1dd91339657388197faa50b79a6d_l3.png) signify?
Actually, ![Z_{ij}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-86bba84981665d87128dfabd08778a15_l3.png) is the
likelihood of label j for ![i^{th}](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-fed8e1e15a62215e09e863591008fc5b_l3.png)
observation. It is not a proper probability value but can be considered as a
score given to each class label for each observation!

Let us define ![Z_i](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-977e13d3c8efb342240bdd4797ead88c_l3.png) as the **logit
score vector** for ![i^{th}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-fed8e1e15a62215e09e863591008fc5b_l3.png) observation.

For example, let the vector ![Z_5 = \[1.1, 2.0, 3.1, 5.2, 1.0, 1.5, 0.2, 0.1,
1.2, 0.4\]](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-080ae98e71957737ece9d382a960e171_l3.png) represents the
score for each of the class labels
![{0,1,2,3,4,5,6,7,8,9}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-522451e50fdcf39d4880fae68d4db393_l3.png) in handwritten
digit classification problem for ![5^{th}](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-2ce06192a0a3ca0e98a5d792085f88c3_l3.png)
observation. Here, the max score is 5.2 which corresponds to class label ‘3’.
Hence, our model currently predicts the
![5^{th}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-2ce06192a0a3ca0e98a5d792085f88c3_l3.png)
observation/image as ‘3’.

  *  **Softmax layer  
** It is harder to train the model using score values since it is hard to
differentiate them while implementing **Gradient Descent algorithm** for
minimizing the cost function. So, we need some function which normalizes the
logit scores as well as makes them easily differentiable!In order to convert
the score matrix ![Z](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-a5ca1dd91339657388197faa50b79a6d_l3.png) to
probabilities, we use **Softmax function**.

For a vector ![y](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-5ff86b813b3643d6670e4e1bb889da39_l3.png), softmax
function ![S\(y\)](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-7a083eedbe5055b1b6e3900f0b239205_l3.png) is defined as:
![](https://latex.codecogs.com/gif.latex?S%28y_i%29%20%3D%20%5Cfrac%7Be%5E%7By_i%7D%7D%7B%5Csum_%7Bj%3D0%7De%5E%7By_j%7D%7D)
So, softmax function will do 2 things:

    
        1. convert all scores to probabilities.
    2. sum of all probabilities is 1.
    

Recall that in Binary Logistic classifier, we used **sigmoid function** for
the same task. Softmax function is nothing but a generalization of sigmoid
function! Now, this softmax function computes the probability that the
![i^{th}](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-
fed8e1e15a62215e09e863591008fc5b_l3.png) training sample belongs to class
![j](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-993d084f16613ab590616a3b93e4a1ed_l3.png) given the logits
vector ![Z_i](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-977e13d3c8efb342240bdd4797ead88c_l3.png) as:
![](https://latex.codecogs.com/gif.latex?P%28y%3Dj%7C%20Z_i%29%20%3D%20%5BS%28Z_i%29%5D_j%20%3D%20%5Cfrac%7Be%5E%7BZ_%7Bij%7D%7D%7D%7B%5Csum_%7Bp%3D0%7D%5E%7Bk%7D%7Be%5E%7BZ_%7Bip%7D%7D%7D%7D)

In vector form, we can simply write:
![](https://latex.codecogs.com/gif.latex?P%28y%7CZ_i%29%20%3D%20S%28Z_i%29)

For simplicity, let ![S_i](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-e19ce287943704fa6e979e490bd13699_l3.png) denote the
**softmax probability vector** for ![i^{th}](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-fed8e1e15a62215e09e863591008fc5b_l3.png)
observation.

  *  **One-hot encoded target matrix  
** Since softmax function provides us with a vector of probabilities of each
class label for a given observation, we need to convert target vector in the
same format to calculate the cost function! Corresponding to each observation,
there is a target vector (instead of a target value!) composed of only zeros
and ones where only correct label is set as 1. This technique is called **one-
hot encoding**.See the diagram given below for a better understanding:

![](https://media.geeksforgeeks.org/wp-content/uploads/one-hot.png)

Now, we denote one-hot encoding vector for
![i^{th}](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-
fed8e1e15a62215e09e863591008fc5b_l3.png) observation as
![T_i](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-c036464689aa4ef0f9367bb67b7f75e2_l3.png)

  * **Cost function  
** Now, we need to define a cost function for which, we have to compare the
softmax probabilities and one-hot encoded target vector for similarity. We use
the concept of **Cross-Entropy** for the same. The **Cross-entropy** is a
**distance calculation function** which takes the calculated probabilities
from softmax function and the created one-hot-encoding matrix to calculate the
distance. For the right target classes, the distance values will be lesser,
and the distance values will be larger for the wrong target classes.We define
cross entropy, ![D\(S_i,T_i\)](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-ff68e98bf443898c3e4432dcf1ae5c01_l3.png) for
![i^{th}](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-
fed8e1e15a62215e09e863591008fc5b_l3.png) observation with softmax probability
vector, ![S_i](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-e19ce287943704fa6e979e490bd13699_l3.png) and one-hot
target vector, ![T_i](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-c036464689aa4ef0f9367bb67b7f75e2_l3.png) as:
![](https://latex.codecogs.com/gif.latex?D%28S_i%2C%20T_i%29%20%3D%20-%5Csum_%7Bj%3D1%7D%5E%7Bk%7D%20%7BT_%7Bij%7D%20log%20S_%7Bij%7D%7D)

And now, cost function, ![J](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-903253bd4a404e77f4cf5d46f2375ea4_l3.png) can be defined
as the average cross entropy, i.e:
![](https://latex.codecogs.com/gif.latex?J%28W%2Cb%29%20%3D%20%5Cfrac%7B1%7D%7Bn%7D%5Csum_%7Bi%3D1%7D%5E%7Bn%7DD%28S_i%2CT_i%29)

and the task is to minimize this cost function!

  *  **Gradient Descent algorithm  
** In order to learn our softmax model via gradient descent, we need to
compute the derivative:
![](https://latex.codecogs.com/gif.latex?%5CDelta_W%20J%28W%2Cb%29) and
![](https://latex.codecogs.com/gif.latex?%5CDelta_b%20J%28W%2Cb%29)which we
then use to update the weights and biases in opposite direction of the
gradient:
![](https://latex.codecogs.com/gif.latex?w_j%20%3A%3D%20w_j%20-%20%5Calpha%5CDelta_W%20J%28W%2Cb%29)
and
![](https://latex.codecogs.com/gif.latex?b_j%20%3A%3D%20b_j%20-%20%5Calpha%5CDelta_b%20J%28W%2Cb%29)
for each class ![j](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-993d084f16613ab590616a3b93e4a1ed_l3.png) where ![j \\in
{1,2,..,k}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-3f42a754e9f02df59ccf1c8df90f77fc_l3.png) and
![\\alpha](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-091e0ab996bb6a7f0e720b84e9aee36f_l3.png) is learning
rate.Using this cost gradient, we iteratively update the weight matrix until
we reach a specified number of epochs (passes over the training set) or reach
the desired cost threshold.

 **Implementation**

Let us now implement **Softmax Regression** on the MNIST handwritten digit
dataset using **TensorFlow** library.

For a gentle introduction to **TensorFlow** , follow this tutorial:  
Introduction to TensorFlow  

 **Step 1: Import the dependencies**

First of all, we import the dependencies.

 __

 __  
 __

 __

 __  
 __  
 __

import tensorflow as tf

import numpy as np

import matplotlib.pyplot as plt  
  
---  
  
 __

 __

 **Step 2: Download the data**

TensorFlow allows you to download and read in the MNIST data automatically.
Consider the code given below. It will download and save data to the folder,
**MNIST_data** , in your current project directory and load it in current
program.

 __

 __  
 __

 __

 __  
 __  
 __

from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)  
  
---  
  
 __

 __

    
    
    Extracting MNIST_data/train-images-idx3-ubyte.gz
    Extracting MNIST_data/train-labels-idx1-ubyte.gz
    Extracting MNIST_data/t10k-images-idx3-ubyte.gz
    Extracting MNIST_data/t10k-labels-idx1-ubyte.gz

 **Step 3: Understanding data**

Now, we try to understand the structure of the dataset.

The MNIST data is split into three parts: 55,000 data points of training data
( **mnist.train** ), 10,000 points of test data ( **mnist.test** ), and 5,000
points of validation data ( **mnist.validation** ).

Each image is 28 pixels by 28 pixels which has been flattened into 1-D numpy
array of size 784. Number of class labels is 10. Each target label is already
provided in one-hot encoded form.

 __

 __  
 __

 __

 __  
 __  
 __

print("Shape of feature matrix:", mnist.train.images.shape)

print("Shape of target matrix:", mnist.train.labels.shape)

print("One-hot encoding for 1st observation:\n",
mnist.train.labels[0])

 

# visualize data by plotting images

fig,ax = plt.subplots(10,10)

k = 0

for i in range(10):

 for j in range(10):

 ax[i][j].imshow(mnist.train.images[k].reshape(28,28),
aspect='auto')

 k += 1

plt.show()  
  
---  
  
 __

 __

Output:

    
    
    Shape of feature matrix: (55000, 784)
    Shape of target matrix: (55000, 10)
    One-hot encoding for 1st observation:
     [ 0.  0.  0.  0.  0.  0.  0.  1.  0.  0.]
    ![](https://media.geeksforgeeks.org/wp-content/uploads/images_visual.png)
    

**Step 4: Defining computation graph**

Now, we create a computation graph.

 __

 __  
 __

 __

 __  
 __  
 __

# number of features

num_features = 784

# number of target labels

num_labels = 10

# learning rate (alpha)

learning_rate = 0.05

# batch size

batch_size = 128

# number of epochs

num_steps = 5001

 

# input data

train_dataset = mnist.train.images

train_labels = mnist.train.labels

test_dataset = mnist.test.images

test_labels = mnist.test.labels

valid_dataset = mnist.validation.images

valid_labels = mnist.validation.labels

 

# initialize a tensorflow graph

graph = tf.Graph()

 

with graph.as_default():

 """

 defining all the nodes

 """

 

 # Inputs

 tf_train_dataset = tf.placeholder(tf.float32, shape=(batch_size,
num_features))

 tf_train_labels = tf.placeholder(tf.float32, shape=(batch_size,
num_labels))

 tf_valid_dataset = tf.constant(valid_dataset)

 tf_test_dataset = tf.constant(test_dataset)

 

 # Variables.

 weights = tf.Variable(tf.truncated_normal([num_features,
num_labels]))

 biases = tf.Variable(tf.zeros([num_labels]))

 

 # Training computation.

 logits = tf.matmul(tf_train_dataset, weights) + biases

 loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(

 labels=tf_train_labels, logits=logits))

 

 # Optimizer.

 optimizer =
tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)

 

 # Predictions for the training, validation, and test data.

 train_prediction = tf.nn.softmax(logits)

 valid_prediction = tf.nn.softmax(tf.matmul(tf_valid_dataset, weights)
+ biases)

 test_prediction = tf.nn.softmax(tf.matmul(tf_test_dataset, weights)
+ biases)  
  
---  
  
 __

 __

Some important points to note:

  * For the training data, we use a placeholder that will be fed at run time with a training minibatch. The technique of using minibatches for training model using gradient descent is termed as **Stochastic Gradient Descent**.  

> In both gradient descent (GD) and stochastic gradient descent (SGD), you
> update a set of parameters in an iterative manner to minimize an error
> function. While in GD, you have to run through ALL the samples in your
> training set to do a single update for a parameter in a particular
> iteration, in SGD, on the other hand, you use ONLY ONE or SUBSET of training
> sample from your training set to do the update for a parameter in a
> particular iteration. If you use SUBSET, it is called Minibatch Stochastic
> gradient Descent. Thus, if the number of training samples are large, in fact
> very large, then using gradient descent may take too long because in every
> iteration when you are updating the values of the parameters, you are
> running through the complete training set. On the other hand, using SGD will
> be faster because you use only one training sample and it starts improving
> itself right away from the first sample. SGD often converges much faster
> compared to GD but the error function is not as well minimized as in the
> case of GD. Often in most cases, the close approximation that you get in SGD
> for the parameter values are enough because they reach the optimal values
> and keep oscillating there.

  * The weight matrix is initialized using random values following a (truncated) normal distribution. This is achieved using **tf.truncated_normal** method. The biases get initialized to zero using **tf.zeros** method.
  * Now, we multiply the inputs with the weight matrix, and add biases. We compute the softmax and cross-entropy using **tf.nn.softmax_cross_entropy_with_logits** (it’s one operation in TensorFlow, because it’s very common, and it can be optimized). We take the average of this cross-entropy across all training examples using **tf.reduce_mean** method.
  * We are going to minimize the loss using gradient descent. For this, we use **tf.train.GradientDescentOptimizer**.
  *  **train_prediction** , **valid_prediction** and **test_prediction** are not part of training, but merely here so that we can report accuracy figures as we train.

 **Step 5: Running the computation graph**

Since we have already built the computation graph, now it’s time to run it
through a session.

 __

 __  
 __

 __

 __  
 __  
 __

# utility function to calculate accuracy

def accuracy(predictions, labels):

 correctly_predicted = np.sum(np.argmax(predictions, 1) ==
np.argmax(labels, 1))

 accu = (100.0 * correctly_predicted) /
predictions.shape[0]

 return accu

 

with tf.Session(graph=graph) as session:

 # initialize weights and biases

 tf.global_variables_initializer().run()

 print("Initialized")

 

 for step in range(num_steps):

 # pick a randomized offset

 offset = np.random.randint(0, train_labels.shape[0] -
batch_size - 1)

 

 # Generate a minibatch.

 batch_data = train_dataset[offset:(offset + batch_size), :]

 batch_labels = train_labels[offset:(offset + batch_size), :]

 

 # Prepare the feed dict

 feed_dict = {tf_train_dataset : batch_data,

 tf_train_labels : batch_labels}

 

 # run one step of computation

 _, l, predictions = session.run([optimizer, loss, train_prediction],

 feed_dict=feed_dict)

 

 if (step % 500 == 0):

 print("Minibatch loss at step {0}: {1}".format(step, l))

 print("Minibatch accuracy: {:.1f}%".format(

 accuracy(predictions, batch_labels)))

 print("Validation accuracy: {:.1f}%".format(

 accuracy(valid_prediction.eval(), valid_labels)))

 

 print("\nTest accuracy: {:.1f}%".format(

 accuracy(test_prediction.eval(), test_labels)))  
  
---  
  
 __

 __

Output:

    
    
    Initialized
    Minibatch loss at step 0: 11.68728256225586
    Minibatch accuracy: 10.2%
    Validation accuracy: 14.3%
    Minibatch loss at step 500: 2.239773750305176
    Minibatch accuracy: 46.9%
    Validation accuracy: 67.6%
    Minibatch loss at step 1000: 1.0917563438415527
    Minibatch accuracy: 78.1%
    Validation accuracy: 75.0%
    Minibatch loss at step 1500: 0.6598564386367798
    Minibatch accuracy: 78.9%
    Validation accuracy: 78.6%
    Minibatch loss at step 2000: 0.24766433238983154
    Minibatch accuracy: 91.4%
    Validation accuracy: 81.0%
    Minibatch loss at step 2500: 0.6181786060333252
    Minibatch accuracy: 84.4%
    Validation accuracy: 82.5%
    Minibatch loss at step 3000: 0.9605385065078735
    Minibatch accuracy: 85.2%
    Validation accuracy: 83.9%
    Minibatch loss at step 3500: 0.6315320730209351
    Minibatch accuracy: 85.2%
    Validation accuracy: 84.4%
    Minibatch loss at step 4000: 0.812285840511322
    Minibatch accuracy: 82.8%
    Validation accuracy: 85.0%
    Minibatch loss at step 4500: 0.5949224233627319
    Minibatch accuracy: 80.5%
    Validation accuracy: 85.6%
    Minibatch loss at step 5000: 0.47554320096969604
    Minibatch accuracy: 89.1%
    Validation accuracy: 86.2%
    
    Test accuracy: 86.5%
    

Some important points to note:

  * In every iteration, a minibatch is selected by choosing a random offset value using **np.random.randint** method.
  * To feed the placeholders **tf_train_dataset** and **tf_train_label** , we create a **feed_dict** like this:
    
        feed_dict = {tf_train_dataset : batch_data, tf_train_labels : batch_labels}
    

  * A shortcut way of performing one step of computation is:
    
        _, l, predictions = session.run([optimizer, loss, train_prediction], feed_dict=feed_dict)
    

This node returns the new values of loss and predictions after performing
optimization step.

This brings us to the end of the implementation. Complete code can be found
here.

Finally, here are some points to ponder upon:

  * You can try to tweak with the parameters like learning rate, batch size, number of epochs, etc and achieve better results. You can also try a different optimizer like tf.train.AdamOptimizer.
  * Accuracy of above model can be improved by using a neural network with one or more hidden layers. We will discuss its implementation using TensorFlow in some upcoming articles.
  *  **Softmax Regression vs. k Binary Classifiers  
** One should be aware of the scenarios where softmax regression works and
where it doesn’t. In many cases, you may need to use k different binary
logistic classifiers for each of the k possible values of the class label.

Suppose you are working on a computer vision problem where you’re trying to
classify images into three different classes:

 **Case 1:** Suppose that your classes are indoor_scene, outdoor_urban_scene,
and outdoor_wilderness_scene.

 **Case 2:** Suppose your classes are indoor_scene, black_and_white_image, and
image_has_people.

In which case you would use **Softmax Regression** classifier and in which
case you would use 3 **Binary Logistic Regression** classifiers?

This will depend on whether the 3 classes are mutually exclusive.

In **case 1** , a scene can be either indoor_scene, outdoor_urban_scene or
outdoor_wilderness_scene. So, assuming that each training example is labeled
with exactly one of the 3 classes, we should build a softmax classifier with k
= 3.

However, in **case 2** , the classes are not mutually exclusive since a scene
can be both indoor and have people in it. So, in this case, it would be more
appropriate to build 3 binary logistic regression classifiers. This way, for
each new scene, your algorithm can separately decide whether it falls into
each of the 3 categories.

 **References:**

  * http://www.kdnuggets.com/2016/07/softmax-regression-related-logistic-regression.html
  * https://classroom.udacity.com/courses/ud730
  * http://ufldl.stanford.edu/wiki/index.php/Softmax_Regression

This article is contributed by **Nikhil Kumar**. If you like GeeksforGeeks and
would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

