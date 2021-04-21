Python | yield Keyword



 **yield** is a keyword in Python that is used to return from a function
without destroying the states of its local variable and when the function is
called, the execution starts from the last yield statement. Any function that
contains a yield keyword is termed as generator. Hence, yield is what makes a
generator. yield keyword in Python is less known off but has a greater utility
which one can think of.  
  
 **Code #1 :** Demonstrating yield working

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# yield keyword

 

# generator to print even numbers

def print_even(test_list) :

 for i in test_list:

 if i % 2 == 0:

 yield i

 

# initializing list 

test_list = [1, 4, 5, 6, 7]

 

# printing initial list

print ("The original list is : " + str(test_list))

 

# printing even numbers 

print ("The even numbers in list are : ", end = " ")

for j in print_even(test_list):

 print (j, end = " ")  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 4, 5, 6, 7]
    The even numbers in list are :  4 6 
    

  
**Code #2:**

 __

 __  
 __

 __

 __  
 __  
 __

# A Python program to generate squares from 1

# to 100 using yield and therefore generator 

 

# An infinite generator function that prints 

# next square number. It starts with 1 

def nextSquare(): 

 i = 1; 

 

 # An Infinite loop to generate squares 

 while True: 

 yield i*i 

 i += 1 # Next execution resumes 

 # from this point 

 

# Driver code 

for num in nextSquare(): 

 if num > 100: 

 break

 print(num)   
  
---  
  
__

__

**Output:**

    
    
    1
    4
    9
    16
    25
    36
    49
    64
    81
    100

 **Advantages of yield:**

  

  

  * Since it stores the local variable states, hence overhead of memory allocation is controlled.
  * Since the old state is retained, flow doesn’t start from the beginnning and hence saves time.

 **Disadvantages of yield:**

  * Sometimes, the use of yield becomes erroneous is calling of function is not handled properly.
  * The time and memory optimization has a cost of complexity of code and hence sometimes hard to understand logic behind it.

 **Practical Applications:**  
The possible practical application is that when handling the last amount of
data and searching particulars from it, yield can be used as we don’t need
to lookup again from start and hence would save time. There can possibly be
many application of yield depending upon the use cases.  

__

__  
__

__

__  
__  
__

# Python3 code to demonstrate yield keyword

 

# Checking number of occurrence of 

# geeks in string 

 

# generator to print even numbers

def print_even(test_string) :

 for i in test_string:

 if i == "geeks":

 yield i

 

# initializing string

test_string = " The are many geeks around you, \

 geeks are known for teaching other geeks"

 

# printing even numbers using yield

count = 0

print ("The number of geeks in string is : ", end = "" )

test_string = test_string.split()

 

for j in print_even(test_string):

 count = count + 1

 

print (count)  
  
---  
  
 __

 __

 **Output :**

    
    
    The number of geeks in string is : 3

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

