Split a text column into two columns in Pandas DataFrame



Let’s see how to split a text column into two columns in Pandas DataFrame.

 **Method #1 :** Using Series.str.split() functions.

Split _Name_ column into two different columns. By default splitting is done
on the basis of single space by str.split() function.

 __

 __  
 __

 __

 __  
 __  
 __

# import Pandas as pd

import pandas as pd

 

# create a new data frame

df = pd.DataFrame({'Name': ['John Larter', 'Robert Junior',
'Jonny Depp'],

 'Age':[32, 34, 36]})

 

print("Given Dataframe is :\n",df)

 

# bydefault splitting is done on the basis of single space.

print("\nSplitting 'Name' column into two different columns :\n",

 df.Name.str.split(expand=True))  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-content/uploads/split_col1.png)  
  
Split _Name_ column into “First” and “Last” column respectively and add it to
the existing Dataframe .

 __

 __  
 __

 __

 __  
 __  
 __

# import Pandas as pd

import pandas as pd

 

# create a new data frame

df = pd.DataFrame({'Name': ['John Larter', 'Robert Junior',
'Jonny Depp'],

 'Age':[32, 34, 36]})

 

print("Given Dataframe is :\n",df)

 

# Adding two new columns to the existing dataframe.

# bydefault splitting is done on the basis of single space.

df[['First','Last']] = df.Name.str.split(expand=True)

 

print("\n After adding two new columns : \n", df)  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/split_col2.png)

  

  

  
Use _underscore_ as delimiter to split the column into two columns.

 __

 __  
 __

 __

 __  
 __  
 __

# import Pandas as pd

import pandas as pd

 

# create a new data frame

df = pd.DataFrame({'Name': ['John_Larter', 'Robert_Junior',
'Jonny_Depp'],

 'Age':[32, 34, 36]})

 

print("Given Dataframe is :\n",df)

 

# Adding two new columns to the existing dataframe.

# splitting is done on the basis of underscore.

df[['First','Last']] =
df.Name.str.split("_",expand=True)

 

print("\n After adding two new columns : \n",df)  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-content/uploads/split_col3.png)  
  
Use str.split(), tolist() function together.

 __

 __  
 __

 __

 __  
 __  
 __

# import Pandas as pd

import pandas as pd

 

# create a new data frame

df = pd.DataFrame({'Name': ['John_Larter', 'Robert_Junior',
'Jonny_Depp'],

 'Age':[32, 34, 36]})

 

print("Given Dataframe is :\n",df)

 

print("\nSplitting Name column into two different columns :") 

print(pd.DataFrame(df.Name.str.split('_',1).tolist(),

 columns = ['first','Last']))  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-content/uploads/split_col4.png)  
  
**Method #2 :** Using apply() function.

Split _Name_ column into two different columns.

 __

 __  
 __

 __

 __  
 __  
 __

# import Pandas as pd

import pandas as pd

 

# create a new data frame

df = pd.DataFrame({'Name': ['John_Larter', 'Robert_Junior',
'Jonny_Depp'],

 'Age':[32, 34, 36]})

 

print("Given Dataframe is :\n",df)

 

print("\nSplitting Name column into two different columns :") 

print(df.Name.apply(lambda x:
pd.Series(str(x).split("_"))))  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-content/uploads/split_col5.png)

Split _Name_ column into two different columns named as “First” and “Last”
respectively and then add it to the existing Dataframe.

 __

 __  
 __

 __

 __  
 __  
 __

# import Pandas as pd

import pandas as pd

 

# create a new data frame

df = pd.DataFrame({'Name': ['John_Larter', 'Robert_Junior',
'Jonny_Depp'],

 'Age':[32, 34, 36]})

 

print("Given Dataframe is :\n",df)

 

print("\nSplitting Name column into two different columns :") 

 

# splitting 'Name' column into Two columns 

# i.e. 'First' and 'Last'respectively and 

# Adding these columns to the existing dataframe.

df[['First','Last']] = df.Name.apply(

 lambda x: pd.Series(str(x).split("_")))

 

print(df)  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-content/uploads/split_col6.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

