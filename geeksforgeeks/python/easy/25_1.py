Image Classifier using CNN



The article is about creating an Image classifier for identifying cat-vs-dogs
using TFLearn in Python. The problem is here hosted on kaggle.

 **Machine Learning** is now one of the most hot topics around the world.
Well, it can even be said as the new electricity in today’s world. But to be
precise what is Machine Learning, well it’s just one way of teaching the
machine by feeding the large amount of data. To know more about Machine
learning and its algorithms you can refer to some links that is provided in
the Reference sections of this article.

Today, we will create a Image Classifier of our own which can distinguish
whether a **given pic is of a dog or cat** or something else depending upon
your fed data. To achieve our goal, we will use one of the famous machine
learning algorithms out there which is used for Image Classification i.e.
Convolutional Neural Network(or CNN).  
So basically what is CNN – as we know its a machine learning algorithm for
machines to understand the features of the image with foresight and remember
the features to guess whether the name of the new image fed to the machine.
Since its not an article explaining the CNN so I’ll add some links in the end
if you guys are interested how CNN works and behaves.

So after going through all those links let us see how to create our very own
cat-vs-dog image classifier. For the dataset we will use the kaggle dataset of
cat-vs-dog:

  * train dataset- link
  * test dataset- link

Now after getting the data set, we need to preprocess the data a bit and
provide labels to each of the image given there during training the data set.
To do so we can see that name of each image of training data set is either
start with “cat” or “dog” so we will use that to our advantage then we use one
hot encoder for machine to understand the labels(cat[1, 0] or dog[0, 1]).

  

  

    
    
    def label_img(img):
        word_label = img.split('.')[-3]
       
     # DIY One hot encoder
        if word_label == 'cat': return [1, 0]
        elif word_label == 'dog': return [0, 1]
    

**Libraries Required :**

  *  **TFLearn** – Deep learning library featuring a higher-level API for TensorFlow used to create layers of our CNN
  *  **tqdm** – Instantly make your loops show a smart progress meter, just for simple designing sake
  *  **numpy** – To process the image matrices
  *  **open-cv** – To process the image like converting them to grayscale and etc.
  *  **os** – To access the file system to read the image from the train and test directory from our machines
  *  **random** – To shuffle the data to overcome the biasing
  *  **matplotlib** – To display the result of our predictive outcome.
  *  **tensorflow** – Just to use the tensorboard to compare the loss and adam curve our result data or obtained log.

TRAIN_DIR and TEST_DIR should be set according to the user convenience and
play with the basic hyperparameters like epoch, learning rate, etc to improve
the accuracy. I have converted the image to grayscale so that we will only
have to deal with 2-d matrix otherwise 3-d matrix is tough to directly apply
CNN to, especially not recommended for beginners. Below here is the code which
is heavily commented or otherwise you can find the code here in my GitHub
account from this link.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to create

# Image Classifier using CNN

 

# Importing the required libraries

import cv2

import os

import numpy as np

from random import shuffle

from tqdm import tqdm

 

'''Setting up the env'''

 

TRAIN_DIR = 'E:/dataset / Cats_vs_Dogs / train'

TEST_DIR = 'E:/dataset / Cats_vs_Dogs / test1'

IMG_SIZE = 50

LR = 1e-3

 

 

'''Setting up the model which will help with tensorflow models'''

MODEL_NAME = 'dogsvscats-{}-{}.model'.format(LR, '6conv-
basic')

 

'''Labelling the dataset'''

def label_img(img):

 word_label = img.split('.')[-3]

 # DIY One hot encoder

 if word_label == 'cat': return [1, 0]

 elif word_label == 'dog': return [0, 1]

 

'''Creating the training data'''

def create_train_data():

 # Creating an empty list where we should store the training data

 # after a little preprocessing of the data

 training_data = []

 

 # tqdm is only used for interactive loading

 # loading the training data

 for img in tqdm(os.listdir(TRAIN_DIR)):

 

 # labeling the images

 label = label_img(img)

 

 path = os.path.join(TRAIN_DIR, img)

 

 # loading the image from the path and then converting them into

 # greyscale for easier covnet prob

 img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

 

 # resizing the image for processing them in the covnet

 img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))

 

 # final step-forming the training data list with numpy array of the
images

 training_data.append([np.array(img), np.array(label)])

 

 # shuffling of the training data to preserve the random state of our data

 shuffle(training_data)

 

 # saving our trained data for further uses if required

 np.save('train_data.npy', training_data)

 return training_data

 

'''Processing the given test data'''

# Almost same as processing the training data but

# we dont have to label it.

