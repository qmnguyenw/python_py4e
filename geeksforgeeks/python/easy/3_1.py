How to append a new row to an existing csv file?



For appending a new row to an existing CSV file we have many ways to do that.
Here we will discuss 2 ways to perform this task effectively. So, we have 2
ways first is ‘Append a list as a new row to the existing CSV file’ and the
second way is ‘Append a dictionary as a new row to the existing CSV file’.

First, let’s have a look at our existing CSV file contents. Suppose we have
CSV file event.csv which has the below contents.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201121104351/csv1-300x114.JPG)

CSV file before append

For writing a CSV file, the CSV module provides two different classes writer
and Dictwriter.

 **Append a list as a new row to the** **existing CSV file**

let’s see how to use writer class to append a list as a new row into an
existing CSV file. There are several steps to take that.

  

  

  * Import writer class from csv module
  * Open your existing CSV file in append mode  
Create a file object for this file.

  * Pass this file object to csv.writer() and get a writer object.
  * Pass the list as an argument into the writerow() function of the writer object.  
(It will add a list as a new row into the CSV file).

  * Close the file object

Let’s take one List that we want to add as a new row.

    
    
    List=[6,'William',5532,1,'UAE']
    

Now apply the above steps to the program.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import writer class from csv module

from csv import writer

 

# List 

List=[6,'William',5532,1,'UAE']

 

# Open our existing CSV file in append mode

# Create a file object for this file

with open('event.csv', 'a') as f_object:

 

 # Pass this file object to csv.writer()

 # and get a writer object

 writer_object = writer(f_object)

 

 # Pass the list as an argument into

 # the writerow()

 writer_object.writerow(List)

 

 #Close the file object

 f_object.close()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201121143452/csv2-300x129.JPG)

CSV file After appending List

When you are executing this program Ensure that your CSV file must be closed
otherwise this program will give you a permission error.

###  **Append a dictionary as a new row to the existing CSV file**

let’s see how to use DictWriter class to append a dictionary as a new row into
an existing CSV file. There are several steps to do that.

  * Import DictWriter class from CSV module.
  * Open your CSV file in append mode  
Create a file object for this file.

  * Pass the file object and a list of column names to DictWriter()  
You will get a object of DictWriter.

  * Pass the dictionary as an argument to the Writerow() function of DictWriter  
(it will add a new row to CSV file).

  * Close the file object

Let’s take one Dictionary that we want to add as a new row.

    
    
    dict={'ID':6,'NAME':'William','RANK':5532,'ARTICLE':1,'COUNTRY':'UAE'}
    

Now apply the above steps to the program.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import DictWriter class from CSV module

from csv import DictWriter

 

# list of column names 

field_names = ['ID','NAME','RANK',

 'ARTICLE','COUNTRY']

 

# Dictionary

dict={'ID':6,'NAME':'William','RANK':5532,

 'ARTICLE':1,'COUNTRY':'UAE'}

 

# Open your CSV file in append mode

# Create a file object for this file

with open('event.csv', 'a') as f_object:

 

 # Pass the file object and a list 

 # of column names to DictWriter()

 # You will get a object of DictWriter

 dictwriter_object = DictWriter(f_object, fieldnames=field_names)

 

 #Pass the dictionary as an argument to the Writerow()

 dictwriter_object.writerow(dict)

 

 #Close the file object

 f_object.close()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201121143452/csv2-300x129.JPG)

CSV file after Appending Dictionary

When you are executing this program ensures that your CSV file must be closed
otherwise this program will give you a permission error.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

