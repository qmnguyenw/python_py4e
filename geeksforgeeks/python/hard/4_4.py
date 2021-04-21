Dropout in Neural Networks



The concept of Neural Networks is inspired by the neurons in the human brain
and scientists wanted a machine to replicate the same process. This craved a
path to one of the most important topics in Artificial Intelligence. A Neural
Network (NN) is based on a collection of connected units or nodes called
artificial neurons, which loosely model the neurons in a biological brain.
Since such a network is created artificially in machines, we refer to that as
Artificial Neural Networks (ANN). This article assumes that you have a decent
knowledge of ANN. More about ANN can be found here.  
Now, let us go narrower into the details of **Dropout** in ANN.

 **Problem:**

When a fully-connected layer has a large number of neurons, co-adaption is
more likely to happen. Co-adaptation refers to when multiple neurons in a
layer extract the same, or very similar, hidden features from the input data.
This can happen when the connection weights for two different neurons are
nearly identical.  
  
![An example of co-adaptation between neurons A and B. Due to identical
weights, A and B will pass the same value into
C.](https://media.geeksforgeeks.org/wp-
content/uploads/20200502110455/4685869376077824.png)

This poses two different problems to our model:

  * Wastage of machine’s resources when computing the same output.
  * If many neurons are extracting the same features, it adds more significance to those features for our model. This leads to overfitting if the duplicate extracted features are specific to only the training set.

 **Solution to the problem:**

  

  

As the title suggests, we use dropout while training the NN to minimize co-
adaption.  
In dropout, we randomly shut down some fraction of a layer’s neurons at each
training step by zeroing out the neuron values. The fraction of neurons to be
zeroed out is known as the dropout rate, ![  r_{d}
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-a62f19e209060b7e70eb72918a1ed234_l3.png). The remaining
neurons have their values multiplied by ![ \\frac{1}{1 - r_d}
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-1f1216db13457128e1aad5319a511793_l3.png) so that the
overall sum of the neuron values remains the same.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200502110654/6183453068361728.png)

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200502110727/5971145083846656.png)

The two images represent dropout applied to a layer of 6 units, shown at
multiple training steps. The dropout rate is 1/3, and the remaining 4 neurons
at each training step have their value scaled by x1.5. Thereby, we are
choosing a random sample of neurons rather than training the whole network at
once. This ensures that the co-adaption is solved and they learn the hidden
features better.  
 **  
Dropout can be applied to a network using TensorFlow APIs as,**

 __

 __  
 __

 __

 __  
 __  
 __

tf.keras.layers.Dropout(

 rate

)

 

# rate: Float between 0 and 1. 

# The fraction of the input units to drop.  
  
---  
  
 __

 __

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save

