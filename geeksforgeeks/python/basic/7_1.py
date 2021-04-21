Extract text from PDF File using Python



All of you must be familiar with what PDFs are. In fact, they are one of the
most important and widely used digital media. PDF stands for **Portable
Document Format**. It uses **.pdf** extension. It is used to present and
exchange documents reliably, independent of software, hardware, or operating
system.

## Extracting Text from PDF File

Python package PyPDF can be used to achieve what we want (text extraction),
although it can do more than what we need. This package can also be used to
generate, decrypting and merging PDF files.

 **Note:** For more information, refer to Working with PDF files in Python

## Installation

To install this package type the below command in the terminal.

    
    
    pip install PyPDF2

 **Example:**

  

  

 **Input PDF:**

![extract-pdf-text-python](https://media.geeksforgeeks.org/wp-
content/uploads/20200427190331/extract-pdf-text-python.png)

 __

 __  
 __

 __

 __  
 __  
 __

# importing required modules

import PyPDF2 

 

# creating a pdf file object 

pdfFileObj = open('example.pdf', 'rb') 

 

# creating a pdf reader object 

pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

 

# printing number of pages in pdf file 

print(pdfReader.numPages) 

 

# creating a page object 

pageObj = pdfReader.getPage(0) 

 

# extracting text from page 

print(pageObj.extractText()) 

 

# closing the pdf file object 

pdfFileObj.close()   
  
---  
  
__

__

**Output:**

![extract-pdf-python](https://media.geeksforgeeks.org/wp-
content/uploads/20200427190427/extract-pdf-python.png)

Let us try to understand the above code in chunks:

  *     pdfFileObj = open('example.pdf', 'rb')

We opened the **example.pdf** in binary mode. and saved the file object as
**pdfFileObj**.

  *     pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

Here, we create an object of **PdfFileReader** class of PyPDF2 module and pass
the pdf file object & get a pdf reader object.

  *     print(pdfReader.numPages)

 **numPages** property gives the number of pages in the pdf file. For example,
in our case, it is 20 (see first line of output).

  *     pageObj = pdfReader.getPage(0)

Now, we create an object of **PageObject** class of PyPDF2 module. pdf reader
object has function **getPage()** which takes page number (starting form index
0) as argument and returns the page object.

  *     print(pageObj.extractText())

Page object has function **extractText()** to extract text from the pdf page.

  *     pdfFileObj.close()

At last, we close the pdf file object.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

