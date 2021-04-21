Python | Generate Personalized Data from given list of expressions



Given different lists of expressions, the task is to generate a random
combination of these expressions in a csv file for some purposes such as test
databases contrary to ordinal data simulator which generates datasets from
random numbers and standard names.

 **Examples:**

    
    
    **Input :lists of your own expressions** 
    Names   = ['David', 'Emilia', 'John', 'Karmen'], 
    Hobbies = ['Hiking', 'football', 'Gaming', 'Skydiving'],
    skills  = ['Communication', 'leadership', 'cooking']
     
    **Output : a csv file with a random combination of expressions**
    Names, Age, Hobbies, skills
    Emilia, 54, "['football', 'Hiking']", leadership
    David, 22, "['Skydiving', 'Gaming']", cooking
    Emilia, 59, "['football', 'Skydiving']", leadership
    Emilia, 45, "['Gaming', 'football']", leadership
    David, 62, "['Hiking', 'football']", cooking
    David, 56, "['football', 'Hiking']", leadership
    John, 17, "['Gaming', 'football']", cooking
    David, 28, "['Gaming', 'football']", leadership
    David, 28, "['Skydiving', 'football']", cooking
    John, 17, "['Gaming', 'Skydiving']", cooking
    John, 61, "['Hiking', 'football']", cooking
    John, 44, "['Hiking', 'Gaming']", leadership
    Emilia, 17, "['Hiking', 'Gaming']", Communication
    Karmen, 34, "['football', 'Skydiving']", leadership
    Emilia, 65, "['football', 'Hiking']", leadership
    

**Code :** Generating Personalised Data

 __

 __  
 __

 __

 __  
 __  
 __

# importing libraries

import csv

import random

 

# create a csv file named "abc" that contains our dataset

with open('abc.csv', 'w', newline ='') as f: 

 file = csv.writer(f)

 file.writerow(['Names', 'Age', 'Hobbies', 'skills'])

 

 # generate rows as much as wanted

 for i in range (1, 10) : 

 Names =['David', 'Emilia', 'John', 'Karmen']

 Hobbies =['Hiking', 'football', 'Gaming',
'Skydiving']

 skills =['Communication', 'leadership', 'cooking']

 file.writerow([random.choice(Names), random.randint(17, 65), 

 random.sample(Hobbies, 2), random.choice(skills)])  
  
---  
  
 __

 __

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

