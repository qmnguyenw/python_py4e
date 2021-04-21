json.load() in Python



The full-form of JSON is JavaScript Object Notation. It means that a script
(executable) file which is made of text in a programming language, is used to
store and transfer the data. Python supports JSON through a built-in package
called json. To use this feature, we import the json package in Python
script. The text in JSON is done through quoted-string which contains the
value in key-value mapping within { }. It is similar to the dictionary in
Python.

 **Note:** For more information, refer to Working With JSON Data in Python

## json.load()

json.load() takes a file object and returns the json object. A **JSON
object** contains data in the form of key/value pair. The keys are strings and
the values are the JSON types. Keys and values are separated by a colon. Each
entry (key/value pair) is separated by a comma.

 **Syntax :**

    
    
    json.load(file_object)

 **Argument :** It takes file object as a parameter.

  

  

 **Return :** It return json object.

 **Example:** Let’s suppose the JSON looks like this.

![pyhton-append-json1](https://media.geeksforgeeks.org/wp-
content/uploads/20191227135952/pyhton-append-json1.png)

We want to read the content of this file. Below is the implementation.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to read

# json file

 

 

import json

 

# Opening JSON file

f = open('data.json',)

 

# returns JSON object as 

# a dictionary

data = json.load(f)

 

# Iterating through the json

# list

for i in data['emp_details']:

 print(i)

 

# Closing file

f.close()  
  
---  
  
 __

 __

 **Output:**

![python-read-json-output1](https://media.geeksforgeeks.org/wp-
content/uploads/20191227140208/python-read-json-output1.png)

Here, we have used the open() function to read the JSON file. Then, the file
is parsed using json.load() method which gives us a dictionary named data.  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

