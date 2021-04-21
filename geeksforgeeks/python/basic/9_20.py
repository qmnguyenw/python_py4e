Convert JSON to CSV in Python



The full-form of **JSON is JavaScript Object Notation**. It means that a
script (executable) file which is made of text in a programming language, is
used to store and transfer the data. Python supports JSON through a built-in
package called json. To use this feature, we import the json package in
Python script. The text in JSON is done through quoted string which contains
the value in key-value mapping within { }. It is similar to the dictionary
in Python.

 **CSV (Comma Separated Values)** is a simple file format used to store
tabular data, such as a spreadsheet or database. CSV file stores tabular data
(numbers and text) in plain text. Each line of the file is a data record. Each
record consists of one or more fields, separated by commas. The use of the
comma as a field separator is the source of the name for this file format.

> Refer to the below articles to understand the basics of JSON and CSV.
>
>   * Working With JSON Data in Python
>   * Working with CSV file in Python.
>

#### Converting JSON to CSV

For a simple JSON data consisting of key and value pairs, keys will be headers
for CSV file and values the descriptive data.

 **Example:** Suppose the JSON file looks like this:

  

  

![python-json-to-csv](https://media.geeksforgeeks.org/wp-
content/uploads/20191216134100/python-json-to-csv.png)

We want to convert the above JSON to CSV file with key as headers.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to convert

# JSON file to CSV

 

 

import json

import csv

 

 

# Opening JSON file and loading the data

# into the variable data

with open('data.json') as json_file:

 data = json.load(json_file)

 

employee_data = data['emp_details']

 

# now we will open a file for writing

data_file = open('data_file.csv', 'w')

 

# create the csv writer object

csv_writer = csv.writer(data_file)

 

# Counter variable used for writing 

# headers to the CSV file

count = 0

 

for emp in employee_data:

 if count == 0:

 

 # Writing headers of CSV file

 header = emp.keys()

 csv_writer.writerow(header)

 count += 1

 

 # Writing data of CSV file

 csv_writer.writerow(emp.values())

 

data_file.close()  
  
---  
  
 __

 __

 **Output:**

![python-json-to-csv-output](https://media.geeksforgeeks.org/wp-
content/uploads/20191216134435/python-json-to-csv-output.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

