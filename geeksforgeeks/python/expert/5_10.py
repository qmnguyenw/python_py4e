Deep Neural Network With L – Layers



This article aims to implement a deep neural network with an arbitrary number
of hidden layers each containing different numbers of neurons. We will be
implementing this neural net using a few helper functions and at last, we will
combine these functions to make the L-layer neural network model.

 **L – layer deep neural network structure** (for understanding)  

![L-layer model](https://media.geeksforgeeks.org/wp-
content/uploads/20200628162624/architecture-2.png)

L – layer neural network

The model’s structure is [LINEAR -> tanh](L-1 times) -> LINEAR -> SIGMOID.
i.e., it has L-1 layers using the hyperbolic tangent function as activation
function followed by the output layer with a sigmoid activation function.  
More about activation functions

 **Step by step implementation of the neural network:**

    
    
    
    
    
    
      * Initialize the parameters for the L layers
    
      * Implement the forward propagation module
    
      * Compute the loss at the final layer
    
      * Implement the backward propagation module
    
      * Finally, update the parameters
    
      * Train the model using existing training dataset
    
      * Use trained parameters to test model
    
    
    

**Naming conventions followed in the article to prevent confusion:**

  

  

  * Each layer in the network is represented by a set of two parameters **W** matrix (weight matrix) and **b** matrix (bias matrix). For layer, **i** these parameters are represented as **Wi** and **bi** respectively.
  * The linear output of layer, i is represented as **Zi** , and the output after activation is represented as **Ai**. The dimensions of Zi and Ai are the same.

 **Dimensions of the weights and bias matrices.**  
The input layer is of the size (x, m) where m is the number of images.Layer
number| Shape of W| Shape of b| Linear Output| Shape of Activation| Layer 1|
![\(n\[1\], x\)](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-df861c444f01499712c1fe5a4bbc2317_l3.png)| ![\(n\[1\],
1\)](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-a7a40ee268fae2640064c5448fd45e9e_l3.png)| ![Z\[1\] =
W\[1\]X + b\[1\]](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-2560c197b0ddeca0e44133fdac6073c0_l3.png)| ![\(n\[1\],
m\)](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-
fcb03fcf30ff2080b0424e6b6e947533_l3.png)| Layer 2| ![\(n\[2\],
n\[1\]\)](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-
bf405ca6c8c5d58eb33d709928fbe810_l3.png)| ![\(n\[2\],
1\)](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-e7f23d517a68480253eb63cc1d2e04da_l3.png)| ![Z\[2\] =
W\[2\]A\[1\] + b\[2\]](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-2e190cef5bd9a1780731dfb2a5917569_l3.png)| ![\(n\[2\],
m\)](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-258f5630592d904ab409390184841a06_l3.png)| :|
![:](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-5dbf10eddab54ecd3c76c51458b24b41_l3.png)|
![:](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-5dbf10eddab54ecd3c76c51458b24b41_l3.png)|
![:](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-5dbf10eddab54ecd3c76c51458b24b41_l3.png)|
![:](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-5dbf10eddab54ecd3c76c51458b24b41_l3.png)| Layer L – 1|
![\(n\[L - 1\], n\[L - 2\]\)](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-a0b19705cfe516d9a6cf8737667a14c0_l3.png)| ![\(n\[L - 1\],
1\)](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-44dfcab8546e1cb1457c17f7a5301764_l3.png)| ![Z\[L - 1\] =
W\[L - 1\]A\[L - 2\] + b\[L - 1\]](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-eeb68442575915981624f1b314d7a7a9_l3.png)|
![\(n\[L - 1\], m\)](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-23292380347c7b97b8b7b6918d290c2d_l3.png)| Layer L|
![\(n\[L\], n\[L - 1\]\)](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-8b7682a0465df70969d9252eeff65551_l3.png)| ![\(n\[L\],
1\)](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-f734815229d60e3f2aabec4ef79fcc7d_l3.png)| ![Z\[L\] =
W\[L\]A\[L - 1\] + b\[L\]](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-f1e5ab4ead9e2e29c3e5a2224fd397a9_l3.png)| ![\(n\[L\],
m\)](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-b3ae544628c75d78467423f47b9fce11_l3.png)  
---|---|---|---|---  
  
 **Code: Importing all the required python libraries.**

 __

 __  
 __

 __

 __  
 __  
 __

