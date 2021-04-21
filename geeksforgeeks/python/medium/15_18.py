Keras.Conv2D Class



 **Keras Conv2D** is a 2D Convolution Layer, this layer creates a convolution
kernel that is wind with layers input which helps produce a tensor of outputs.

 **Kernel:** In image processing kernel is a convolution matrix or masks which
can be used for blurring, sharpening, embossing, edge detection, and more by
doing a convolution between a kernel and an image.

 **The Keras Conv2D class constructor has the following arguments:**

    
    
    keras.layers.Conv2D(filters, kernel_size, strides=(1, 1),
      padding='valid', data_format=None, dilation_rate=(1, 1),
      activation=None, use_bias=True, kernel_initializer='glorot_uniform',
      bias_initializer='zeros', kernel_regularizer=None,
      bias_regularizer=None, activity_regularizer=None,
      kernel_constraint=None, bias_constraint=None)

 **Now let us examine each of these parameters individually:**  
 **filters**

  * Mandatory Conv2D parameter is the numbers of filters that convolutional layers will learn from.
  * It is an integer value and also determines the number of output filters in the convolution.
    
         **model.add(Conv2D(32, (3, 3), padding="same", activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))**

  * Here we are learning a total of 32 filters and then we use Max Pooling to reduce the spatial dimensions of the output volume.
  * As far as choosing the appropriate value for no. of filters, it is always recommended to use powers of 2 as the values.

 **kernel_size**

  

  

  * This parameter determines the dimensions of the kernel. Common dimensions include 1×1, 3×3, 5×5, and 7×7 which can be passed as (1, 1), (3, 3), (5, 5), or (7, 7) tuples.
  * It is an integer or tuple/list of 2 integers, specifying the height and width of the 2D convolution window.
  * This parameter must be an odd integer.

    
    
     **model.add(Conv2D(32, (7, 7), activation="relu"))**

 **strides**

  * This parameter is an integer or tuple/list of 2 integers, specifying the “step” of the convolution along with the height and width of the input volume.
  * Its default value is always set to (1, 1) which means that the given Conv2D filter is applied to the current location of the input volume and the given filter takes a 1-pixel step to the right and again the filter is applied to the input volume and it is performed until we reach the far right border of the volume in which we are moving our filter.

    
    
     **model.add(Conv2D(128, (3, 3), strides=(1, 1), activation="relu"))
    model.add(Conv2D(128, (3, 3), strides=(2, 2), activation="relu"))**

 **padding**

  * The padding parameter of the Keras Conv2D class can take one of two values: ‘valid’ or ‘same’.
  * Setting the value to “valid” parameter means that the input volume is not zero-padded and the spatial dimensions are allowed to reduce via the natural application of convolution.

    
    
     **model.add(Conv2D(32, (3, 3), padding="valid"))**

You can instead preserve spatial dimensions of the volume such that the output
volume size matches the input volume size, by setting the value to the “same”.

    
    
     **model.add(Conv2D(32, (3, 3), padding="same"))**

 **data_format**

  * This parameter of the Conv2D class can be either set to “channels_last” or “channels_first” value.
  * The TensorFlow backend to Keras uses channels last ordering whereas the Theano backend uses channels first ordering.
  * Usually we are not going to touch this value as Keras as most of the times we will be using TensorFlow backend to Keras.
  * It defaults to the image_data_format value found in your Keras config file at ~/.keras/Keras.json.

 **dilation_rate**

  * The dilation_rate parameter of the Conv2D class is a 2-tuple of integers, which controls the dilation rate for dilated convolution.
  * The Dilated Convolution is the basic convolution applied to the input volume with defined gaps.
  * You may use this parameter when working with higher resolution images and fine-grained details are important to you or when you are constructing a network with fewer parameters.

 **activation**

  * The activation parameter to the Conv2D class is simply a convenience parameter which allows you to supply a string, which specifies the name of the activation function you want to apply after performing the convolution.

    
    
     **model.add(Conv2D(32, (3, 3), activation="relu"))**

