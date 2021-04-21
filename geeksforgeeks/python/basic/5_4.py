Importing Kaggle dataset into google colaboratory



While building a Deep Learning model, the first task is to import datasets
online and this task proves to be very hectic sometimes.  
We can easily import Kaggle datasets in just a few steps:  
 **Code: Importing CIFAR 10 dataset**

 __

 __  
 __

 __

 __  
 __  
 __

!pip install kaggle  
  
---  
  
 __

 __

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200517160552/geeks11.jpeg)

Now go to your Kaggle account and create new API token from my account
section, a kaggle.json file will be downloaded in your PC.  
 **Code:**

 __

 __  
 __

 __

 __  
 __  
 __

from google.colab import files

files.upload()  
  
---  
  
 __

 __

 **Code: Uploading the kaggle.json file**

 __

 __  
 __

 __

 __  
 __  
 __

!mkdir-p ~/.kaggle

!cp kaggle.json ~/.kaggle/

!chmod 600 ~/.kaggle/kaggle.json  
  
---  
  
 __

 __

Copy the URL of your dataset and paste it in another cell.  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200517161428/geeks21.jpeg)

  

  

 **Code: To unzip the uploaded dataset.**

 __

 __  
 __

 __

 __  
 __  
 __

from zipfile import Zipfile

file_name=("cifar10-preprocessed.zip")

with Zipfile(file_name,'r') as zip:

 zip.extractall()

 print("done")  
  
---  
  
 __

 __

 **Code:**

 __

 __  
 __

 __

 __  
 __  
 __

'./get_CIFAR-10.sh'

import tensorflow as tf

 

(x_train,y_train),(x_test,y_test) = tf.keras.cifar10.load_data()  
  
---  
  
 __

 __

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200517162306/geeks3.jpeg)

Now your training and test set is ready to be used.

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save

