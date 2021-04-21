ML | Training Image Classifier using Tensorflow Object Detection API



This article aims to learn how to build an object detector using Tensorflow’s
object detection API.

 **Requirement :**

  * Python Programming
  * Basics of Machine Learning
  * Basics of neural networks (Not Mandatory)
  * An enthusiasm to build a Cool project(Mandatory) :p

Even though if you don’t have the first three essentials, you’re welcome to
the adventure. Don’t worry about getting lost, I’ll guide you properly through
the journey!

 **What is object detection?**  
Object detection is the process of finding instances of real-world objects
such as faces, buildings, and bicycle in images or videos. Object detection
algorithms typically use extracted features and learning algorithms to
recognize instances of an object category. It is commonly used in applications
such as image retrieval, security, surveillance, and advanced driver
assistance systems (Self-driving cars). I personally have used object
detection to build a prototype of an Image-Based Search Engine.

 **What is Tensorflow’s Object Detection API?**  
Tensorflow is an open-source deep learning framework created by Google Brain.
Tensorflow’s Object Detection API is a powerful tool which enables everyone to
create their own powerful Image Classifiers. No coding or programming
knowledge is needed to use Tensorflow’s Object Detection API. But to
understand it’s working, knowing python programming and basics of machine
learning helps.

  

  

Before starting the Adventure let’s us make sure that, Python 3 is installed
in your system

For installing python and pip refer this site

First things first! Make sure that the below-given packages are installed in
your system. These are essential in your adventure.

    
    
           pip install protobuf
           pip install pillow
           pip install lxml
           pip install Cython
           pip install jupyter
           pip install matplotlib
           pip install pandas
           pip install opencv-python 
           pip install tensorflow
    

In order to start the adventure, we must get the vehicle and make the
necessary configurations to it.  
 **Tensorflow’s Object Detection API**

  1. We can get Tensorflow’s Object Detection API from github
  2. Visit the link provided: Download here

After downloading the models folder, extract it to the project’s directory. We
can find the **object_detection** directory inside

    
    
     models-master/research/ 

  * **Creating a PYTHONPATH variable:**  
A PYTHONPATH variable must be created that points to the \models,
\models\research, and \models\research\slim directories. Issue the command in
the following manner from any directory. In my case,

    
           set PYTHONPATH=F:\Programming\geeksforgeeks_project\models-master;F:\Programming\geeksforgeeks_project\models-master\research;F:\Programming\geeksforgeeks_project\models-master\research\slim

 **Compiling protobuf files and running setup.py:**  
The need to compile the Protobuf files, which are used by TensorFlow to
configure the model and the training parameters.  
For Compiling protoc files first we need to get protobuf compiler. You can
Download it here. Download **protoc-3.8-win64.zip** file for windows OS and
for other operating systems download the related zip file. Extract the bin
folder to research directory.  
Copy the below given code and save it as **use_protobuf.py** in your research
directory.

    
    
      import os 
      import sys 
      args = sys.argv 
      directory = args[1] 
      protoc_path = args[2] 
      for file in os.listdir(directory):
         if file.endswith(".proto"):
             os.system(protoc_path+" "+directory+"/"+file+" --python_out=.")

Go to research directory in command promt and use the command given below.

  

  

    
        python use_protobuf.py  .\object_detection\protos\ .\bin\protoc

This compiles all the protobuf files and creates a name_pb2.py file from every
name.proto file in the \object_detection\protos folder.  
Finally, run the following commands from the models-master\research directory:

    
    
      python setup.py build
      python setup.py install

With this the installation is finished and a package named **object-
detection** is installed.

  *  **Testing the API:**  
For testing the Object Detection api, go to object_detection directory and
enter the following command:

    
        jupyter notebook object_detection_tutorial.ipynb

This opens up the jupyter notebook in the browser.  
 _Note:_ If you have a line sys.path.append(“..”) in the first cell of the
notebook, remove that line.

Run all the cells of the notebook and check if you’re getting an output
similar to the below image:  
![Output of Jupyter notebook](https://media.geeksforgeeks.org/wp-
content/uploads/20190618225146/im7.png)  
![Output of Jupyter notebook](https://media.geeksforgeeks.org/wp-
content/uploads/20190618225153/im21.png)

With this we have successfully configured our vehicle.

 **Let’s begin our journey!**

To reach our destination we need to cross 6 Check points:

  1. Preparing Dataset
  2. Labeling the Dataset
  3. Generating Records for Training
  4. Configuring Training
  5. Training the Model
  6. Exporting Inference Graph

