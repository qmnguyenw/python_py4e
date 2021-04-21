ML | Handle Missing Data with Simple Imputer



 **SimpleImputer** is a scikit-learn class which is helpful in handling the
missing data in the predictive model dataset. It replaces the NaN values with
a specified placeholder.  
It is implemented by the use of the **SimpleImputer()** method which takes the
following arguments :

>  **missing_values** : The missing_values placeholder which has to be
> imputed. By default is _NaN_  
>  **stategy** : The data which will replace the NaN values from the dataset.
> The strategy argument can take the values – ‘mean'(default), ‘median’,
> ‘most_frequent’ and ‘constant’.  
>  **fill_value** : The constant value to be given to the NaN data using the
> constant strategy.

 **Code: Python code illustrating the use of SimpleImputer class.**

 __

 __  
 __

 __

 __  
 __  
 __

import numpy as np

 

# Importing the SimpleImputer class

from sklearn.impute import SimpleImputer

 

# Imputer object using the mean strategy and 

# missing_values type for imputation

imputer = SimpleImputer(missing_values = np.nan, 

 strategy ='mean')

 

data = [[12, np.nan, 34], [10, 32, np.nan], 

 [np.nan, 11, 20]]

 

print("Original Data : \n", data)

# Fitting the data to the imputer object

imputer = imputer.fit(data)

 

# Imputing the data 

data = imputer.transform(data)

 

print("Imputed Data : \n", data)  
  
---  
  
 __

 __

 **Output**

    
    
    Original Data :   
    
    [[12, nan, 34]
    [10, 32, nan]
    [nan, 11, 20]]
      
    
    Imputed Data :   
    
    [[12, 21.5, 34]
    [10, 32, 27]
    [11, 11, 20]]
    

**Remember: The mean or median is taken along the column of the matrix**

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save

