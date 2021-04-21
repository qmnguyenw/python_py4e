Replace values in Pandas dataframe using regex



While working with large sets of data, it often contains text data and in many
cases, those texts are not pretty at all. The is often in very messier form
and we need to clean those data before we can do anything meaningful with that
text data. Mostly the text corpus is so large that we cannot manually list out
all the texts that we want to replace. So in those cases, we use regular
expressions to deal with such data having some pattern in it.

We have already discussed in previous article how to replace some known string
values in dataframe. In this post, we will use regular expressions to replace
strings which have some pattern to it.

 **Problem #1 :** You are given a dataframe which contains the details about
various events in different cities. For those cities which starts with the
keyword ‘New’ or ‘new’, change it to ‘New_’.

 **Solution :** We are going to use regular expression to detect such names
and then we will use Dataframe.replace() function to replace those names.

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas as pd

import pandas as pd

 

# Let's create a Dataframe

df = pd.DataFrame({'City':['New York', 'Parague', 'New
Delhi', 'Venice', 'new Orleans'],

 'Event':['Music', 'Poetry', 'Theatre', 'Comedy',
'Tech_Summit'],

 'Cost':[10000, 5000, 15000, 2000, 12000]})

 

# Let's create the index

index_ = [pd.Period('02-2018'), pd.Period('04-2018'),

 pd.Period('06-2018'), pd.Period('10-2018'),
pd.Period('12-2018')]

 

# Set the index

df.index = index_

 

# Let's print the dataframe

print(df)  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-content/uploads/1-1722.png)

  

  

Now we will write the regular expression to match the string and then we will
use Dataframe.replace() function to replace those names.

 __

 __  
 __

 __

 __  
 __  
 __

# replace the matching strings

df_updated = df.replace(to_replace ='[nN]ew', value = 'New_',
regex = True)

 

# Print the updated dataframe

print(df_updated)  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-content/uploads/1-1723.png)  
As we can see in the output, the old strings have been replaced with the new
ones successfully.  
  
**Problem #2 :** You are given a dataframe which contains the details about
various events in different cities. The names of certain cities contain some
additional details enclosed in a bracket. Search for such names and remove the
additional details.

 **Solution :** For this task, we will write our own customized function using
regular expression to identify and update the names of those cities.
Additionally, We will use Dataframe.apply() function to apply our customized
function on each values the column.

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas as pd

import pandas as pd

 

# Let's create a Dataframe

df = pd.DataFrame({'City':['New York (City)', 'Parague',
'New Delhi (Delhi)', 'Venice', 'new Orleans'],

 'Event':['Music', 'Poetry', 'Theatre', 'Comedy',
'Tech_Summit'],

 'Cost':[10000, 5000, 15000, 2000, 12000]})

 

 

# Let's create the index

index_ = [pd.Period('02-2018'), pd.Period('04-2018'),

 pd.Period('06-2018'), pd.Period('10-2018'),
pd.Period('12-2018')]

 

# Set the index

df.index = index_

 

# Let's print the dataframe

print(df)  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-content/uploads/1-1736.png)

Now we will write our own customized function to match the description in the
names of the cities.

 __

 __  
 __

 __

 __  
 __  
 __

# Importing re package for using regular expressions

import re

 

# Function to clean the names

def Clean_names(City_name):

 # Search for opening bracket in the name followed by

 # any characters repeated any number of times

 if re.search('\(.*', City_name):

 

 # Extract the position of beginning of pattern

 pos = re.search('\(.*', City_name).start()

 

 # return the cleaned name

 return City_name[:pos]

 

 else:

 # if clean up needed return the same name

 return City_name

 

# Updated the city columns

df['City'] = df['City'].apply(Clean_names)

 

# Print the updated dataframe

print(df)  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-content/uploads/1-1737.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

