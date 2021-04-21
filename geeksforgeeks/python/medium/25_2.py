Python Faker Library



Faker is a Python package that generates fake data for you.

Installation: Help Link  
Open Anaconda prompt command to install:

    
    
    conda install -c conda-forge faker 
    

**Import package**

    
    
     from faker import Faker

Faker has the ability to print/get a lot of different fake data, for instance,
it can print fake name, address, email, text, etc.

Important most commonly used faker commands

  

  

    
    
    fake.name()
    fake.address()
    fake.email()
    fake.text()
    fake.country()
    

__

__  
__

__

__  
__  
__

from faker import Faker

fake = Faker()

print (fake.email())

print(fake.country())

print(fake.name())

print(fake.text())

print(fake.latitude(), fake.longitude())

print(fake.url())  
  
---  
  
 __

 __

    
    
    OUTPUT:(Different every time)
    vwilson@hotmail.com
    Belgium
    Shane Hunter
    Commodi vel libero placeat quibusdam odio odio consequatur. Ducimus libero quae optio non quidem. Facilis quas impedit quo.
    26.5687745 -124.802165
    http://www.turner.com/

 **Application 1 : Create a json of 100 students with name students.json that
contains student name, address, location coordinates and student roll
number.**

 __

 __  
 __

 __

 __  
 __  
 __

from faker import Faker 

 

# To create a json file

import json 

 

# For student id 

from random import randint 

 

fake = Faker() 

 

def input_data(x): 

 

 # dictionary 

 student_data ={} 

 for i in range(0, x): 

 student_data[i]={} 

 student_data[i]['id']= randint(1, 100) 

 student_data[i]['name']= fake.name() 

 student_data[i]['address']= fake.address() 

 student_data[i]['latitude']= str(fake.latitude()) 

 student_data[i]['longitude']= str(fake.longitude()) 

 print(student_data) 

 

 # dictionary dumped as json in a json file 

 with open('students.json', 'w') as fp: 

 json.dump(student_data, fp) 

 

 

def main(): 

 

 # Enter number of students 

 # For the above task make this 100 

 number_of_students = 10

 input_data(number_of_students) 

main() 

# The folder or location where this python code 

# is save there a students.json will be created 

# having 10 students data.   
  
---  
  
__

__

    
    
    OUTPUT 
    {0: {'id': 20, 'name': 'Benjamin Washington', 'address': 'USCGC Garrison\nFPO AP 48025-9793', 'latitude': '-68.975800', 'longitude': '153.009590'}, 1: {'id': 2, 'name': 'Christopher Howell', 'address': '7778 Sarah Center Apt. 663\nLawrenceport, WY 78084', 'latitude': '-21.8141675', 'longitude': '-122.830387'}, 2: {'id': 67, 'name': 'Fernando Fuentes', 'address': '7756 Bradford Plain Suite 997\nEast Chelseaburgh, KY 75776', 'latitude': '-82.791227', 'longitude': '-42.964122'}, 3: {'id': 86, 'name': 'Patrick Torres', 'address': 'Unit 5217 Box 7477\nDPO AE 82354-0160', 'latitude': '34.949096', 'longitude': '121.715387'}, 4: {'id': 11, 'name': 'James Hines', 'address': '4567 Donald Grove\nWilliamhaven, MO 85891', 'latitude': '86.7208035', 'longitude': '-48.103935'}, 5: {'id': 33, 'name': 'James Miller', 'address': 'PSC 2613, Box 7165\nAPO AP 29256-6576', 'latitude': '-35.4630595', 'longitude': '-50.415667'}, 6: {'id': 76, 'name': 'Randall Fuller', 'address': '7731 Garcia Pike\nNew Eric, KS 20545', 'latitude': '12.198124', 'longitude': '126.720134'}, 7: {'id': 49, 'name': 'Ivan Franco', 'address': '801 Chambers Light\nWest Daniel, IA 17114-4374', 'latitude': '-58.2576055', 'longitude': '171.773233'}, 8: {'id': 75, 'name': 'Amy Smith', 'address': '995 Luna Stream Apt. 297\nThompsonchester, NY 82115', 'latitude': '80.4262245', 'longitude': '115.142004'}, 9: {'id': 38, 'name': 'Danielle Thomas', 'address': '7309 Chris Ferry Suite 674\nColebury, MA 39673-2967', 'latitude': '-73.340443', 'longitude': '-176.964241'}}

 **Application 2: Print 10 fake names and countries in Hindi language.**

 __

 __  
 __

 __

 __  
 __  
 __

