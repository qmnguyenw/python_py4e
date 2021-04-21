Softmax Regression Using Keras



Prerequisites: Logistic Regression

 **Getting Started With Keras:**  
Deep learning is one of the major subfields of machine learning framework. It
is supported by various libraries such as Theano, TensorFlow, Caffe, Mxnet
etc., Keras is one of the most powerful and easy to use python library, which
is built on top of popular deep learning libraries like TensorFlow, Theano,
etc., for creating deep learning models.  
Keras offers a collection of datasets that can be used to train and test the
model. The **Fashion MNIST dataset** is a part of the available datasets
present in the **tf.keras** datasets API. This dataset contains _70_ thousand
images of fashion objects that spread across 10 categories such as shoe, bag,
T-shirts etc. which are scaled to _28 by 28_ Greyscale pixels.

 **Approach:**  
So, the approach would be to first load the _MNIST Objects Dataset_ and then
we will use the _Matplotlib_ to see examples so as to get a better idea about
the dataset. Then finally we will classify them using _Keras API_ by building
a Neural Network. Later we will test our trained model on the test set to
check the accuracy of our model.  
 **Implementation:**  
 **Code: Loading the Data**

 __

 __  
 __

 __

 __  
 __  
 __

mnist= tf.keras.datasets.fashion_mnist

(training_images, training_labels), (test_images, test_labels) =
mnist.load_data()  
  
---  
  
 __

 __

Calling load_data on this object will give us two sets of two lists, these
will be the training and testing values for the graphics that contain the
dataset items and their labels.

 **Code: Understanding The Data**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

import numpy as np

np.set_printoptions(linewidth = 200)

import matplotlib.pyplot as plt

plt.imshow(training_images[42])

 

# printing training labels and training images

print(training_labels[42])

print(training_images[42])  
  
---  
  
 __

 __

 **Output:**

    
    
    9
    [[  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0]
     [  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0]
     [  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0]
     [  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0]
     [  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0]
     [  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0  82 187  26   0   0   0   0   0   0   0   0   0]
     [  0   0   0   0   0   0   0   0   0   1   0   0   1   0   0 179 240 237 255 240 139  83  64  43  60  54   0   1]
     [  0   0   0   0   0   0   0   0   0   1   0   0   1   0  58 239 222 234 238 246 252 254 255 248 255 187   0   0]
     [  0   0   0   0   0   0   0   0   0   0   2   3   0   0 194 239 226 237 235 232 230 234 234 233 249 171   0   0]
     [  0   0   0   0   0   0   0   0   0   1   1   0   0  10 255 226 242 239 238 239 240 239 242 238 248 192   0   0]
     [  0   0   0   0   0   0   0   0   0   0   0   0   0 172 245 229 240 241 240 241 243 243 241 227 250 209   0   0]
     [  0   0   0   0   0   0   0   0   0   6   5   0  62 255 230 236 239 241 242 241 242 242 238 238 242 253   0   0]
     [  0   0   0   0   0   0   0   0   0   3   0   0 255 235 228 244 241 241 244 243 243 244 243 239 235 255  22   0]
     [  0   0   0   0   0   0   0   0   0   0   0 246 228 220 245 243 237 241 242 242 242 243 239 237 235 253 106   0]
     [  0   0   3   4   4   2   1   0   0  18 243 228 231 241 243 237 238 242 241 240 240 240 235 237 236 246 234   0]
     [  1   0   0   0   0   0   0   0  22 255 238 227 238 239 237 241 241 237 236 238 239 239 239 239 239 237 255   0]
     [  0   0   0   0   0  25  83 168 255 225 225 235 228 230 227 225 227 231 232 237 240 236 238 239 239 235 251  62]
     [  0 165 225 220 224 255 255 233 229 223 227 228 231 232 235 237 233 230 228 230 233 232 235 233 234 235 255  58]
     [ 52 251 221 226 227 225 225 225 226 226 225 227 231 229 232 239 245 250 251 252 254 254 252 254 252 235 255   0]
     [ 31 208 230 233 233 237 236 236 241 235 241 247 251 254 242 236 233 227 219 202 193 189 186 181 171 165 190  42]
     [ 77 199 172 188 199 202 218 219 220 229 234 222 213 209 207 210 203 184 152 171 165 162 162 167 168 157 192  78]
     [  0  45 101 140 159 174 182 186 185 188 195 197 188 175 133  70  19   0   0 209 231 218 222 224 227 217 229  93]
     [  0   0   0   0   0   0   2  24  37  45  32  18  11   0   0   0   0   0   0  72  51  53  37  34  29  31   5   0]
     [  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0]
     [  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0]
     [  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0]
     [  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0]
     [  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0]]
    

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200511172853/1406-4.png)

  
**Normalisation:**  
Notice that all of the values in the number are between 0 and 255. If we are
training a neural network, for various reasons it’s easier if we treat all
values as between 0 and 1, a process called ‘normalizing’…and fortunately in
Python it’s easy to normalize a list like this without looping. We can do it
like this:

 **Code:**

 __

 __  
 __

 __

 __  
 __  
 __

