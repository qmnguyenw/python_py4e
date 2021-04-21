Reading an excel file using Python



Using xlrd module, one can retrieve information from a spreadsheet. For
example, reading, writing or modifying the data can be done in Python. Also,
the user might have to go through various sheets and retrieve data based on
some criteria or modify some rows and columns and do a lot of work.

 **xlrd** module is used to extract data from a spreadsheet.  
  
Command to install xlrd module :

    
    
    pip install xlrd
    
    

**Input File:**

![Sample excel file](https://media.geeksforgeeks.org/wp-content/uploads/excel-
file.png)

**Code #1:** Extract a specific cell

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Reading an excel file using Python

import xlrd

# Give the location of the file

loc = ("path of file")

# To open Workbook

wb = xlrd.open_workbook(loc)

sheet = wb.sheet_by_index(0)

# For row 0 and column 0

print(sheet.cell_value(0, 0))  
  
---  
  
 __

 __

Output :

    
    
    'NAME'
    
    

**Code #2:** Extract the number of rows

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Program to extract number

# of rows using Python

import xlrd

# Give the location of the file

loc = ("path of file")

wb = xlrd.open_workbook(loc)

sheet = wb.sheet_by_index(0)

sheet.cell_value(0, 0)

# Extracting number of rows

print(sheet.nrows)  
  
---  
  
 __

 __

Output :

    
    
    4
    
    

**Code #3:** Extract the number of columns

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Program to extract number of

# columns in Python

import xlrd

loc = ("path of file")

wb = xlrd.open_workbook(loc)

sheet = wb.sheet_by_index(0)

# For row 0 and column 0

sheet.cell_value(0, 0)

# Extracting number of columns

print(sheet.ncols)  
  
---  
  
 __

 __

Output :

    
    
    3
    
    

**Code #4 :** Extracting all columns name

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Program extracting all columns

# name in Python

import xlrd

loc = ("path of file")

wb = xlrd.open_workbook(loc)

sheet = wb.sheet_by_index(0)

# For row 0 and column 0

sheet.cell_value(0, 0)

for i in range(sheet.ncols):

 print(sheet.cell_value(0, i))  
  
---  
  
 __

 __

Output :

    
    
    NAME
    SEMESTER
    ROLL NO
    
    

**Code #5:** Extract the first column

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Program extracting first column

import xlrd

loc = ("path of file")

wb = xlrd.open_workbook(loc)

sheet = wb.sheet_by_index(0)

sheet.cell_value(0, 0)

for i in range(sheet.nrows):

 print(sheet.cell_value(i, 0))  
  
---  
  
 __

 __

Output :

    
    
    NAME
    ALEX
    CLAY
    JUSTIN
    
    

**Code #6:** Extract a particular row value

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Program to extract a particular row value

import xlrd

loc = ("path of file")

wb = xlrd.open_workbook(loc)

sheet = wb.sheet_by_index(0)

sheet.cell_value(0, 0)

print(sheet.row_values(1))  
  
---  
  
 __

 __

Output :

    
    
    ['ALEX', 4.0, 2011272.0]
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

