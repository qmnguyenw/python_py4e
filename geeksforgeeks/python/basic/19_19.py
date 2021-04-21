time.sleep() in Python



 **sleep()** is defined in time() module of python 3. Sometimes, there is a
need to hault the flow of the program so that several other executions can
take place or simply due to the utility required. sleep() can come handy in
such a situation which provides an accurate and flexible way to halt the flow
of code for any period of time. This function discusses the insight of this
function.  

> Syntax : **sleep(sec)**  
>  **Parameters :**  
> **sec :** Number of seconds for which the code is required to be stopped.  
>  **Returns :** **VOID.**  
>

  
**Code #1 :** Demonstrating sleep()  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# working of sleep()

import time

# printing the start time

print("The time of code execution begin is : ", end ="")

print(time.ctime())

# using sleep() to hault the code execution

time.sleep(6)

# printing the end time

print("The time of code execution end is : ", end ="")

print(time.ctime())  
  
---  
  
 __

 __

  

  

 **Output:**  

    
    
    The time of code execution begin is : Mon Apr  9 20:57:10 2018
    The time of code execution end is : Mon Apr  9 20:57:16 2018
    
    
    

**Application :**  
There are many applications that sleep() is used for. Be it execution of the
background thread which is repeated at regular interval, this can be
implemented with the help of sleep(). Another popular application is using
sleep() to print the words letter by letter for good user interface. The
latter is represented from this code below.  
  
**Code #2 :** Demonstrating application of sleep()  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# application of sleep()

import time

# initializing string

strn = "GeeksforGeeks"

# printing geeksforgeeks after delay

# of each character

for i in range(0, len(strn)):

 print(strn[i], end ="")

 time.sleep(2)  
  
---  
  
 __

 __

 **Output:**

    
    
    GeeksForGeeks
    
    
     **Note :** Visible effect of sleep() can be seen in the local editor.

 **Code #3:** Creating Time Delay in **List**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing time package

import time

# creating a time delay of 5 seconds

time.sleep(5)

# creating and Initilizing a list

myList = ['Jai', 'Shree', 'RAM', 5, 'August',
2020]

# the list will be displayed after the delay of 5 seconds

print(myList)  
  
---  
  
 __

 __

 **Output:**

After the delay of 5 seconds, we will get the output as:

    
    
    ['Jai', 'Shree', 'RAM', 5, 'August', 2020]
    

**Code #4:** Creating Time Delay in **Tuple**

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing time package

import time

# creating a time delay of 4 seconds

time.sleep(4)

# creating and Initilizing a tuple

mytuple = ('Anil Kumbl', 'Sachin Tendulkar', 'Sunil
Gavaskar', 'Rahul Dravid', 'Mahendra Singh Dhoni',

 'Dennis Lillee', 'Muttiah Muralitharan', 'Shane Warne')

# the tuple will be displayed after the delay of 4 seconds

print(mytuple)  
  
---  
  
 __

 __

 **Output:**

After the delay of 4 seconds, we will get the output as:

    
    
    ('Anil Kumbl', 'Sachin Tendulkar', 'Sunil Gavaskar', 'Rahul Dravid',
    'Mahendra Singh Dhoni', 'Dennis Lillee', 'Muttiah Muralitharan', 'Shane Warne')
    

**Code #5:** Creating **Multiple** Time Delays

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing time package

import time

# creating and Initilizing a list

Languages = ['Java', 'C++', 'Python', 'Javascript',
'C#', 'C', 'Kotlin']

# creating a time delay of 5 seconds

time.sleep(5)

# the list will be displayed after the delay of 5 seconds

print(Languages)

for lan in Languages:

 

 # creating a time delay of 13 seconds

 time.sleep(13)

 

 # After every 13 seconds an item of list will be displayed

 print(lan)  
  
---  
  
 __

 __

 **Output:**

After the delay of 5 seconds, the list will be displayed as:

    
    
    ['Java', 'C++', 'Python', 'Javascript', 'C#', 'C', 'Kotlin']
    

Then after every 13 seconds, the items of the list will be displayed as:

    
    
    Java
    C++
    Python
    Javascript
    C#
    C
    Kotlin
    
    

**Code #6:** Time Delay in a **List Comprehension**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing time package

import time

# creating and Initilizing a list

cricketers = ['Anil Kumble', 'Sachin Tendulkar', 'Sunil
Gavaskar', 'Rahul Dravid', 'Mahendra Singh Dhoni',

 'Dennis Lillee', 'Muttiah Muralitharan', 'Shane Warne']

# time delay of 7 seconds is created

# after every 7 seconds item of list gets displayed

cricketers = [(time.sleep(7), print(cric)) for cric in
cricketers]  
  
---  
  
 __

 __

 **Output:**

After every 7 seconds, the items of the list will be displayed as:

    
    
    Anil Kumble
    Sachin Tendulkar
    Sunil Gavaskar
    Rahul Dravid
    Mahendra Singh Dhoni
    Dennis Lillee
    Muttiah Muralitharan
    Shane Warne
    
    

**Code #7:** Creating a Time Delay of **3 minutes** in List

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing time package

import time

# creating and Initilizing a list

Languages = ['Java', 'C++', 'Python', 'Javascript',
'C#', 'C', 'Kotlin']

# creating a time delay of 3 minutes

time.sleep(3 * 60)

# the list will be displayed after the delay of 3 minutes

print(Languages)  
  
---  
  
 __

 __

 **Output:**

After the delay of 3 minutes, the list will be displayed as:

    
    
    ['Java', 'C++', 'Python', 'Javascript', 'C#', 'C', 'Kotlin']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

