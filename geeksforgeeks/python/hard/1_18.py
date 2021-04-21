Retrieve Image and File stored as a BLOB from MySQL Table using Python



 **Prerequisites:**MySQL server should be installed

In this post, we will be talking about how we can store files like images,
text files, and other file formats into a MySQL table from a python script.
Sometimes, just like other information, we need to store images and files into
our database and provide it the security equivalent to other data.

In MySQL, we can use BLOB datatype to store the files. A BLOB is a binary
large object that can hold a variable amount of data. We can represent the
files in binary format and then store them in our database. The four BLOB
types are TINYBLOB, BLOB, MEDIUMBLOB, and LONGBLOB. These differ only in the
maximum length of the values they can hold.

 **We will use mysql-connect to use MySQL drivers in our python script.
First** , **install the requirements:**

    
    
    python3 -m pip install mysql-connect-python

 **Next, create a database and a table as shown below:**

  

  

> CREATE DATABASE STUDENTDB;
>
> USE STUDENTDB;
>
> CREATE TABLE PROFILE ( ID BIGINT PRIMARY KEY, NAME VARCHAR(50) NOT NULL,
> PICTURE LONGBLOB NOT NULL );

 **We can see the database schema using:**

    
    
    DESC PROFILE;

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210215213726/Screenshotfrom20210215213553.png)

 **Now, let’s add some data into the database:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import the required modules

import mysql.connector

import base64

from PIL import Image

import io 

 

# For security reasons, never expose your password

password = open('password','r').readline()

 

# Create a connection

mydb = mysql.connector.connect(

 host="localhost",

 user="root",

 password=password,

 database="studentdb" # Name of the database

)

 

# Create a cursor object

cursor = mydb.cursor()

 

# Open a file in binary mode

file = open('image.png','rb').read()

 

# We must encode the file to get base64 string

file = base64.b64encode(file)

 

# Sample data to be inserted

args = ('100', 'Sample Name', file)

 

# Prepare a query

query = 'INSERT INTO PROFILE VALUES(%s, %s, %s)'

 

# Execute the query and commit the database.

cursor.execute(query,args)

mydb.commit()  
  
---  
  
 __

 __

Now moving back to our MySQL database, we can see the inserted row.

  

  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210215213725/Screenshotfrom20210215213624.png)

### Retrieve the file:

We can make an SQL query to retrieve the image. The returned data will be in
base64 format. So first we need to decode the data. We can transmit this data
to the user or utilize it in other ways. In this post, we will simply show the
image on the screen.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import the required modules

import mysql.connector

import base64

from PIL import Image

import io 

 

# For security reasons, never expose your password

password = open('password','r').readline()

 

# Create a connection

mydb = mysql.connector.connect(

 host="localhost",

 user="root",

 password=password,

 database="studentdb" # Name of the database

)

 

# Create a cursor object

cursor = mydb.cursor()

 

# Prepare the query

query = 'SELECT PICTURE FROM PROFILE WHERE ID=100'

 

# Execute the query to get the file

cursor.execute(query)

 

data = cursor.fetchall()

 

# The returned data will be a list of list

image = data[0][0]

 

# Decode the string

binary_data = base64.b64decode(image)

 

# Convert the bytes into a PIL image

image = Image.open(io.BytesIO(binary_data))

 

# Display the image

image.show()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210215214336/Screenshotfrom20210215214308.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

