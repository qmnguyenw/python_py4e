Python – Measure time taken by program to execute



This article aims to show how to measure the time taken by the program to
execute. Calculating time helps to optimize your Python script to perform
better.

 **Approach #1 :**  
A simple solution to it is to use **time** module to get the current time. The
following steps calculate the running time of a program or section of a
program.

  * Store the starting time before the first line of the program executes.
  * Store the ending time after the last line of the program executes.
  * Print the difference between start time and end time.

 **Code #1 :**

 __

 __  
 __

 __

 __  
 __  
 __

# Code to Measure time taken by program to execute.

import time

 

# store starting time

begin = time.time()

 

# program body starts

 

for i in range(5):

 print("GeeksForGeeks")

# program body ends

 

time.sleep(1)

# store end time

end = time.time()

 

# total time taken

print(f"Total runtime of the program is {end - begin}")  
  
---  
  
 __

 __

 **Output:**

    
    
    GeeksForGeeks
    GeeksForGeeks
    GeeksForGeeks
    GeeksForGeeks
    GeeksForGeeks
    Total runtime of the program is 1.0010437965393066
    

  
**Approach #2 :** Using Timeit module

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# importing the required module

import timeit 

 

# code snippet to be executed only once 

mysetup = "from math import sqrt"

 

# code snippet whose execution time is to be measured 

mycode = ''' 

def example(): 

 mylist = [] 

 for x in range(100): 

 mylist.append(sqrt(x)) 

'''

 

# timeit statement 

print timeit.timeit(setup = mysetup, 

 stmt = mycode, 

 number = 10000)   
  
---  
  
__

__

**Output:**

    
    
    0.00119590759277

 **Note:** Output may vary depending on the system or server load.

To read more about Timeit modulule, refer – Timeit in Python with Examples

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

