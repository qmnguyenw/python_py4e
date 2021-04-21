Difference of two columns in Pandas dataframe



Difference of two columns in pandas dataframe in Python is carried out by
using following methods :

 **Method #1 :** Using **” -”** operator.

 __

 __  
 __

 __

 __  
 __  
 __

import pandas as pd

 

# Create a DataFrame

df1 = { 'Name':['George','Andrea','micheal',

 'maggie','Ravi','Xien','Jalpa'],

 'score1':[62,47,55,74,32,77,86],

 'score2':[45,78,44,89,66,49,72]}

 

df1 = pd.DataFrame(df1,columns=
['Name','score1','score2'])

 

print("Given Dataframe :\n", df1)

 

# getting Difference

df1['Score_diff'] = df1['score1'] - df1['score2']

print("\nDifference of score1 and score2 :\n", df1)  
  
---  
  
 __

 __

 **Output:**

    
    
    Given Dataframe :
           Name  score1  score2
    0   George      62      45
    1   Andrea      47      78
    2  micheal      55      44
    3   maggie      74      89
    4     Ravi      32      66
    5     Xien      77      49
    6    Jalpa      86      72
    
    Difference of score1 and score2 :
           Name  score1  score2  Score_diff
    0   George      62      45          17
    1   Andrea      47      78         -31
    2  micheal      55      44          11
    3   maggie      74      89         -15
    4     Ravi      32      66         -34
    5     Xien      77      49          28
    6    Jalpa      86      72          14
    

  
**Method #2 :** Using **sub()** method of the Dataframe.

 __

 __  
 __

 __

 __  
 __  
 __

import pandas as pd

 

# Create a DataFrame

df1 = { 'Name':['George','Andrea','micheal',

 'maggie','Ravi','Xien','Jalpa'],

 'score1':[62,47,55,74,32,77,86],

 'score2':[45,78,44,89,66,49,72]}

 

df1 = pd.DataFrame(df1,columns=
['Name','score1','score2'])

 

print("Given Dataframe :\n", df1)

 

df1['Score_diff'] = df1['score1'].sub(df1['score2'], axis
= 0)

print("\nDifference of score1 and score2 :\n", df1)  
  
---  
  
 __

 __

 **Output:**

    
    
    Given Dataframe :
           Name  score1  score2
    0   George      62      45
    1   Andrea      47      78
    2  micheal      55      44
    3   maggie      74      89
    4     Ravi      32      66
    5     Xien      77      49
    6    Jalpa      86      72
    
    Difference of score1 and score2 :
           Name  score1  score2  Score_diff
    0   George      62      45          17
    1   Andrea      47      78         -31
    2  micheal      55      44          11
    3   maggie      74      89         -15
    4     Ravi      32      66         -34
    5     Xien      77      49          28
    6    Jalpa      86      72          14
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