OR

    
    
     **model.add(Conv2D(32, (3, 3)))
    model.add(Activation("relu"))**

  * If you don’t specify anything, no activation is applied and won’t have an impact on the performance of your Convolutional Neural Network.

 **use_bias**

  

  

  * This parameter of the Conv2D class is used to determine whether a bias vector will be added to the convolutional layer.
  * By default, its value is set as True.

 **kernel_initializer**

  * This parameter controls the initialization method which is used to initialize all the values in the Conv2D class before actually training the model.
  * It is the initializer for the kernel weights matrix.

 **bias_initializer**

  * Whereas the bias_initializer controls how the bias vector is actually initialized before the training starts.
  * It is the initializer for the bias vector.

 **kernel_regularizer, bias_regularizer and activity_regularizer**

  *  **kernel_regularizer** is the Regularizer function which is applied to the kernel weights matrix.
  *  **bias_regularizer** is the Regularizer function which is applied to the bias vector.
  *  **activity_regularizer** is the Regularizer function which is applied to the output of the layer(i.e activation).
  * Regularizations are techniques used to reduce the error by fitting a function appropriately on the given training set and avoid overfitting.
  * It controls the type and amount of regularization method applied to the Conv2D layer.
  * Using regularization is a must when working with large datasets and deep neural networks.
  * Using regularization helps us to reduce the effects of overfitting and also to increase the ability of our model to generalize.
  * There are two types of regularization: L1 and L2 regularization, both are used to reduce overfitting of our model.

    
    
     **from keras.regularizers import l2
    ...
    model.add(Conv2D(128, (3, 3), activation="relu"),
        kernel_regularizer=l2(0.0002))**

  * The value of regularization which you apply is the hyperparameter you will need to tune for your own dataset and its value usually ranges from 0.0001 to 0.001.
  * It is always recommended to leave the bias_regularizer alone as it has very less impact on reducing the overfitting.
  * It is also recommended to leave the activity_regularizer to its default value.

 **kernel_constraint and bias_constraint**

  * kernel_constraint is the Constraint function which is applied to the kernel matrix.
  * bias_constraint is the Constraint function which is applied to the bias vector.
  * A constraint is a condition of an optimization problem that the solution must satisfy.  
There are several types of constraints—primarily equality constraints,
inequality constraints, and integer constraints.

  * These parameters allow you to impose constraints on the Conv2D layers.
  * These parameters are usually left alone unless you have a specific reason to apply a constraint on the Con2D layers.

 **Here is a simple code example to show you the working of different
parameters of Conv2D class:**

 __

 __  
 __

 __

 __  
 __  
 __

# build the model

model = Sequential()

model.add(Conv2D(32, kernel_size =(5, 5), strides
=(1, 1),

 activation ='relu'))

model.add(MaxPooling2D(pool_size =(2, 2), strides =(2,
2)))

model.add(Conv2D(64, (5, 5), activation ='relu'))

model.add(MaxPooling2D(pool_size =(2, 2)))

model.add(Flatten())

model.add(Dense(1000, activation ='relu'))

model.add(Dense(num_classes, activation ='softmax'))

 

# training the model

model.compile(loss = keras.losses.categorical_crossentropy,

 optimizer = keras.optimizers.SGD(lr = 0.01),

 metrics =['accuracy'])

 

# fitting the model

model.fit(x_train, y_train,

 batch_size = batch_size,

 epochs = epochs,

 verbose = 1,

 validation_data =(x_test, y_test),

 callbacks =[history])

 

# evaluating and printing results

score = model.evaluate(x_test, y_test, verbose = 0)

print('Test loss:', score[0])

print('Test accuracy:', score[1])  
  
---  
  
 __

 __

 **Understanding the Code:**

  * When adding the Conv2D layers using **Sequential.model.add()** method, there are numerous parameters we can use which we have read about earlier in our blog.
  * The first parameter tells us about the number of filters used in our convolution operation.
  * Then the second parameter specifies the size of the convolutional filter in pixels. Filter size may be determined by the CNN architecture you are using – for example, VGGNet exclusively uses (3, 3) filters. If not, use a 5×5 or 7×7 filter to learn larger features and then quickly reduce to 3×3.
  * The Third parameter specifies how the convolutional filter should step along the x-axis and the y-axis of the source image. In most cases, it’s okay to leave the strides parameter with the default (1, 1). However, you may increase it to (2, 2) to reduce the size of the output volume.
  * The Fourth parameter is the activation parameter which specifies the name of the activation function you want to apply after performing convolution.

 **Similar Code using Functional API**

 __

 __  
 __

 __

 __  
 __  
 __

#build the model

inputs = Input(shape = ())

conv1 = Conv2D(32, kernel_size = (5,5), strides =
(1,1), activation = 'relu'))(inputs)

max1 = MaxPooling2D(pool_size=(2,2),
strides=(2,2)))(conv1)

conv2 = Conv2D(64, (5,5), activation = 'relu'))(max1)

max2 = MaxPooling2D(pool_size=(2,2)))(conv2)

flat = Flatten()(max2)

den1 = Dense(100, activation = 'relu'))(flat)

out1 = Dense(num_classes, activation ='softmax'))(den1)

 

model = Model(inputs = inputs, output =out1 )

 

 

# training the model 

model.compile(loss = keras.losses.categorical_crossentropy,

 optimizer = keras.optimizers.SGD(lr = 0.01),

 metrics =['accuracy'])

 

# fitting the model 

model.fit(x_train, y_train,

 batch_size = batch_size,

 epochs = epochs,

 verbose = 1,

 validation_data =(x_test, y_test),

 callbacks =[history])

 

# evaluating and printing results 

score = model.evaluate(x_test, y_test, verbose = 0)

print('Test loss:', score[0])

print('Test accuracy:', score[1])  
  
---  
  
 __

 __

## Summary:

  * Most of the time you will be using filters, kernel_size, strides, padding.
  * How to properly use Keras Conv2D class to create our own Convolution Neural Network and determine if we need to utilize a specific parameter to the Keras Conv2D class.

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save