Plan what objects do you want to detect using the classifier.

  *  **Check Point 1: Preparing Dataset:**

In this adventure, I am going to build a classifier which detects shoes and
water bottles. Remember, the dataset is the most important thing in building a
classifier. This will be the basis of your classifier on which object
detection is done. Collect as many different and variety of images consisting
of the objects. Create a directory named images inside research directory.
Store 80% of the images into **train** directory and 20% of the images into
**test** directory inside the images directory. I have collected 50 images in
train directory and 10 images in the test directory. The more the number of
images the better is the precision of your classifier.

Images in train directory

![Images in Train directory](https://media.geeksforgeeks.org/wp-
content/uploads/20190619105501/12210.png)

Images in test directory

![Images in test directory](https://media.geeksforgeeks.org/wp-
content/uploads/20190619105925/12310.png)

  *  **Check Point 2: Labeling the Dataset:**  
To cross this checkpoint, we need to have a tool called as **labelimg**. You
can get it from: labelimg download

Open the labelimg application and start drawing the rect boxes on the image
where ever the object is present. And label them with an appropriate name as
shown in the figure:  
![How to label](https://media.geeksforgeeks.org/wp-
content/uploads/20190619120122/ll1.png)  
![how to label](https://media.geeksforgeeks.org/wp-
content/uploads/20190619120132/ll21.png)

Save each image after labeling which generates a xml file with the respective
image’s name as shown in the below image.  
![xml file generation](https://media.geeksforgeeks.org/wp-
content/uploads/20190619120504/ll3.png)

  *  **Check Point 3: Generating Records for Training:**  
To cross this check point, we need to create TFRecords that can be served as
input data for training of the object detector. In order to create the
TFRecords we will use two scripts from Dat Tran’s Racoon Detector. Namely the
**xml_to_csv.py** and **generate_tfrecord.py** files. Download them and save
them in object_detection folder.

replace the main() method of the xml_to_csv.py with the following code:

    
        def main():
        for folder in ['train', 'test']:
            image_path = os.path.join(os.getcwd(), ('images/' + folder))
            xml_df = xml_to_csv(image_path)
            xml_df.to_csv(('images/'+folder+'_labels.csv'), index=None)
            print('Successfully converted xml to csv.')

And also, add the below lines of code in xml_to_csv() method before the return
statement as shown in the below figure.

    
        names=[]
        for i in xml_df['filename']:
            names.append(i+'.jpg')
        xml_df['filename']=names

![Editing xml_to_csv.py](https://media.geeksforgeeks.org/wp-
content/uploads/20190619171136/w13.png)  
First let’s convert all the XML files to CSV files by running xml_to_csv.py
file with the following command in the object_detection directory:

    
        python xml_to_csv.py

This creates **test.csv** and **train.csv** files in the images folder.

Next, open the generate_tfrecord.py file in a text editor and edit the method
**class_text_to_int()** which can be found in the line 30 as shown in the
below image.

![Editing generate_tfrecord.py](https://media.geeksforgeeks.org/wp-
content/uploads/20190619141228/ll4.png)

Then, generate the TFRecord files by issuing these commands from the
\object_detection folder:

    
        python generate_tfrecord.py --csv_input=images\train_labels.csv --image_dir=images\train --output_path=train.record
    python generate_tfrecord.py --csv_input=images\test_labels.csv --image_dir=images\test --output_path=test.record

This creates test.record and train.record files in object_detection directory.

  *  **Check Point 4: Configuring Training:**

In order to cross this checkpoint, we first need to create a label map.

Create a new directory named **training** inside object_detection directory.

Use a text editor to create a new file and save it as **labelmap.pbtxt** in
the training directory. The label map tells the trainer what each object is by
defining a mapping of class names to class ID numbers.  
Now, add content in labelmap.pbtxt file in the following format to create a
labelmap for your classifier.

    
        item {
      id: 1
      name: 'shoe'
    }
    
    item {
      id: 2
      name: 'bottle'
    }

The label map ID numbers should be the same as what is defined in the
**generate_tfrecord.py** file.

Now let’s start to configure training!

We need a model i.e, algorithm to train our classifier. In this project we are
going to use **faster_rcnn_inception** model. Tensorflow’s object detection
API comes with a huge number of models. Navigate to
**object_detection\samples\configs**.  
In this location you can find a lot of config files to all the models provided
by the API. You can download the model using this link. Download the file
**faster_rcnn_inception_v2_coco**. After the downloading is finished, extract
the folder **faster_rcnn_inception_v2_coco_2018_01_28** to object_detection
directory. For understanding the working of the model refer this article.

