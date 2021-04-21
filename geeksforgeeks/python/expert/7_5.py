Reading CSV files in Python



A **CSV (Comma Separated Values)** file is a form of plain text document which
uses a particular format to organize tabular information. CSV file format is a
bounded text document that uses a comma to distinguish the values. Every row
in the document is a data log. Each log is composed of one or more fields,
divided by commas. It is the most popular file format for importing and
exporting spreadsheets and databases.

## Reading a CSV File

There are various ways to read a CSV file that uses either the csv module or
the pandas library.

  *  **csv Module:** The CSV module is one of the modules in Python which provides classes for reading and writing tabular information in CSV file format.
  *  **pandas Library:** The pandas library is one of the open-source Python libraries that provides high-performance, convenient data structures and data analysis tools and techniques for Python programming.

 **Reading a CSV File Format in Python:**

Consider the below CSV file named ‘Giants.CSV’:

![](https://media.geeksforgeeks.org/wp-
content/uploads/20191213022527/Giants.csv-File-Format-1024x324.png)

  

  

  *  **USing csv.reader():** At first, the CSV file is opened using the open() method in ‘r’ mode(specifies read mode while opening a file) which returns the file object then it is read by using the reader() method of CSV module that returns the reader object that iterates throughout the lines in the specified CSV document.

 **Note:** The ‘with‘ keyword is used along with the open() method as it
simplifies exception handling and automatically closes the CSV file.

 __

 __  
 __

 __

 __  
 __  
 __

import csv

 

# opening the CSV file

with open('Giants.csv', mode ='r')as file:

 

 # reading the CSV file

 csvFile = csv.reader(file)

 

 # displaying the contents of the CSV file

 for lines in csvFile:

 print(lines)  
  
---  
  
 __

 __

 **Output:**

    
        ['Organiztion', 'CEO', 'Established']
    ['Alphabet', 'Sundar Pichai', '02-Oct-15']
    ['Microsoft', 'Satya Nadella', '04-Apr-75']
    ['Aamzon', 'Jeff Bezos', '05-Jul-94']

In the above program reader() method is used to read the Giants.csv file which
maps the data into lists.

  *  **Using csv.DictReader() class:** It is similar to the previous method, the CSV file is first opened using the open() method then it is read by using the DictReader class of csv module which works like a regular reader but maps the information in the CSV file into a dictionary. The very first line of the file comprises of dictionary keys.

 __

 __  
 __

 __

 __  
 __  
 __

import csv

 

# opening the CSV file

with open('Giants.csv', mode ='r') as file: 

 

 # reading the CSV file

 csvFile = csv.DictReader(file)

 

 # displaying the contents of the CSV file

 for lines in csvFile:

 print(lines)  
  
---  
  
 __

 __

 **Output:**

> OrderedDict([(‘Organiztion’, ‘Alphabet’), (‘CEO’, ‘Sundar Pichai’),
> (‘Established’, ’02-Oct-15′)])  
> OrderedDict([(‘Organiztion’, ‘Microsoft’), (‘CEO’, ‘Satya Nadella’),
> (‘Established’, ’04-Apr-75′)])  
> OrderedDict([(‘Organiztion’, ‘Aamzon’), (‘CEO’, ‘Jeff Bezos’),
> (‘Established’, ’05-Jul-94′)])

  *  **Using pandas.read_csv() method:** It is very easy and simple to read a CSV file using pandas library functions. Here read_csv() method of pandas library is used to read data from CSV files.

 __

 __  
 __

 __

 __  
 __  
 __

import pandas

 

# reading the CSV file

csvFile = pandas.read_csv('Giants.csv')

 

# displaying the contents of the CSV file

print(csvFile)  
  
---  
  
 __

 __

 **Output:**

    
    
    Organiztion            CEO Established
    0    Alphabet  Sundar Pichai   02-Oct-15
    1   Microsoft  Satya Nadella   04-Apr-75
    2      Aamzon     Jeff Bezos   05-Jul-94
    

In the above program, the csv_read() method of pandas library reads the
Giants.csv file and maps its data into a 2D list.

 **Note:** To know more about pandas.csv_read() click here.

