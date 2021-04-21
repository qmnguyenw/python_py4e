Modifying PDF file using Python



The following article depicts how a PDF can be modified using python’s
pylovepdf module. The Portable Document Format(PDF) is a file format developed
by Adobe in 1993 to present documents, including text formatting and images,
in a manner independent of application software, hardware, and operating
systems.

pylovepdf module can be downloaded using pip command:

    
    
    pip install pylovepdf

The iLovePDF API i.e ‘pylovepdf’ module is organized around REST. Their API
are predictable, resource-oriented URLs, and uses HTTP response codes to
indicate API errors. They use built-in HTTP features, like HTTP authentication
and HTTP verbs, which are understood by off-the-shelf HTTP clients. They
support cross-origin resource sharing, allowing you to interact securely with
their API from a client-side web application. With this API we can compress
the PDF files, also can add watermark, convert them to images and even split
them and vice -versa and lots of other stuff.

In order to do so first we need a public-key to use this module, for that
login on to https://developer.ilovepdf.com/ and after login the public key
will be visible in the ‘My Projects’ section. Below is the screenshot of the
public key

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201121000043/final-300x168.png)

  

  

Now since we have our public key, we can use this API for modifying any PDF
file using the steps given below:

  * 1\. Creating a ILovePdf object using the public key
  * 2\. Uploading the PDF file
  * 3\. Processing the PDF file
  * 4\. Downloading the PDF file

Implementation of this module is depicted properly using examples. Click here
for the PDF used in the examples provided in this article:  

**Example 1:** _Compressing the PDF file_

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importng the ilovepdf api

from pylovepdf.ilovepdf import ILovePdf

 

# public key

public_key = 'paste_your_public_key_here'

 

# creating a ILovePdf object

ilovepdf = ILovePdf(public_key, verify_ssl=True)

 

# assigning a new compress task

task = ilovepdf.new_task('compress')

 

# adding the pdf file to the task

task.add_file('my_pdf.pdf')

 

# setting the output folder directory

# if no folder exist it will create one

task.set_output_folder('output_folder')

 

# execute the task

task.execute()

 

# download the task

task.download()

 

# delete the task

task.delete_current_task()  
  
---  
  
 __

 __

Before processing:

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201124235145/final582.png)

 **Output :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201126143935/Screenshot268-300x138.png)

  

  

After Processing:

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201124235537/final583.png)

**Example 2:** _Splitting the PDF_

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# public key

from pylovepdf.ilovepdf import ILovePdf

public_key = 'paste your code here'

 

# importng the ilovepdf api

 

# creating a ILovePdf object

ilovepdf = ILovePdf(public_key, verify_ssl=True)

 

# assigning a new split task task

task = ilovepdf.new_task('split')

 

# adding the pdf file to the task

task.add_file('my_pdf.pdf')

 

 

# setting the output folder directory

# if no folder exist it will create one

task.set_output_folder('output_folder')

 

# execute the task

task.execute()

 

# download the task

task.download()

 

# delete the task

task.delete_current_task()  
  
---  
  
 __

 __

  

**Output :**  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201126142508/Screenshot267-300x141.png)

After processing:

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201121002840/final-300x168.png)

zip

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