As we are using **faster_rcnn_inception_v2_coco** model in this project, copy
the **faster_rcnn_inception_v2_coco.config** file from
object_detection\samples\configs and paste it in the training directory
created before.  
Use a text editor to open the config file and make the following changes to
the faster_rcnn_inception_v2_pets.config file.  
 _Note:_ The paths must be entered with single forward slashes (NOT
backslashes), or TensorFlow will give a file path error when trying to train
the model! Also, the paths must be in double quotation marks ( ” ), not single
quotation marks ( ‘ ).

    *  **Line 10:** Set the num_classes value to the number of objects your classifier is classifying. In my case, as I am classifying shoes and bottles it would be num_classes: 2.
    *  **In Line 107:** Give the absolute path of model.ckpt file to the **file_tuning_checkpoint** parameter. model.ckpt file is present in the location object_detection/faster_rcnn_inception_v2_coco_2018_01_28. In my case,

fine_tune_checkpoint: “F:/Programming/geeksforgeeks_project/models-
master/research/object_detection/faster_rcnn_inception_v2_coco_2018_01_28/model.ckpt”

    *  **train_input_reader section:** you can find this section in the line 120. In this section set the input_path parameter to your train.record file. In my case it is  
input_path: “F:/Programming/geeksforgeeks_project/models-
master/research/object_detection/train.record”.

Set the label_map_path parameter to the labelmap.pbtxt file. In my case it is:  
label_map_path: “F:/Programming/geeksforgeeks_project/models-
master/research/object_detection/training/labelmap.pbtxt”

    *  **eval config section:** You can find this section in the line 128. set num_examples parameter to the number of images present in the test directory. In my case,  
num_examples: 10

    *  **eval_input_reader section:** You can find this section in the line 134. Similar to train_input_reader section, set the paths to test.record and labelmap.pbtxt files. In my case,  
input_path: “F:/Programming/geeksforgeeks_project/models-
master/research/object_detection/train.record”

label_map_path: “F:/Programming/geeksforgeeks_project/models-
master/research/object_detection/training/labelmap.pbtxt”

With this all the configurations are done and we’re going to reach our last
checkpoint.

  *  **Check Point 5: Training the Model:**  
Finally the time has come to train our model. You can find a file named
**train.py** at the location object_detection/legacy/.

Copy the train.py file and paste it in the object_detection directory.  
Navigate to object_detection directory and run the following command to start
training your model!

    
        python train.py --logtostderr --train_dir=training/ --pipeline_config_path=training/faster_rcnn_inception_v2_coco.config
    

It takes around 1min to initialize the setup before the training begins. When
the training begins, it looks like:  
![Training ss](https://media.geeksforgeeks.org/wp-
content/uploads/20190619231145/tr11.png)

Tensorflow creates a checkpoint for every 5 minutes and stores it. You can see
that all the checkpoints are saved in the training directory.  
![Check Points](https://media.geeksforgeeks.org/wp-
content/uploads/20190619231320/ckp.png)  
You can view the progress of the training job by using TensorBoard. To do
this, open a new command prompt and navigate to the object_detection
directory, and issue the following command:

    
        tensorboard --logdir=training

Tensorboard looks like:  
![Tensorboard](https://media.geeksforgeeks.org/wp-
content/uploads/20190619231652/tb1.png)

Continue the training process until the loss is less than or equal to 0.1.

  *  **Check Point 6: Exporting Inference Graph:**  
This is the last checkpoint to be crossed to reach the destination.  
Now that we have a trained model we need to generate an inference graph, which
can be used to run the model. For doing so we need to first of find out the
highest saved step number. For this, we need to navigate to the training
directory and look for the model.ckpt file with the biggest index.

Then we can create the inference graph by typing the following command in the
command line.

    
        python export_inference_graph.py --input_type image_tensor --pipeline_config_path training/faster_rcnn_inception_v2_coco.config --trained_checkpoint_prefix training/model.ckpt-XXXX --output_directory inference_graph

XXXX should be filled by the highest checkpoint number.  
This creates a frozen_inference_graph.pb file in the
\object_detection\inference_graph folder. The .pb file contains the object
detection classifier.

With this, we have finished building our classifier. All that is left to
finish our adventure is using our model to detect objects.

create a python file in the object_detection directory with the below code:

 __

 __  
 __

 __

 __  
 __  
 __

# Write Python3 code here

import os

import cv2