training_images= training_images / 255.0

test_images = test_images / 255.0  
  
---  
  
 __

 __

 **Code:** Implementing Keras Model

 __

 __  
 __

 __

 __  
 __  
 __

model= tf.keras.models.Sequential([tf.keras.layers.Flatten(), 

 tf.keras.layers.Dense(128, activation = tf.nn.relu), 

 tf.keras.layers.Dense(10, activation = tf.nn.softmax)])  
  
---  
  
 __

 __

  *  **Sequential:** That defines a SEQUENCE of layers in the neural network.
  *  **Flatten:** It justs takes the image and convert it to a 1 Dimensional set.
  *  **Dense:** Adds a layer of neurons.
  * Each layer of neurons need an **activation function** to tell them what to do. There’s lots of options, but just use these for now.
  *  **Relu:** Effectively means “If _X > 0_ return _X_ , else return 0″ — so what it does it it only passes values 0 or greater to the next layer in the network.
  *  **Softmax:** takes a set of values, and effectively picks the biggest one, so, for example, if the output of the last layer looks like _[0.1, 0.1, 0.05, 0.1, 9.5, 0.1, 0.05, 0.05, 0.05]_ , it saves you from fishing through it looking for the biggest value, and turns it into _[0, 0, 0, 0, 1, 0, 0, 0, 0]_. The goal is to save a lot of coding

 **Step 5: Compile The Model**  
The next thing to do, now the model is defined, is to actually build it. You
do this by compiling it with an optimizer and loss function as before and then
you train it by calling _model.fit_ asking it to fit your training data to
your training labels i.e. have it figure out the relationship between the
training data and its actual labels, so in future, if you have data that looks
like the training data, then it can make a prediction for what that data would
look like.  
 **Code:**

 __

 __  
 __

 __

 __  
 __  
 __

model.compile(optimizer = tf.optimizers.Adam(),

 loss = 'sparse_categorical_crossentropy',

 metrics =['accuracy'])

 

model.fit(training_images, training_labels, epochs = 5)  
  
---  
  
 __

 __

 **Output:**

    
    
    Instructions for updating:
    Colocations handled automatically by placer.
    Epoch 1/5
    60000/60000 [==============================] - 8s 130us/sample - loss: 0.4714 - acc: 0.8322
    Epoch 2/5
    60000/60000 [==============================] - 8s 137us/sample - loss: 0.3598 - acc: 0.8683
    Epoch 3/5
    60000/60000 [==============================] - 9s 142us/sample - loss: 0.3201 - acc: 0.8824
    Epoch 4/5
    60000/60000 [==============================] - 8s 131us/sample - loss: 0.2949 - acc: 0.8917
    Epoch 5/5
    60000/60000 [==============================] - 8s 140us/sample - loss: 0.2767 - acc: 0.9098
    

Once it’s done training we should see an accuracy value at the end of the
final epoch. It might look something like 0.9098. This tells us that your
neural network is about 91% accurate in classifying the training data. i.e. it
figured out a pattern match between the image and the labels that worked 91%
of the time. Not great, but not bad considering it was only trained for 5
epochs and done quite quickly.

 **Step 6: Model Evaluation**

But how would it work with unseen data? That’s why we have the test images. We
can call _model.evaluate_ , and pass in the two sets, and it will report back
the loss for each.  
 **  
Code:**

 __

 __  
 __

 __

 __  
 __  
 __

model.evaluate(test_images, test_labels)  
  
---  
  
 __

 __

 **Output:**

    
    
    10000/10000 [==============================] - 1s 60us/sample - loss: 0.2908 - acc: 0.8956
    

Finally, we have trained our model and got an accuracy of 90% on the unseen
dataset. That’s pretty good.

 **Advantages of Using KERAS:**  
We have seen that our calculations have just reduced to 7-8 lines rather than
a hundred lines of code. That’s awesome. Overall, this helps us save our time
and energy and also reduces the chances of error in our code.

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save