def process_test_data():

 testing_data = []

 for img in tqdm(os.listdir(TEST_DIR)):

 path = os.path.join(TEST_DIR, img)

 img_num = img.split('.')[0]

 img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

 img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))

 testing_data.append([np.array(img), img_num])

 

 shuffle(testing_data)

 np.save('test_data.npy', testing_data)

 return testing_data

 

'''Running the training and the testing in the dataset for our model'''

train_data = create_train_data()

test_data = process_test_data()

 

# train_data = np.load('train_data.npy')

# test_data = np.load('test_data.npy')

'''Creating the neural network using tensorflow'''

# Importing the required libraries

import tflearn

from tflearn.layers.conv import conv_2d, max_pool_2d

from tflearn.layers.core import input_data, dropout, fully_connected

from tflearn.layers.estimator import regression

 

import tensorflow as tf

tf.reset_default_graph()

convnet = input_data(shape =[None, IMG_SIZE, IMG_SIZE, 1],
name ='input')

 

convnet = conv_2d(convnet, 32, 5, activation ='relu')

convnet = max_pool_2d(convnet, 5)

 

convnet = conv_2d(convnet, 64, 5, activation ='relu')

convnet = max_pool_2d(convnet, 5)

 

convnet = conv_2d(convnet, 128, 5, activation ='relu')

convnet = max_pool_2d(convnet, 5)

 

convnet = conv_2d(convnet, 64, 5, activation ='relu')

convnet = max_pool_2d(convnet, 5)

 

convnet = conv_2d(convnet, 32, 5, activation ='relu')

convnet = max_pool_2d(convnet, 5)

 

convnet = fully_connected(convnet, 1024, activation ='relu')

convnet = dropout(convnet, 0.8)

 

convnet = fully_connected(convnet, 2, activation ='softmax')

convnet = regression(convnet, optimizer ='adam', learning_rate =
LR,

 loss ='categorical_crossentropy', name ='targets')

 

model = tflearn.DNN(convnet, tensorboard_dir ='log')

 

# Splitting the testing data and training data

train = train_data[:-500]

test = train_data[-500:]

 

'''Setting up the features and lables'''

# X-Features & Y-Labels

 

X = np.array([i[0] for i in train]).reshape(-1,
IMG_SIZE, IMG_SIZE, 1)

Y = [i[1] for i in train]

test_x = np.array([i[0] for i in test]).reshape(-1,
IMG_SIZE, IMG_SIZE, 1)

test_y = [i[1] for i in test]

 

'''Fitting the data into our model'''

# epoch = 5 taken

model.fit({'input': X}, {'targets': Y}, n_epoch = 5, 

 validation_set =({'input': test_x}, {'targets': test_y}), 

 snapshot_step = 500, show_metric = True, run_id =
MODEL_NAME)

model.save(MODEL_NAME)

 

'''Testing the data'''

import matplotlib.pyplot as plt

# if you need to create the data:

# test_data = process_test_data()

# if you already have some saved:

test_data = np.load('test_data.npy')

 

fig = plt.figure()

 

for num, data in enumerate(test_data[:20]):

 # cat: [1, 0]

 # dog: [0, 1]

 

 img_num = data[1]

 img_data = data[0]

 

 y = fig.add_subplot(4, 5, num + 1)

 orig = img_data

 data = img_data.reshape(IMG_SIZE, IMG_SIZE, 1)

 

 # model_out = model.predict([data])[0]

 model_out = model.predict([data])[0]

 

 if np.argmax(model_out) == 1: str_label ='Dog'

 else: str_label ='Cat'

 

 y.imshow(orig, cmap ='gray')

 plt.title(str_label)

 y.axes.get_xaxis().set_visible(False)

 y.axes.get_yaxis().set_visible(False)

plt.show()  
  
---  
  
 __

 __

The output image will not be very clear since all the image is reduced to
50X50 for a machine to process fast though the tradeoff between speed and
loss.  
And to access the tensorboard use the following command in your cmd(Windows
user)

    
    
    tensorboard --logdir=foo:C:\Users\knapseck\Desktop\Dev\Cov_Net\log

Output:

https://media.geeksforgeeks.org/wp-content/uploads/2017-12-22-at-02-20-02.mp4

Reference Links for beginner to Machine Learning:

  * Machine Learning GeeksforGeeks
  * Siraj Raval – YouTube
  * Andrew Ng Machine Learning Course on Coursera
  * Machine Learning : A probabilistic Approach by Kevin Murphy
  * Reddit community for Machine Learning.

 **Reference Links for CNN :**

  * Jupyter Notebook – Conv_Net
  * Wikipedia – Convolutional Neural Networks
  * Stanford Course – cs231n

![Try out the all-new GeeksforGeeks
Premium!](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210304125233/GFG-Go-Premium.png)

My Personal Notes _arrow_drop_up_

Save