import time

import numpy as np

import h5py

import matplotlib.pyplot as plt

import scipy

from PIL import Image

from scipy import ndimage  
  
---  
  
 __

 __

 **Initialization:**

  * We will use random initialization for the weight matrices( to avoid identical output from all neurons in the same layer).
  * Zero initialization for the biases.
  * The number of neurons in each layer is stored in the layer_dims dictionary with keys as layer number.

 **Code:**

 __

 __  
 __

 __

 __  
 __  
 __

def initialize_parameters_deep(layer_dims):

 # 0th layer is the input layer with number

 # of columns stored in layer_dims.

 parameters = {}

 

 # number of layers in the network

 L = len(layer_dims) 

 

 for l in range(1, L):

 parameters['W' + str(l)] = np.random.randn(layer_dims[l], 

 layer_dims[l - 1])*0.01

 parameters['b' + str(l)] = np.zeros((layer_dims[l], 1))

 

 return parameters  
  
---  
  
 __

 __

 **Forward propagation module:**  
The Forward propagation module will be completed in three steps. We will
complete three functions in this order:

  * linear_forward (to compute linear output Z for any layer)
  * linear_activation_forward where activation will be either tanh or Sigmoid.
  * L_model_forward [LINEAR -> tanh](L-1 times) -> LINEAR -> SIGMOID (whole model)

The linear forward module (vectorized over all the examples) computes the
following equations:  
Zi = Wi * A(i – 1) + bi Ai = activation_func(Zi)

 **Code:**

 __

 __  
 __

 __

 __  
 __  
 __

def linear_forward(A_prev, W, b):

 

 # cache is stored to be used in backward propagation module

 Z = np.dot(W, A_prev) + b

 cache = (A, W, b)

 return Z, cache  
  
---  
  
 __

 __

 __

 __  
 __

 __

 __  
 __  
 __

def sigmoid(Z):

 

 A = 1/(1 + np.exp(-Z))

 return A, {'Z' : Z}

 

def tanh(Z):

 

 A = np.tanh(Z)

 return A, {'Z' : Z}

 

def linear_activation_forward(A_prev, W, b, activation):

 

 # cache is stored to be used in backward propagation module

 if activation == "sigmoid":

 Z, linear_cache = linear_forward(A_prev, W, b)

 A, activation_cache = sigmoid(Z)

 elif activation == "tanh":

 Z, linear_cache = linear_forward(A_prev, W, b)

 A, activation_cache = tanh(Z)

 cache = (linear_cache, activation_cache)

 

 return A, cache  
  
---  
  
 __

 __

 __

 __  
 __

 __

 __  
 __  
 __

def L_model_forward(X, parameters):

 """

 Arguments:

 X -- data, numpy array of shape (input size, number of examples)

 parameters -- output of initialize_parameters_deep()

 

 Returns:

 AL -- last post-activation value

 caches -- list of caches containing:

 every cache of linear_activation_forward() 

 (there are L-1 of them, indexed from 0 to L-1)

 """

 

 caches = []

 A = X

 

 # number of layers in the neural network

 L = len(parameters) // 2

 

 # Implement [LINEAR -> TANH]*(L-1). Add "cache" to the "caches" list.

 for l in range(1, L):

 A_prev = A 

 A, cache = linear_activation_forward(A_prev,

 parameters['W' + str(l)], 

 parameters['b' + str(l)], 'tanh')

 

 caches.append(cache)

 

 # Implement LINEAR -> SIGMOID. Add "cache" to the "caches" list.

 AL, cache = linear_activation_forward(A, parameters['W' +
str(L)],

 parameters['b' + str(L)], 'sigmoid')

 caches.append(cache)

 

 return AL, caches  
  
---  
  
 __

 __

  

  

![ \\\[   {\\Huge J =
\\frac{1}{m}\\sum_{i=1}^{\\m}y^{\(i\)}log\(a^{\[L\]\[i\]}\) + \(1 -
y^{\(i\)}\)log\(1 - a^{\[L\]\[i\]}\)} \\\] ](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-a0e4660d62f7724f8365c1837a79d946_l3.png)

