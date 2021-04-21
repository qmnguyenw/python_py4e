Python | Excel File Comparison



Given Two Excel Files, We want to compare the values of each column row-wise
after sorting the values and print the changed column name and row number and
values change.

    
    
    **Input :**
    Two Excel files
    
    **Output :**
    Column name : 'location' and Row Number : 0
    Column name : 'location' and Row Number : 3
    Column name : 'date' and Row Number     : 1
    
    

**Code : Python code for comparing two excel files**

 __

 __  
 __

 __

 __  
 __  
 __

# Write Python3 code here

# importing Pandas

 

import pandas as pd

 

#Reading two Excel Sheets

 

sheet1 = pd.read_excel(r'Book1.xlsx')

sheet2 = pd.read_excel(r'Book2.xlsx')

 

# Iterating the Columns Names of both Sheets

for i,j in zip(sheet1,sheet2):

 

 # Creating empty lists to append the columns values 

 a,b =[],[]

 

 # Iterating the columns values

 for m, n in zip(sheet1[i],sheet2[j]):

 

 # Appending values in lists

 a.append(m)

 b.append(n)

 

 # Sorting the lists

 a.sort()

 b.sort()

 

 # Iterating the list's values and comparing them

 for m, n in zip(range(len(a)), range(len(b))):

 if a[m] != b[n]:

 print('Column name : \'{}\' and Row Number : {}'.format(i,m))  
  
---  
  
 __

 __

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