import numpy as np

import tensorflow as tf

import sys

 

# This is needed since the notebook is stored in the object_detection
folder.

sys.path.append("..")

 

# Import utilites

from utils import label_map_util

from utils import visualization_utils as vis_util

 

# Name of the directory containing the object detection module we're using

MODEL_NAME = 'inference_graph' # The path to the directory where
frozen_inference_graph is stored.

IMAGE_NAME = '11man.jpg' # The path to the image in which the object
has to be detected.

 

# Grab path to current working directory

CWD_PATH = os.getcwd()

 

# Path to frozen detection graph .pb file, which contains the model that is
used

# for object detection.

PATH_TO_CKPT = os.path.join(CWD_PATH, MODEL_NAME,
'frozen_inference_graph.pb')

 

# Path to label map file

PATH_TO_LABELS = os.path.join(CWD_PATH, 'training',
'labelmap.pbtxt')

 

# Path to image

PATH_TO_IMAGE = os.path.join(CWD_PATH, IMAGE_NAME)

 

# Number of classes the object detector can identify

NUM_CLASSES = 2

 

# Load the label map.

# Label maps map indices to category names, so that when our convolution

# network predicts 5, we know that this corresponds to king.

# Here we use internal utility functions, but anything that returns a

# dictionary mapping integers to appropriate string labels would be fine

label_map = label_map_util.load_labelmap(PATH_TO_LABELS)

categories = label_map_util.convert_label_map_to_categories(

 label_map, max_num_classes = NUM_CLASSES, use_display_name =
True)

category_index = label_map_util.create_category_index(categories)

 

# Load the Tensorflow model into memory.

detection_graph = tf.Graph()

with detection_graph.as_default():

 od_graph_def = tf.GraphDef()

 with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:

 serialized_graph = fid.read()

 od_graph_def.ParseFromString(serialized_graph)

 tf.import_graph_def(od_graph_def, name ='')

 

 sess = tf.Session(graph = detection_graph)

 

# Define input and output tensors (i.e. data) for the object detection
classifier

 

# Input tensor is the image

image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

 

# Output tensors are the detection boxes, scores, and classes

# Each box represents a part of the image where a particular object was
detected

detection_boxes =
detection_graph.get_tensor_by_name('detection_boxes:0')

 

# Each score represents level of confidence for each of the objects.

# The score is shown on the result image, together with the class label.

detection_scores =
detection_graph.get_tensor_by_name('detection_scores:0')

detection_classes =
detection_graph.get_tensor_by_name('detection_classes:0')

 

# Number of objects detected

num_detections =
detection_graph.get_tensor_by_name('num_detections:0')

 

# Load image using OpenCV and

# expand image dimensions to have shape: [1, None, None, 3]

# i.e. a single-column array, where each item in the column has the pixel RGB
value

image = cv2.imread(PATH_TO_IMAGE)

image_expanded = np.expand_dims(image, axis = 0)

 

# Perform the actual detection by running the model with the image as input

(boxes, scores, classes, num) = sess.run(

 [detection_boxes, detection_scores, detection_classes, num_detections],

 feed_dict ={image_tensor: image_expanded})

 

# Draw the results of the detection (aka 'visualize the results')

 

vis_util.visualize_boxes_and_labels_on_image_array(

 image,

 np.squeeze(boxes),

 np.squeeze(classes).astype(np.int32),

 np.squeeze(scores),

 category_index,

 use_normalized_coordinates = True,

 line_thickness = 8,

 min_score_thresh = 0.60)

 

# All the results have been drawn on the image. Now display the image.

cv2.imshow('Object detector', image)

 

# Press any key to close the image

cv2.waitKey(0)

 

# Clean up

cv2.destroyAllWindows()  
  
---  
  
 __

 __

Give the path to the image in which object to be detected in the line 17.

Below are some of the results of my model.

![Result1](https://media.geeksforgeeks.org/wp-
content/uploads/20190620103209/res4.png)  
![Result 2](https://media.geeksforgeeks.org/wp-
content/uploads/20190620103221/res1.png)  
![Result 3](https://media.geeksforgeeks.org/wp-
content/uploads/20190620103228/res5.png)  
![Result 4](https://media.geeksforgeeks.org/wp-
content/uploads/20190620103237/res3.png)  
![Result 5](https://media.geeksforgeeks.org/wp-
content/uploads/20190620104928/10res.png)

So finally our model is ready. This model has also been used to build an
Image-based search engine, which searches using image inputs by detecting
objects in the image.

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save

