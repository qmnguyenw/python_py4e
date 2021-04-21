ML | Label Encoding of datasets in Python



In machine learning, we usually deal with datasets which contains multiple
labels in one or more than one columns. These labels can be in the form of
words or numbers. To make the data understandable or in human readable form,
the training data is often labeled in words.

 **Label Encoding** refers to converting the labels into numeric form so as to
convert it into the machine-readable form. Machine learning algorithms can
then decide in a better way on how those labels must be operated. It is an
important pre-processing step for the structured dataset in supervised
learning.

 **Example :**  
Suppose we have a column _Height_ in some dataset.  
![](https://media.geeksforgeeks.org/wp-content/uploads/Capture-190.png)  
After applying label encoding, the Height column is converted into:  
![](https://media.geeksforgeeks.org/wp-content/uploads/Capture-191.png)  
where 0 is the label for tall, 1 is the label for medium and 2 is label for
short height.

We apply _Label Encoding_ on iris dataset on the target column which is
Species. It contains three species _Iris-setosa, Iris-versicolor, Iris-
virginica_.

 __

 __  
 __

 __

 __  
 __  
 __

# Import libraries

import numpy as np

import pandas as pd

 

# Import dataset

df = pd.read_csv('../../data/Iris.csv')

 

df['species'].unique()  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    array(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'], dtype=object)

  
After applying Label Encoding –

 __

 __  
 __

 __

 __  
 __  
 __

# Import label encoder

from sklearn import preprocessing

 

# label_encoder object knows how to understand word labels.

label_encoder = preprocessing.LabelEncoder()

 

# Encode labels in column 'species'.

df['species']= label_encoder.fit_transform(df['species'])

 

df['species'].unique()  
  
---  
  
 __

 __

 **Output:**

    
    
    array([0, 1, 2], dtype=int64)
    

**Limitation of label Encoding**  
Label encoding convert the data in machine readable form, but it assigns a
unique number(starting from 0) to each class of data. This may lead to the
generation of priority issue in training of data sets. A label with high value
may be considered to have high priority than a label having lower value.

 **Example**

An attribute having output classes **mexico** , **paris** , **dubai**. On
Label Encoding this column, let **mexico** is replaced with _0_ , **paris** is
replaced with _1_ and **dubai** is replaced with 2.  
With this, it can be interpreted that **dubai** have high priority than
**mexico** and **paris** while training the model, But actually there is no
such priority relation between these cities here.

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save