from faker import Faker 

 

#'hi_IN' changed the language

fake = Faker('hi_IN') 

 

for i in range(0, 10): 

 print('Name->', fake.name(),

 'Country->', fake.country())   
  
---  
  
__

__

![](https://media.geeksforgeeks.org/wp-content/uploads/rough-2.png)

**Application 3: Create fake profile**

 __

 __  
 __

 __

 __  
 __  
 __

import faker from Faker

fake = Faker()

print(fake.profile())  
  
---  
  
 __

 __

    
    
    OUTPUT
    {'job': 'Town planner', 'company': 'Martinez-Clark', 'ssn': '559-93-0521', 'residence': '46820 Johnny Circles\nStokesside, IL 87065-2470', 'current_location': (Decimal('83.5271055'), Decimal('43.705455')), 'blood_group': 'A+', 'website': ['https://www.taylor.com/'], 'username': 'hsmith', 'name': 'Christopher Davis', 'sex': 'M', 'address': '335 Mcdaniel Fork Suite 589\nTeresabury, AZ 85283', 'mail': 'kenneth48@yahoo.com', 'birthdate': '1981-03-29'}

 **Application 4: Seeding the Generator getting particular fake data again.**  
Seeding gives use the same fake data result that was generated at first
instance at that seed number.  
Example

 __

 __  
 __

 __

 __  
 __  
 __

from faker import Faker

fake = Faker()

 

fake.seed(1)

print(fake.name())

print(fake.address())

print(fake.email())  
  
---  
  
 __

 __

    
    
    OUTPUT
    Ryan Gallagher
    7631 Johnson Village Suite 690
    Adamsbury, NC 50008
    bparks@johnson.info

NOTE: Even if I run the program, again and again, I would get the same result.
As soon as I remove that fake.seed(1) line, we see randomness in data
generation.

 **Application 5: Print data from the list you want.**

 __

 __  
 __

 __

 __  
 __  
 __

import faker from Faker 

fake = Faker() 

# Print random sentences 

print(fake.sentence()) 

 

# List has words that we want in our sentence 

word_list = ["GFG", "Geeksforgeeks",

 "shaurya", "says", "Gfg",

 "GEEKS"] 

 

# Let's print 5 sentences that

# have words from our word_list 

for i in range(0, 5): 

 

 # You need to use ext_word_list = listnameyoucreated 

 print(fake.sentence(ext_word_list = word_list))   
  
---  
  
__

__

    
    
    OUTPUT
    # This is the random sentence that is generated using
    # fake.sentence()
    Error architecto inventore aut.
    
    # These are the 5 sentence that contains words from 
    # word_list we provided
    Shaurya shaurya GEEKS Geeksforgeeks.
    Gfg shaurya Geeksforgeeks GFG Gfg GFG.
    Geeksforgeeks Gfg says Geeksforgeeks GEEKS Gfg Gfg GFG.
    Geeksforgeeks shaurya GFG Geeksforgeeks Gfg GEEKS.
    Gfg Geeksforgeeks says GFG GEEKS says.

 **Summary of what we learned from Faker**  
1\. Fake data generation like name, address, email, text, sentence, etc  
2\. Creating a JSON file of fake data.  
3\. Different language fake data printed.  
4\. Creating Profile  
5\. Seeding i.e printing particular fake data  
6\. Generating a sentence that contains the words we provided.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

