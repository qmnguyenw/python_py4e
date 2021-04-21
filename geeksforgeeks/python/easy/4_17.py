Commonly used file formats in Data Science



 **What is a File Format**  
File formats are designed to store specific types of information, such as
**CSV, XLSX** etc. The file format also tells the computer how to display or
process its content. Common file formats, such as **CSV, XLSX, ZIP, TXT** etc.

If you see your future as a data scientist so you must understand the
different types of file format. Because data science is all about the data and
it’s processing and if you don’t understand the file format so may be it’s
quite complicated for you. Thus, it is mandatory for you to be aware of
different file formats.

 **Different type of file formats:**

 **CSV:** the CSV is stand for Comma-separated values. as-well-as this name
CSV file is use comma to separated values. In CSV file each line is a data
record and Each record consists of one or more then one data fields, the field
is separated by commas.

 **Code: Python code to read csv file in pandas**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

import pandas as pd

df = pd.read_csv("file_path / file_name.csv")

print(df)  
  
---  
  
 __

 __

 **XLSX:** The XLSX file is Microsoft Excel Open XML Format Spreadsheet file.
This is used to store any type of data but it’s mainly used to store financial
data and to create mathematical models etc.

 **Code: Python code to read xlsx file in pandas**

 __

 __  
 __

 __

 __  
 __  
 __

import pandas as pd

df = pd.read_excel (r'file_path\\name.xlsx')

print (df)  
  
---  
  
 __

 __

 **Note:**

> install xlrd before reading excel file in python for avoid the error. You
> can install xlrd using following command.
>
> pip install xlrd

 **ZIP:** ZIP files are used an data containers, they store one or more then
one files in the compressed form. it widely used in internet After you
downloaded ZIP file, you need to unpack its contents in order to use it.

 **Code: Python code to read zip file in pandas**

 __

 __  
 __

 __

 __  
 __  
 __

import pandas as pd

df = pd.read_csv(' File_Path \\ File_Name .zip')

print(df)  
  
---  
  
 __

 __

 **TXT:** TXT files are useful for storing information in plain text with no
special formatting beyond basic fonts and font styles. It is recognized by any
text editing and other software programs.

  

  

 **Code: Python code to read txt file in pandas**

 __

 __  
 __

 __

 __  
 __  
 __

import pandas as pd

df = pd.read_csv('File_Path \\ File_Name .txt')

print(df)  
  
---  
  
 __

 __

 **JSON:** JSON is stand for JavaScript Object Notation. JSON is a standard
text-based format for representing structured data based on JavaScript object
syntax

 **Code: Python code to read json file in pandas**

 __

 __  
 __

 __

 __  
 __  
 __

import pandas as pd

df = pd.read_json('File_path \\ File_Name .json')

print(df)  
  
---  
  
 __

 __

 **HTML:** HTML is stand for stands for Hyper Text Markup Language is use fore
creating web pages. we can read html table in python pandas using read_html()
function.

 **Code: Python code to read html file in pandas**

 __

 __  
 __

 __

 __  
 __  
 __

import pandas as pd

df = pd.read_html('File_Path \\File_Name.html')

print(df)  
  
---  
  
 __

 __

 **Note:**

> You need to install a package named “lxml & html5lib” which can handle the
> file with ‘.html’ extension.
>
> pip install html5lib  
> pip install lxml

 **PDF:** pdf stands for Portable Document Format (PDF) this file format is
use when we need to save files that cannot be modified but still need to be
easily available.

 **Code: Python code to read pdf in pandas**

 __

 __  
 __

 __

 __  
 __  
 __

pip install tabula-py

pip install pandas

df = tabula.read_pdf(file_path \\ file_name .pdf)

print(df)  
  
---  
  
 __

 __

 **Note:**

> You need to install a package named “tabula-py” which can handle the file
> with ‘.pdf’ extension.  
> pip install tabula-py

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

