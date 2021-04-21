Convert integer to string in Python



In Python an integer can be converted into a string using the built-in
**str()** function. The str() function takes in any python data type and
converts it into a string. But use of the **str()** is not the only way to do
so. This type of conversion can also be done using the **“%s”** keyword, the
**.format** **** function or using **f-string** function.  
Below is the list of possible ways to convert an integer to string in python:

 **1\. Using str() function**

> **Syntax:** str(integer_value)

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

num= 10

# check and print type of num variable

print(type(num))

# convert the num into string

converted_num = str(num)

# check and print type converted_num variable

print(type(converted_num))  
  
---  
  
 __

 __

 **2\. Using “%s” keyword**

  

  

>  **Syntax:** “%s” % integer

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

num= 10

# check and print type of num variable

print(type(num))

# convert the num into string and print

converted_num = "% s" % num

print(type(converted_num))  
  
---  
  
 __

 __

 **3\. Using .format() function**

>  **Syntax:** ‘{}’.format(integer)

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

num= 10

# check and print type of num variable

print(type(num))

# convert the num into string and print

converted_num = "{}".format(num)

print(type(converted_num))  
  
---  
  
 __

 __

 **4\. Using f-string**

>  **Syntax:** f'{integer}’

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

num= 10

# check and print type of num variable

print(type(num))

# convert the num into string

converted_num = f'{num}'

# print type of converted_num

print(type(converted_num))  
  
---  
  
 __

 __

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

