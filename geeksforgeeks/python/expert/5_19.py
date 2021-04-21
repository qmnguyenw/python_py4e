Humanize Package in Python



 **Humanize** is a package in python which contains various humanization
utilities like turning a number into a human-readable size or throughput or
number. In this article, we will discuss how to install this package and what
are the different utilities present in this package.

 **Installation:** To install this package, we will use pip a command. Python
pip is the package manager for Python packages. pip comes pre-installed on 3.4
or older versions of Python, pip commands are used in the command prompt. The
following command is used to install the package:

> pip install humanize

 **Usage:** This package offers various utilities which can be used on the
numbers to make the numbers easily readable for the humans. The utilities of
the package are:

  1.  **File Size Utility:** This utility can convert large integers of file sizes to human-readable form. The default unit of the size it accepts is **bytes**. For example:

 __

 __  
 __

 __

 __  
 __  
 __

# Program to demonstrate the

# File Size Utility

import humanize

 

size = humanize.naturalsize(1024000)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    1.0 MB
    

  2. **Scientific Notation:** This utility is used to add scientific notation to the program. This utility also gives an option to add precision to the number. Precision here means the number of digits needed in the number. For example:

 __

 __  
 __

 __

 __  
 __  
 __

# Program to demonstrate the

# scientific notation utility

import humanize

 

# Scientific notation using 

# integer without precision

gfg = humanize.scientific(2000)

print('Without Precision: '+gfg)

 

# Scientific notation using 

# integer with precision

gfg = humanize.scientific(2**10, precision = 5)

print('With Precision: '+gfg)  
  
---  
  
 __

 __

 **Output:**

    
    
    Without Precision: 2.00 x 10³
    With Precision: 1.02400 x 10³
    

  3. **Floating Point to Fractions:** This utility is used to convert a floating-point to fractions. For example:

 __

 __  
 __

 __

 __  
 __  
 __

# Program to demonstrate the

# floating point to fraction 

# utility

import humanize

 

gfg = humanize.fractional(0.5269)

print(gfg)  
  
---  
  
 __

 __

 **Output:**

    
    
    333/632
    

  4. **Date & Time Utility:** Many a times, we encounter few scenarios where the date or time is returned in the form of numbers. This utility is used to convert the date into a human understandable format. For example:

 __

 __  
 __

 __

 __  
 __  
 __

# Program to demonstrate the

# date time utility

import humanize

import datetime as dt

 

# Converting the date represented

# as a number

gfg = humanize.naturaldate(dt.date(2020, 5, 3))

print(gfg)

 

# Converting seconds to a 

# better representation

gfg = humanize.naturaldelta(dt.timedelta(seconds = 900))

print(gfg)  
  
---  
  
 __

 __

 **Output:**

    
    
    May 03 2020
    15 minutes
    

  5. **Integer Utility:** This utility is used to make integer values more presentable. For Example:

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# the integer utility

import humanize

 

# Adding commas to integer values

gfg = humanize.intcomma(14523689)

print(gfg)

 

# Converts the integer to 

# long and short scales

gfg = humanize.intword(1562345640)

print(gfg)

 

# Converts numbers (0-9) to their 

# english format

gfg = humanize.apnumber(5)

print(gfg)  
  
---  
  
 __

 __

 **Output:**

    
    
    14, 523, 689
    1.6 billion
    five
    

**References:** https://pypi.org/project/humanize/

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

