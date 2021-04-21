How to convert PDF file to Excel file using Python?



In this article, we will see how to convert a PDF to Excel or CSV File Using
Python. It can be done with various methods, here are we are going to use some
methods.

 **Method 1: Using pdftables_api**

Here will use the **pdftables_api** Module for converting the PDF file into
any other format. It’s a simple web-based API, so can be called from any
programming language.

 **Installation:**

    
    
    pip install git+https://github.com/pdftables/python-pdftables-api.git

After Installation, you need an API KEY. Go to **PDFTables.com** **** and
signup, then visit the ******API Page** **** to see your API KEY.

  

  

For Converting PDF File Into excel File we will use **xml()** method.

 **Syntax:**

    
    
    xml(pdf_path, xml_path)

 **Below is the Implementation:**

 **PDF File Used:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210119124832/Screenshot263.png)

 **PDF FILE**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import Module

import pdftables_api

 

# API KEY VERIFICATION

conversion = pdftables_api.Client('API KEY')

 

# PDf to Excel 

# (Hello.pdf, Hello)

conversion.xlsx("pdf_file_path", "output_file_path")  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210119124831/Screenshot262.png)

 **EXCEL FILE**

 **Method 2: Using tabula-py**

Here will use the **tabula-py** Module for converting the PDF file into any
other format.

  

  

 **Installation:**

    
    
    pip install tabula-py

Before we start, first we need to install java and add a java installation
folder to the PATH variable.

  * Install java **click here**
  * Add java installation folder **(C:\Program Files (x86)\Java\jre1.8.0_251\bin)** to the environment path variable

 **Approach:**

  * Read **PDF** file using **read_pdf()** method.
  * Then we will convert the PDF files into an Excel file using the **to_excel()** method.

 **Syntax:**

    
    
    read_pdf(PDF File Path, pages = Number of pages, **agrs)

 **Below is the Implementation:**

 **PDF File Used:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210119124832/Screenshot263.png)

 **PDF FILE**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import Module

import tabula

 

# Read PDF File

# this contain a list

df = tabula.read_pdf("PDF File Path", pages = 1)[0]

 

# Convert into Excel File

df.to_excel('Excel File Path')  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210125095123/Screenshot268.png)

 **EXCEL FILE**

  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

