Mean Encoding – Machine Learning



During Feature Engineering the task of converting categorical features into
numerical is called Encoding.  
There are various ways to handle categorical features like **OneHotEncoding**
and **LabelEncoding** , **FrequencyEncoding** or replacing by categorical
features by their count. In similar way we can uses **MeanEncoding**.

Created a DataFrame having two features named _subjects_ and _Target_ and we
can see that here one of the features (SubjectName) is Categorical, so we have
converted it into the numerical feature by applying Mean Encoding.  
 **Code:**

 __

 __  
 __

 __

 __  
 __  
 __

# importing libraries

import pandas as pd

 

# creating dataset

data={'SubjectName':['s1','s2','s3','s1','s4','s3','s2','s1','s2','s4','s1'],


'Target':[1,0,1,1,1,0,0,1,1,1,0]}

 

df = pd.DataFrame(data)

 

print(df)  
  
---  
  
 __

 __

 **Output:**

    
    
         SubjectName  Target
    0    s1    1
    1    s2    0
    2    s3    1
    3    s1    1
    4    s4    1
    5    s3    0
    6    s2    0
    7    s1    1
    8    s2    1
    9    s4    1
    10    s1    0
    

**Code : Counting every datapoints in SubjectName**

 __

 __  
 __

 __

 __  
 __  
 __

df.groupby(['SubjectName'])['Target'].count()  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    subjectName
     s1         4
     s2         3
     s3         2
     s4         2
    Name: Target, dtype: int64
    

**Code: groupby data with SubjectName with their mean according to their
positive target value**

 __

 __  
 __

 __

 __  
 __  
 __

df.groupby(['SubjectName'])['Target'].mean()  
  
---  
  
 __

 __

 **Output:**

    
    
    subjectName
    s1         0.750000
    s2         0.333333
    s3         0.500000
    s4         1.000000
    Name: Target, dtype: float64
    

The output shows the mean mapped with data point in SubjectName with their
positive target value (1-positive and 0-Negative).

 **Code : Finally assigning the mean value and map with _df[‘SubjectName’]_**

 __

 __  
 __

 __

 __  
 __  
 __

Mean_encoded_subject=
df.groupby(['SubjectName'])['Target'].mean().to_dict()

 

df['SubjectName'] =
df['SubjectName'].map(Mean_encoded_subject)

 

print(df)  
  
---  
  
 __

 __

 **Output : Mean Encoded Data**

    
    
        SubjectName    Target
    0    0.750000    1
    1    0.333333    0
    2    0.500000    1
    3    0.750000    1
    4    1.000000    1
    5    0.500000    0
    6    0.333333    0
    7    0.750000    1
    8    0.333333    1
    9    1.000000    1
    10    0.750000    0
    

**Pros of MeanEncoding:**

  * Capture information within the label, therefore rendering more predictive features
  * Creates a monotonic relationship between the variable and the target

 **Cons of MeanEncodig:**

  * It may cause over-fitting in the model.

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save

